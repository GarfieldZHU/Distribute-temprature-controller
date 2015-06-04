#coding=utf-8
#__author__ = 'Garfield'

from database import MySqlDB
import jsonrpc_handle

class ServerHandle:
    #主服务类，用于统一调度所有温控模块和管理数据
    def __init__(self):
        pass


    def run(self):
        jsonrpc_handle.main()


    def pause(self):
        pass

    def shutdown(self):
        pass
