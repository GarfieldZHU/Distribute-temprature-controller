#coding=utf-8
#__author__ = 'Garfield'

import time
import threading
from datetime import *
from database import MySqlDB
from controller import Controller
#from Queue import Queue
#from Queue import PriorityQueue


class ServerHandle:
    #主服务类，用于统一调度所有温控模块和管理数据
    def __init__(self):
        self._db = MySqlDB()
        self._controllers = {}
        self._mode = 'cold'
        self._maxTemp = 25
        self._minTemp = 20
        self.dispatch_list = []

    def init(self):
        rooms = self._db.query_user_room()
        print "- [test-msg] <rooms>", rooms
        threading.Thread(target=self.serve_thread).start()
        for item in rooms:
            ctl = Controller(item[0], self._mode)
            self._controllers[item[0]] = ctl

    def get(self, i):
        res = self._db.query_client(i)
        msg = {}
        msg['ison'] = True if res['ison'] else False
        msg['fanLevel'] = res['fanLevel']
        msg['targetTemperature'] = res['targetTemp']
        msg['cost'] = float(res['cost'])
        msg['maxTemperature'] = self._maxTemp
        msg['minTemperature'] = self._minTemp
        msg['temperature'] = res['curTemp']
        msg['isCentralOn'] = True
        print "- [test-msg] <get>", msg
        return msg

    def set(self, item):
        #print item
        if item[2] <= 3 and item[2] >= 1 and \
                item[1] >= self._minTemp and item[1] <= self._maxTemp:
            self._db.update_client_query(item)
            print "-[test-msg] <set> success"
            return True
        else:
            return False

    def record(self, item):
        self._db.update_list(item)
        print "-[test-record] ", item

    def get_db(self):
        return self._db

    def get_controller(self, id):
        if self._controllers[id]:
            return self._controllers[id]
        else:
            return None

    def add_controller(self, id, controller):
        self._controllers[id] = controller

    def del_controller(self, id, controller):
        del self._controllers[id]

    def run(self):
        while True:
            pass

    def pause(self):
        pass

    def shutdown(self):
        pass

    def serve_thread(self):
        #服务线程，流程为取任务(阻塞式)--服务--完成
        #高风速1分钟变化1度，中风速2分钟变化1度，低风速3分钟变化1度
        #温度变化1度金额1元
        print "- [serve] <thread> serve thread start."

        while True:
            self.dispatch()

            for id in ['301', '302', '303', '304', '305']:
                c = self._controllers.get(id, 'not found')
                if c in self.dispatch_list:
                    c.update_temperature()
                    c.update_cost()

                    temp = c.get_temp()
                    cost = c.get_cost()
                    print "- [serve] <time> ", now_time, "\t<temprature>", temp, \
                        "\t<cost> ", cost
                    room_id = c.get_room()
                    item = (temp, cost, room_id)
                    self._db.update_result(item)

            time.sleep(1)


    def dispatch(self):
        print "- [dispatch] set dispatch queue"
        for id in ['301', '302', '303', '304', '305']:
            c = self._controllers.get(id, 'not found')
