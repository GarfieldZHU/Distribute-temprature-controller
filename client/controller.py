#coding=utf-8
#__author__ = 'Garfield'

import json
import urllib


class Controller:
    #控制器类，含有jsonrpc客户端,可以远程调用主机的控制方法
    def __init__(self, room_num):
        self._id = room_num
        self._ison = False
        self._curTemp = 25
        self._goalTemp = 25
        self._fanLevel = 1
        self._cost = 0
        self._url = "http://localhost:8888/jsonrpc"

        self.MAXTEMP = 30
        self.MINTEMP = 20

    def get(self):
        state = request(self._url, "get", self._id)
        self.MAXTEMP = state['maxTemprature']
        self.MINTEMP = state['minTemprature']
        return state

    def set(self, state):
        print self._id
        return request(self._url, "set", self._id, state)

    def rise_temp(self):
        if self._goalTemp < self.MAXTEMP:
            if self.set({"temprature": self._goalTemp}):
                self._goalTemp += 1

    def reduce_temp(self):
        if self._goalTemp > self.MINTEMP:
            if self.set({"temprature": self._goalTemp}):
                self._goalTemp -= 1

    def rise_fan(self):
        if self._fanLevel < 3:
            if self.set({"fanlevel": self._fanLevel}):
                self._fanLevel += 1

    def reduce_fan(self):
        if self._fanLevel > 1:
            if self.set({"fanlevel": self._fanLevel}):
                self._fanLevel -= 1

    def is_on(self):
        return self._ison

    def get_cur_temp(self):
        return self._curTemp

    def get_temp(self):
        return self._goalTemp

    def get_fan(self):
        return self._fanLevel

    def get_cost(self):
        return self._cost

    def start_up(self):
        #从控机开机
        self._ison = True
        self.set({"ison": True})

    def power_off(self):
        #从控机关机
        self._ison = False
        self.set({"ison": False})

    def update(self, state):
        self._cost = state['cost']

    def test(self):
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
