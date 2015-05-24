#coding=utf-8
#__author__ = 'Garfield'

from mqtt_server import *


class Controller:
    #服务端温控模块类，用于和对应从控机交互
    def __init__(self):
        self._state = 'off'
        self._temp = 25
        self._mqtt = MqttServer()