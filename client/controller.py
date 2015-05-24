#coding=utf-8
#__author__ = 'Garfield'

from json_form import *
from mqtt_client import *


class Controller:
    def __init__(self, room_num):
        self._id = room_num
        self._state = 'off'
        self._curTemp = 25
        self._goalTemp = 25
        self._fanLevel = 1
        self._mqtt = MqttClient()

    def set_temp(self, goal):
        self._goalTemp = goal

    def set_fan(self, goal):
        self._fanLevel = goal

    def get_cur_temp(self):
        return self._curTemp

    def get_temp(self):
        return self._goalTemp

    def get_fan(self):
        return self._fanLevel

    def start_up(self):
        #从控机开机
        self._state = 'on'

    def power_off(self):
        #从控机关机
        self._state = 'off'

    def set_state(self, method, tar_tmpr, fan_lvl):
        #从控机设置状态
        pass
