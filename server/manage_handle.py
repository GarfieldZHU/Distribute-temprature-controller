#coding=utf-8
#__author__ = 'Garfield'

import jsonrpc_handle
import sys
from PySide import QtCore, QtGui

class ManageHandle:
    #管理员类，用于完成系统后台管理操作
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.mySW = ControllerMainWindow()

    def run(self):
        self.mySW.show()
        sys.exit(app.exec_())

    def query(self):
        pass
