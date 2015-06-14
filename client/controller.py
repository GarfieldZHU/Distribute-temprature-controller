#coding=utf-8
#__author__ = 'Garfield'

from __future__ import division
import json
import paho.mqtt.client as mqtt
import sys
import datetime
import socket, sys

class Controller:
    #控制器类，含有jsonrpc客户端,可以远程调用主机的控制方法
    def __init__(self, room_id):
        self._id = room_id
        self._state = 'off'
        self._curTemp = 30
        self._goalTemp = 25
        self._fanLevel = 1
        self._cost = 0
        self._isCentralOn = True
        self._mode = -1
        self._finish = False
        self.MAXTEMP = 25
        self.MINTEMP = 20

        self._client = mqtt.Client('Client %s' % self._id)


    def run(self):
        self._client.on_message = on_message
        self._client.on_connect = on_connect
        self._client.on_publish = on_publish
        self._client.on_subscribe = on_subscribe
        self._client.on_log = on_log

        broker = "10.205.24.141"
        self._client.connect(broker, 1883, 60)
        self._client.subscribe('CentralACSystem')
        self._client.subscribe('CentralAC2%s' % self._id)

        self._client.loop_forever()

    def rise_temp(self):
        if self._goalTemp < self.MAXTEMP:
            self._goalTemp += 1
            msg = json.dumps({'method': 'requestserve', \
                'targettemperature': self._goalTemp, 'fanlevel': self._fanLevel})
            self._client.publish('%s2CentralAC' % self._id, msg)
            print "- [log] temperature rise to ", self._goalTemp
            print '- [publish]', msg, 'to "%s2CentralAC"' % self._id

    def reduce_temp(self):
        if self._goalTemp > self.MINTEMP:
            self._goalTemp -= 1
            msg = json.dumps({'method': 'requestserve', \
                'targettemperature': self._goalTemp, 'fanlevel': self._fanLevel})
            self._client.publish('%s2CentralAC' % self._id, msg)
            print "- [log] temperature down to ", self._goalTemp
            print '- [publish]', msg, 'to "%s2CentralAC"' % self._id

    def rise_fan(self):
        if self._fanLevel < 3:
            self._fanLevel += 1
            msg = json.dumps({'method': 'requestserve', \
                'targettemperature': self._goalTemp, 'fanlevel': self._fanLevel})
            self._client.publish('%s2CentralAC' % self._id, msg)
            print "- [log] fan level rise to ", self._fanLevel
            print '- [publish]', msg, 'to "%s2CentralAC"' % self._id

    def reduce_fan(self):
        if self._fanLevel > 1:
            self._fanLevel -= 1
            msg = json.dumps({'method': 'requestserve', \
                'targettemperature': self._goalTemp, 'fanlevel': self._fanLevel})
            self._client.publish('%s2CentralAC' % self._id, msg)
            print "- [log] fan level down to ", self._fanLevel
            print '- [publish]', msg, 'to "%s2CentralAC"' % self._id

    def get_state(self):
        return self._state

    def if_finish(self):
        return self._finish

    def get_cur_temp(self):
        return self._curTemp

    def get_temp(self):
        return self._goalTemp

    def get_fan(self):
        return self._fanLevel

    def get_cost(self):
        return self._cost

    def get_mode(self):
        return self._mode

    def set_state(self, state):
        self._state = state

    def set_curTemp(self, temp):
        self._curTemp = temp

    def set_cost(self, cost):
        self._cost = cost

    def cmp_temp(self):
        if self._mode == -1 and (self._curTemp - self._goalTemp) < 1:
            return True
        elif self._mode == 1 and (self._goalTemp - self.curTemp) < 1:
            return True
        else:
            return False

    def auto_change(self):
        if self._mode == -1:
            self._curTemp += 1/60
        else:
            self._curTemp -= 1/60

    def auto_request(self):
        #温度偏离1摄氏度后自动请求
        self._state = 'on'
        msg = json.dumps({'method': 'changed', \
            'targettemperature': self._goalTemp, 'fanlevel': self._fanLevel})
        self._client.publish('%s2CentralAC' % self._id, msg)

    def start_up(self):
        #从控机开机
        msg = json.dumps({'method': 'poweron', 'curtemperature': self._curTemp, \
            'targettemperature': self._goalTemp, 'fanlevel': self._fanLevel})
        self._client.publish('%s2CentralAC' % self._id, msg)
        #self._client.publish('02CentralAC', msg)
        print '- [publish]', msg, 'to "%s2CentralAC"' % self._id
        self._state = 'on'

    def power_off(self):
        #从控机关机
        msg = json.dumps({'method': 'poweroff'})
        self._client.publish('%s2CentralAC' % self._id, msg)
        self._ison = False
        print '- [publish]', msg, 'to "%s2CentralAC"' % self._id
        self._state = 'off'

    def update(self, state):
        self._cost = state['cost']



def on_connect(client, userdata, rc):
    print("Connected with result code " + str(rc))


def on_publish(client, userdata, mid):
    print("OnPublish, mid " + str(mid))


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(client, userdata, level, string):
    print("Log: " + string)


def on_message(client, userdata, msg):
    curtime = datetime.datetime.now()
    strcurtime = curtime.strftime("%Y-%m-%d %H-%M-%S")
    print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    #on_exec(str(msg.payload))
    res = json.loads(str(msg.payload))
    channel = 'CentralAC2%s' % cid
    print "- [publish arrived] ", res
    if msg.topic == channel and res['method'] == 'serve':
        controller.set_state(res['state'])
        controller.set_curTemp(res['curtemperature'])
        controller.set_cost(res['cost'])
    elif msg.topic == 'CentralACSystem':
        controller.set_mode(res['mode'])
        controller.MAXTEMP = res['maxtemperature']
        controller.MINTEMP = res['mintemperature']
        if res['state'] == 'on':
            controller._isCentralOn = True
        else:
            controller._isCentralOn = False


def on_exec(strcmd):
    print("Exec: ", strcmd)
    #strExec = strcmd

## --------------------------------------

cid = '0'
controller = Controller(cid)

if __name__ == '__main__':
    controller.run()
