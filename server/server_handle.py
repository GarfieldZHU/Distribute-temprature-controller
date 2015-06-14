#coding=utf-8
#__author__ = 'Garfield'

import sys
import json
import socket, sys
import threading
from time import sleep
from database import MySqlDB
from controller import Controller
from manage_handle import ManageHandle
#from Queue import Queue
#from Queue import PriorityQueue
from controller import *
import paho.mqtt.client as mqtt
import datetime

COLD = -1
WARM = 1

class ServerHandle:
    #主服务类，用于统一调度所有温控模块和管理数据
    #Mqtt服务器类，用于订阅服务端的消息
    def __init__(self):
        self._db = MySqlDB()
        self._controllers = {}
        self._mode = COLD
        self._maxTemp = 25
        self._minTemp = 15
        self.dispatch_list = []
        self.priority_list = {}
        self.dispatched_list = []
        self.serve_flag = []
        self.dispatch_priority = 3
        self.rooms = self._db.query_user_room()
        self._ison = True
        print "- [rooms] ", self.rooms


        self._server = mqtt.Client('master')

    def init(self):
        print "- [test-msg] <rooms>", self.rooms
        self._server.on_connect = on_connect
        self._server.on_message = on_message
        self._server.on_publish = on_publish
        self._server.on_subscribe = on_subscribe
        self._server.on_log = on_log

        broker = "10.205.24.141"
        #broker = "localhost"
        self._server.connect(broker, 1883, 60)
        #订阅所有主频道
        for item in self.rooms:
            ctl = Controller(item[0], self._mode, self._db)
            self._controllers[item[0]] = ctl
            #topic = '%s2CentralAC' % item[0]
            #print topic
            #self._server.subscribe(topic)

        self._server.subscribe('02CentralAC')
        self._server.subscribe('12CentralAC')
        self._server.subscribe('22CentralAC')
        self._server.subscribe('32CentralAC')
        self._server.subscribe('42CentralAC')

        msg = json.dumps({'state': 'on', 'mode': self._mode, \
            'maxtemperature': self._maxTemp, 'mintemperature': self._minTemp})
        self._server.publish('CentralACSystem', msg)
        threading.Thread(target=self.serve_thread).start()
        threading.Thread(target=self.send_thread).start()
        #self._manage_handle = ManageHandle()

    def record(self, item):
        self._db.update_list(item)
        print "- [record] ", item

    def get_db(self):
        return self._db

    def get_controller(self, id):
        return self._controllers.get(id, 'not found')

    def add_controller(self, id, controller):
        self._controllers[id] = controller

    def del_controller(self, id, controller):
        del self._controllers[id]

    def get_mode(self):
        return self._mode

    def run(self):
        #self._client.reinitialise(1)
        self._server.loop_forever()


    def startup(self):
        msg = json.dumps({'state': 'on', 'mode': self._mode, \
            'maxtemperature': self._maxTemp, 'mintemperature': self._minTemp})
        self._server.publish('CentralACSystem', msg)
        self._ison = True

    def reset(self, mode):
        self._mode = mode
        msg = json.dumps({'state': 'on', 'mode': self._mode, \
            'maxtemperature': self._maxTemp, 'mintemperature': self._minTemp})
        self._server.publish('CentralACSystem', msg)
        self._ison = True

    def shutdown(self):
        msg = json.dumps({'state': 'off'})
        self._server.publish('CentralACSystem', msg)
        self._ison = False

    def send_thread(self):
        #计时每60s向客户端发送一次温度变化和费用
        while True:
            for item in self.rooms:
                client_id = item[0]
                ctl = self._controllers.get(client_id, 'not found')
                temp = ctl.get_temp()
                cost = ctl.get_cost()
                if ctl.if_finish():
                    state = 'standby'
                else:
                    state = 'on'
                msg = json.dumps({'method': "serve", "curtemperature": temp, \
                    "state": state, "cost": cost})
                self._server.publish("CentralAC2%s" % client_id, msg)
            sleep(60)

    def serve_thread(self):
        #服务线程，流程为取任务(阻塞式)--服务--完成
        #温度变化1度金额1元
        print "- [serve] <thread> serve thread start."

        while True:
            self.dispatch()
            for item in self.rooms:
                id = item[0]
                ctl = self._controllers.get(id, 'not found')
                if ctl in self.dispatch_list:
                    print "- [serve] serve room", id
                    ctl.update_temperature()
                    ctl.update_cost()

                    if ctl.if_finish():
                        item = (ctl.get_room(), ctl.get_beginTime(), \
                            ctl.get_endTime(), self._mode, ctl.get_fan(), \
                            ctl.get_beginTemp(), ctl.get_endTemp(), \
                            ctl.get_delta())
                        self._db.insert_list(item)
                    temp = ctl.get_temp()
                    cost = ctl.get_cost()
                    if ctl.if_task():
                        print "- [serve] <time> ", datetime.datetime.now(), \
                            "\t<temprature>", round(temp,2), "\t<cost> ", \
                            round(cost,2)
                        room_id = ctl.get_room()
                        item = (temp, cost, room_id)
                        self._db.update_client_result(item)
                    else:
                        print "- [serve] task finish"

            sleep(1)


    def dispatch(self):
        #print "- [dispatch] set dispatch queue"
        to_serve = []
        priority = 3
        self.dispatch_list = []
        self.dispatch_priority = 3

        for item in self.rooms:
            #计算各个任务的优先级
            id = item[0]
            #print id
            ctl = self._controllers.get(id, 'fail to get controller')
            self.priority_list[id] = ctl.get_priority()

        while len(to_serve) < 3 and priority >= 1:
            self.dispatch_priority = priority
            #设置最小的即需要轮转的优先级
            for item in self.rooms:
                id = item[0]
                if self.priority_list[id] == priority:
                    to_serve.append(id)
            priority -= 1

        if len(to_serve) <= 3:
            #不需要调度时，将任务全部加入调度列表
            print "- [dispatch] don't need to dispatch"
            for id in to_serve:
                #print 'to_serve', id
                if self._controllers[id].if_task() and self._controllers[id].if_on():
                    self.dispatch_list.append(self._controllers.get(id, \
                        'not found'))
                    #print "~~~temp", self._controllers[id].get_temp()
        else:
            #需要调度时
            if cmp(dispatched_list, to_serve):
                #和上一次服务列表相同，则说明需要轮转
                print "- [dispatch] time span"
                i = 0
                while serve_flag[i] != 1:
                    i += 1
                serve_in = i
                while serve_flag[i] != 0:
                    i += 1
                serve_out = i
                serve_flag[serve_in] = 1
                serve_flag[serve_out] = 0
            else:
                #和上一次服务列表不同，则进入一次新的轮转
                print "- [dispatch] new span"
                serve_flag = [-1 for i in range(to_serve)]
                i = 0
                for id in to_serve:
                    if self.priority_list[id] > self.dispatched_priority:
                        #必然进入调度列表
                        self.serve_flag[i] = 2
                        self.dispatch_list.append(self._controllers[to_serve[i]])
                    i += 1
                i = 0
                while len(dispatch_list) < 3:
                    item = self.rooms[i]
                    id = item[0]
                    if self.priority_list[id] == self.dispatched_priority:
                        #被调入优先列表的
                        self.serve_flag[i] = 1
                        self.dispatch_list.append(self._controllers[to_serve[i]])
                    i += 1
                for i in range(0, len(to_serve)):
                    if serve_flag[i] != 2 and serve_flag != 1:
                        serve_flag[i] = 0
        self.dispatched_list = to_serve
        print "- [dispatch] <list> ", self.dispatch_list


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
    print strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload)
    #on_exec(str(msg.payload))
    res = json.loads(str(msg.payload))
    print '- [publish arrived] ', res
    if res['method'] == 'poweron':
        client_id = msg.topic.replace('2CentralAC','')
        print "- [set] room ", client_id , "power on"
        curTemp = res['curtemperature']
        fan = res['fanlevel']
        target = res['targettemperature']
        data = server.get_db().query_client(client_id)
        print "- [get from database] ", data
        temp = data['curTemp']
        cost = float(data['cost'])

        server.get_controller(client_id).set_task(target, fan, curTemp, cost)
        server.get_controller(client_id).startup()

    elif res['method'] == 'poweroff':
        client_id = msg.topic.replace('2CentralAC','')
        server.get_controller(client_id).poweroff()
        curTemp = server.get_controller(client_id).get_temp()
        cost = server.get_controller(client_id).get_cost()
        item = (curTemp, cost, client_id)
        server.get_db().update_client_result(item)
        server.get_controller(client_id).finish_task()
        print "- [set] room ", client_id , "power off"
        item = ('off', client_id)
        server.get_db().update_client_state(item)

    elif res['method'] == 'requestserve':
        #print '- [requestserve]:'
        client_id = msg.topic.replace('2CentralAC','')
        data = server.get_db().query_client(client_id)
        cost = data['cost']
        temp = data['curTemp']
        print '- [REQUEST data]', data
        server.get_controller(client_id).set_task(res['targettemperature'],
            res['fanlevel'], temp, float(cost))
        print "- [task] <set>", res['targettemperature'], res['fanlevel'], temp, cost
    elif res['method'] == 'changed':
        client_id = msg.topic.replace('2CentralAC','')
        data = server.get_db().query_client(client_id)
        cost = data['cost']
        temp = data['curTemp'] + 1
        server.get_controller(client_id).set_task(res['targettemperature'],
            res['fanlevel'], temp, float(cost))

def on_exec(strcmd):
    print("Exec: ", strcmd)
    #strExec = strcmd


## --------------------------------

server = ServerHandle()

if __name__ == '__main__':
    server.init()
    server.run()
