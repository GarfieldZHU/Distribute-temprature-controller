#coding=utf-8
#__author__ = 'Garfield'

import time


class Controller:
    #服务端温控模块类，用于和对应从控机交互
    def __init__(self, room_id, mode):
        self._room = room_id
        self._task = [0, 0, 0]
        self._delta = 0
        self._priority = 0
        self._time = 0
        self._cost = 0
        self._mode = mode
        self.serve_permission = True

    def set_task(self, target, fan, temp):
        self._task = [target, fan, float(temp)]
        self._priority = fan
        self.in_time = time.time()

    def finish_task(self):
        self._task = []
        self._priority = 0
        self._time = 0
        self.start_time = 0

    def if_finish(self):
        if self._task[0] == self._task[2]:
            return True
        else:
            return False

    def change_temp(self, temp):
        self._task[2] = temp

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

    def if_task(self):
        if cmp(self._task, []):
            return False
        else:
            return True

    def update_temperature(self):
        cur = self._task[2]
        target = self._task[0]
        fan = self._task[1]
        if self._mode == 'cold':
            if cur > target:
                cur -= 1/180 * fan
                delta += 1/180 * fan
            else:
                cur += 1/180
        else:
            if cur < target:
                cur += 1/180 * fan
                delta += 1/180 * fan
            else:
                cur -= 1/180

    def update_cost(self):
        self._cost = delta

    def set_priority(self):
        #根据任务在主控端已等待的时间提高优先级
        #self.wait_time = int(time.time() - self.in_time)
        #self._priority = self._task[1] + (self.wait_time / 30)
        self._priority = self._task[1]

    def get_priority(self):
        return self._priority
