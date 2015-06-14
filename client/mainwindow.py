# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Jun  2 16:12:17 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

import sys
import time
import threading
from PySide import QtCore, QtGui
import controller

RELAY_TIME = 1000
REQUEST_TIME = 60000
#设定按键延迟等待的时间和自动变化温度时间，单位毫秒


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 340)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.switchButton = QtGui.QPushButton(self.centralWidget)
        self.switchButton.setGeometry(QtCore.QRect(330, 30, 81, 41))
        self.switchButton.setObjectName("switchButton")
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 211, 251))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.curTemp = QtGui.QLCDNumber(self.frame)
        self.curTemp.setGeometry(QtCore.QRect(30, 60, 151, 31))
        self.curTemp.setObjectName("curTemp")
        self.curTemp.display('25')
        self.targetTemp = QtGui.QLCDNumber(self.frame)
        self.targetTemp.setGeometry(QtCore.QRect(30, 110, 151, 31))
        self.targetTemp.setObjectName("targetTemp")
        self.targetTemp.display('25')
        self.stateLabel = QtGui.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(30, 10, 141, 31))
        self.stateLabel.setText("\t--Off--")
        self.stateLabel.setObjectName("stateLabel")
        self.speedLabel = QtGui.QLabel(self.frame)
        self.speedLabel.setGeometry(QtCore.QRect(30, 165, 151, 21))
        self.speedLabel.setText("\t------")
        self.speedLabel.setObjectName("speedLabel")
        self.totalCost = QtGui.QLCDNumber(self.frame)
        self.totalCost.setGeometry(QtCore.QRect(30, 200, 151, 31))
        self.totalCost.setObjectName("totalCost")
        self.totalCost.display('0.00')
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(240, 90, 59, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(240, 140, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(240, 180, 61, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(240, 230, 59, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(240, 40, 59, 16))
        self.label_5.setObjectName("label_5")
        self.tempDown = QtGui.QPushButton(self.centralWidget)
        self.tempDown.setGeometry(QtCore.QRect(380, 140, 61, 32))
        self.tempDown.setObjectName("tempDown")
        self.speedUp = QtGui.QPushButton(self.centralWidget)
        self.speedUp.setGeometry(QtCore.QRect(310, 180, 61, 32))
        self.speedUp.setObjectName("speedUp")
        self.tempUp = QtGui.QPushButton(self.centralWidget)
        self.tempUp.setGeometry(QtCore.QRect(310, 140, 61, 32))
        self.tempUp.setObjectName("tempUp")
        self.speedDown = QtGui.QPushButton(self.centralWidget)
        self.speedDown.setGeometry(QtCore.QRect(380, 180, 61, 32))
        self.speedDown.setObjectName("speedDown")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar()
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 442, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "空调从控机控制面板", None, QtGui.QApplication.UnicodeUTF8))
        self.switchButton.setText(QtGui.QApplication.translate("MainWindow", "开/关", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "当前温度", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "目标温度", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "风速", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "消费金额", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "工作状态", None, QtGui.QApplication.UnicodeUTF8))
        self.tempDown.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.speedUp.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.tempUp.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.speedDown.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Controller", None, QtGui.QApplication.UnicodeUTF8))


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.if_end = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initDisplay()
        self.ui.switchButton.clicked.connect(self.switch)
        self.ui.tempUp.clicked.connect(self.riseTemp)
        self.ui.tempDown.clicked.connect(self.reduceTemp)
        self.ui.speedUp.clicked.connect(self.riseSpeed)
        self.ui.speedDown.clicked.connect(self.reduceSpeed)
        self.timer = QtCore.QTimer(self)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.send_update)
        #self.auto_timer = QtCore.QTimer(self)
        #self.connect(self.auto_timer, QtCore.SIGNAL("timeout()"), self.auto_request)
        self.task = ''

        threading.Thread(target=self.update_thread).start()
        threading.Thread(target=self.run_thread).start()

    def initDisplay(self):
        self.ui.curTemp.display(int(controller.controller.get_cur_temp()))
        self.ui.targetTemp.display(int(controller.controller.get_temp()))
        self.setSpeed(controller.controller.get_fan())
        self.ui.totalCost.display(controller.controller.get_cost())

    def send_update(self):
        if self.task == 'poweroff':
            controller.controller.power_off()
            self.ui.stateLabel.setText("\t--Off--")
            print "- [log] Power off..."
        elif self.task == 'startup':
            controller.controller.start_up()
            self.ui.stateLabel.setText("\t--On--")
            print "- [log] Start up..."
        elif self.task == 'risetemp':
            controller.controller.rise_temp()
            self.ui.targetTemp.display(controller.controller.get_temp())
        elif self.task == 'reducetemp':
            controller.controller.reduce_temp()
            self.ui.targetTemp.display(controller.controller.get_temp())
        elif self.task == 'risespeed':
            controller.controller.rise_fan()
            speed = controller.controller.get_fan()
            self.setSpeed(speed)
        elif self.task == 'reducespeed':
            controller.controller.reduce_fan()
            speed = controller.controller.get_fan()
            self.setSpeed(speed)
        self.timer.stop()

    def switch(self):
        if controller.controller.get_state() == 'on':
            self.timer.start(RELAY_TIME)
            self.task = 'poweroff'
        else:
            self.timer.start(RELAY_TIME)
            self.task = 'startup'

    def riseTemp(self):
        self.timer.start(RELAY_TIME)
        self.task = 'risetemp'

    def reduceTemp(self):
        self.timer.start(RELAY_TIME)
        self.task = 'reducetemp'

    def riseSpeed(self):
        self.timer.start(RELAY_TIME)
        self.task = 'risespeed'

    def reduceSpeed(self):
        self.timer.start(RELAY_TIME)
        self.task = 'reducespeed'

    def setSpeed(self, speed):
        i = 6
        text = '\t'
        while i > 0:
            if i > speed*2:
                text += '-'
            else:
                text += '#'
            i -= 1
        self.ui.speedLabel.setText(text)

    def run_thread(self):
        controller.controller.run()

    def update_thread(self):
        while not self.if_end:
            if controller.controller.get_state() == 'on':
                self.ui.curTemp.display(int(controller.controller.get_cur_temp()))
                self.ui.totalCost.display(controller.controller.get_cost())
            elif controller.controller.get_state() == 'standby':
                if controller.controller.cmp_temp():
                    controller.controller.auto_change()
                else:
                    controller.controller.auto_request()
            time.sleep(1)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
    mySW.if_end = True
