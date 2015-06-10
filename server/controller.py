#coding=utf-8
#__author__ = 'Garfield'

from __future__ import division
import time
from datetime import *


class Controller:
    #服务端温控模块类，用于和对应从控机交互
    def __init__(self, room_id, mode):
        self._room = room_id
        self._task = [-1, -1, -1]
        self._delta = 0.0
        self._cost = 0.0
        self._priority = 0
        self._cost = 0.0
        self._mode = mode
        self.serve_permission = True
        self.RATE = 1/180

    def set_task(self, target, fan, temp, cost):
        self._task = [target, fan, float(temp)]
        self._priority = fan
        self.begin_time = datetime.now()
        self.begin_temp = temp
        print "<controller> set task", self._task
        self._cost = cost

    def finish_task(self):
        print "<controller> task finished"
        self._task = [-1, -1, -1]
        self._priority = 0
        self._time = 0
        self._delta = 0
        self.end_time = datetime.now()
        self.end_temp = self._task[2]

    def if_finish(self):
        if self._task[0] == self._task[2]:
            return True
        else:
            return False

    def set_cost(self, cost):
        self._cost = cost

    def set_temp(self, temp):
        self._task[2] = temp

    def get_room(self):
        return self._room

    def get_fan(self):
        return self._task[1]

    def get_temp(self):
        return self._task[2]

    def get_cost(self):
        return self._cost

    def get_beginTemp(self):
        return self.begin_temp

    def get_endTemp(self):
        return self.end_temp

    def get_beginTime(self):
        return self.begin_time

    def get_endTime(self):
        return self.end_time

    def if_task(self):
        if cmp(self._task, [-1, -1, -1]) == 0:
            print '<controller> task not exist'
            return False
        else:
            return True

    def update_temperature(self):
        #高风速1分钟变化1度，中风速2分钟变化1度，低风速3分钟变化1度
        cur = self._task[2]
        target = self._task[0]
        fan = self._task[1]
        if self._mode == 'cold':
            if cur > target:
                cur -= self.RATE * fan
                self._delta = self.RATE * fan
                self._task[2] = cur
            else:
                self.finish_task()
                #cur += self.RATE
        else:
            if cur < target:
                cur += self.RATE * fan
                self._delta = self.RATE * fan
                self._task[2] = cur
            else:
                self.finish_task()
                #cur -= self.RATE

    def update_cost(self):
        #消费金额为1元每变化1度
        self._cost += self._delta * 1

    def set_priority(self):
        #根据任务在主控端已等待的时间提高优先级
        #self.wait_time = int(time.time() - self.in_time)
        #self._priority = self._task[1] + (self.wait_time / 30)
        self._priority = self._task[1]
        print "- [controller] <room> ", self._room, " <priority> ", \
            self._priority

    def get_priority(self):
        return self._priority
