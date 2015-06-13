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
        self._isCentralOn = True
        self._mode = 'cold'
        self._finish = False
        self.MAXTEMP = 25
        self.MINTEMP = 20

    def get(self):
        state = request(self._url, "get", self._id)
        if state is not None:
            self.MAXTEMP = state['maxTemperature']
            self.MINTEMP = state['minTemperature']
            self._fanLevel = state['fanLevel']
            self._curTemp = state['temperature']
            self._goalTemp = state['targetTemperature']
            self._cost = state['cost']
            self._isCentralOn = state['isCentralOn']
            if self.MAXTEMP >= 28:
                self._mode = 'warm'
            else:
                self._mode = 'cold'
            if state['temperature'] == self._goalTemp:
                self._finish = True
            else:
                self._finish = False
            print "- [log] <get>: ", state
            return True
        else:
            return False
        #return state

    def set(self, state):
        #print self._id
        return request(self._url, "set", self._id, state)

    def rise_temp(self):
        if self._goalTemp < self.MAXTEMP:
            self._goalTemp += 1
            self.set({"ison": self._ison, "fanLevel": self._fanLevel, \
                "targetTemperature": self._goalTemp})
            print "- [log] temperature rise to ", self._goalTemp

    def reduce_temp(self):
        if self._goalTemp > self.MINTEMP:
            self._goalTemp -= 1
            self.set({"ison": self._ison, "fanLevel": self._fanLevel, \
                "targetTemperature": self._goalTemp})
            print "- [log] temperature down to ", self._goalTemp

    def rise_fan(self):
        if self._fanLevel < 3:
            self._fanLevel += 1
            self.set({"ison": self._ison, "fanLevel": self._fanLevel, \
                "targetTemperature": self._goalTemp})
            print "- [log] fan level rise to ", self._fanLevel

    def reduce_fan(self):
        if self._fanLevel > 1:
            self._fanLevel -= 1
            self.set({"ison": self._ison, "fanLevel": self._fanLevel, \
                "targetTemperature": self._goalTemp})
            print "- [log] fan level down to ", self._fanLevel

    def is_on(self):
        return self._ison

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

    def resume_temp(self):
        if self._mode == 'cold':
            self._curTemp += 1
        else:
            self._curTemp -= 1

    def start_up(self):
        #从控机开机
        self.set({"ison": True, "fanLevel": self._fanLevel, \
            "targetTemperature": self._goalTemp})
        self._ison = True

    def power_off(self):
        #从控机关机
        self.set({"ison": False, "fanLevel": self._fanLevel, \
            "targetTemperature": self._goalTemp})
        self._ison = False

    def update(self, state):
        self._cost = state['cost']

    def test(self):
        print self.get()
        self.set({ "ison": True, "fanLevel": 2, "temperature":24 })
        print self.get()


def request(url, func, *args):
    req = json.dumps({"method": func, "params": args, "id": 1})
    result = ''
    try:
        result = urllib.urlopen(url, req).read()
    except:
        print '- [JsonRpc] <Fail> Server is not online'
        return None
    try:
        #print result
        response = json.loads(result)
        #print response
    except:
        return "error: %s" % result
    else:
        res = response.get("result", response.get("error"))
        #print res
        return res
