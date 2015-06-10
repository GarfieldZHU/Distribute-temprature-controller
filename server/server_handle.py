#coding=utf-8
#__author__ = 'Garfield'

import time
import datetime
import threading
from database import MySqlDB
from controller import Controller
from manage_handle import ManageHandle
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
        self.priority_list = {}
        self.dispatched_list = []
        self.serve_flag = []
        self.dispatch_priority = 3
        self.rooms = self._db.query_user_room()

    def init(self):
        print "- [test-msg] <rooms>", self.rooms
        for item in self.rooms:
            ctl = Controller(item[0], self._mode)
            self._controllers[item[0]] = ctl
        threading.Thread(target=self.serve_thread).start()
        self._manage_handle = ManageHandle()
        threading.Thread(target=self._manage_handle.run).start()

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
        print "- [get-msg] <get>", msg
        return msg

    def set(self, item):
        #print item
        if item[2] <= 3 and item[2] >= 1 and \
                item[1] >= self._minTemp and item[1] <= self._maxTemp:
            self._db.update_client_query(item)
            print "- [set-msg] <set> success"
            return True
        else:
            return False

    def auto_set(self, i):
        #自动变温函数
        curTemp = self._db.query_client(i)['curTemp']
        if self._mode == 'cold':
            item = (curTemp+1, i)
        else:
            item = (curTemp-1, i)
        self._db.update_client_(item)

    def record(self, item):
        self._db.update_list(item)
        print "- [record] ", item

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
        self._manage_handle.run()

    def pause(self):
        pass

    def shutdown(self):
        pass

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
                            ctl.get_beginTemp(), ctl.get_endTemp())
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

            time.sleep(1)


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
            for id in to_serve:
                #print 'to_serve', id
                if self._controllers[id].if_task():
                    self.dispatch_list.append(self._controllers.get(id, \
                        'not found'))
                    #print "~~~temp", self._controllers[id].get_temp()
        else:
            #需要调度时
            if cmp(dispatched_list, to_serve):
                #和上一次服务列表相同，则说明需要轮转
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
