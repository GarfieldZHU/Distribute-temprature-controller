#coding=utf-8
#__author__ = 'Garfield'

import json
import urllib


class Controller:
    #控制器类，含有jsonrpc客户端,可以远程调用主机的控制方法
    def __init__(self, room_num):
        self._id = room_num
        self._ison = True
        self._curTemp = 25
        self._goalTemp = 25
        self._fanLevel = 1
        self._cost = 0
        self._url = "http://localhost:8888/jsonrpc"

    def get(self):
        return request(self._url, "get", self._id)

    def set(self, state):
        request(self._url, "set", self._id, state)

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

    def update(self, state):
        self._cost = state['cost']

    def run(self):
        print self.get()
        self.set({ "ison": True, "fanlevel": 2, "temperature":24 })
        print self.get()


def request(url, func, *args):
    req = json.dumps({"method": func, "params": args, "id": 1})
    result = urllib.urlopen(url, req).read()
    try:
        response = json.loads(result)
    except:
        return "error: %s" % result
    else:
        return response.get("result", response.get("error"))
