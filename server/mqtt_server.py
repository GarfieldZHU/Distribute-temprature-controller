#coding=utf-8
#__author__ = 'Garfield'

import paho.mqtt.client as mqtt


from controller import *
import paho.mqtt.client as mqtt
import sys
import datetime
import socket, sys


class MqttServer:
    #Mqtt服务器类，用于订阅服务端的消息
    def __init__(self):
        self._client = mqtt.Client('master')

    def run(self):
        try:
            #self._client.reinitialise(1)
            self._client.on_message = on_message
            self._client.on_connect = on_connect
            self._client.on_publish = on_publish
            self._client.on_subscribe = on_subscribe

            self._client.on_log = on_log

            #broker = "10.205.24.141"
            broker = "localhost"
            self._client.connect(broker, 1883, 60)
            self._client.subscribe('hello/world')
            self._client.publish('hello/world', 'Hello world')
            self._client.loop_forever()
        except ConnectionError:
            print("Paho-Mqtt fail to connect the mosquitto server")

    def send_message(self, client_id, msg):
        pass


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
    on_exec(str(msg.payload))


def on_exec(strcmd):
    print("Exec: ", strcmd)
    #strExec = strcmd

if __name__ == '__main__':
    pass