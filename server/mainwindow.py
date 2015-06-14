# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Jun 10 18:01:20 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

import sys
import threading
import time
from database import MySqlDB
from PySide import QtCore, QtGui
from dialog import ControllerDialog

class Ui_MainWindow(object):
    #管理员类，绘制管理圆界面
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 365)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(340, 10, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(460, 10, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(580, 10, 41, 16))
        self.label_5.setObjectName("label_5")
        self.curTemp1 = QtGui.QLCDNumber(self.centralWidget)
        self.curTemp1.setGeometry(QtCore.QRect(110, 40, 51, 21))
        font = QtGui.QFont()
        font.setFamily(".Helvetica Neue DeskInterface")
        self.curTemp1.setFont(font)
        self.curTemp1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.curTemp1.setObjectName("curTemp1")
        self.targetTemp1 = QtGui.QLCDNumber(self.centralWidget)
        self.targetTemp1.setGeometry(QtCore.QRect(110, 80, 51, 21))
        self.targetTemp1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.targetTemp1.setObjectName("targetTemp1")
        self.fanLevel1 = QtGui.QLCDNumber(self.centralWidget)
        self.fanLevel1.setGeometry(QtCore.QRect(110, 120, 51, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.fanLevel1.setFont(font)
        self.fanLevel1.setSmallDecimalPoint(False)
        self.fanLevel1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.fanLevel1.setProperty("intValue", 24)
        self.fanLevel1.setObjectName("fanLevel1")
        self.label_6 = QtGui.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(20, 40, 59, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 59, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(20, 120, 59, 16))
        self.label_8.setObjectName("label_8")
        self.cost1 = QtGui.QLCDNumber(self.centralWidget)
        self.cost1.setGeometry(QtCore.QRect(110, 160, 51, 21))
        self.cost1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.cost1.setObjectName("cost1")
        self.label_9 = QtGui.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(20, 160, 59, 16))
        self.label_9.setObjectName("label_9")
        #self.label_10 = QtGui.QLabel(self.centralWidget)
        #self.label_10.setGeometry(QtCore.QRect(20, 260, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        #self.label_10.setFont(font)
        #self.label_10.setObjectName("label_10")
        self.fanLevel2 = QtGui.QLCDNumber(self.centralWidget)
        self.fanLevel2.setGeometry(QtCore.QRect(210, 120, 51, 21))
        self.fanLevel2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.fanLevel2.setObjectName("fanLevel2")
        self.targetTemp2 = QtGui.QLCDNumber(self.centralWidget)
        self.targetTemp2.setGeometry(QtCore.QRect(210, 80, 51, 21))
        self.targetTemp2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.targetTemp2.setObjectName("targetTemp2")
        self.cost2 = QtGui.QLCDNumber(self.centralWidget)
        self.cost2.setGeometry(QtCore.QRect(210, 160, 51, 21))
        self.cost2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.cost2.setObjectName("cost2")
        self.curTemp2 = QtGui.QLCDNumber(self.centralWidget)
        self.curTemp2.setGeometry(QtCore.QRect(210, 40, 51, 21))
        self.curTemp2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.curTemp2.setObjectName("curTemp2")
        self.fanLevel3 = QtGui.QLCDNumber(self.centralWidget)
        self.fanLevel3.setGeometry(QtCore.QRect(330, 120, 51, 21))
        self.fanLevel3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.fanLevel3.setObjectName("fanLevel3")
        self.targetTemp3 = QtGui.QLCDNumber(self.centralWidget)
        self.targetTemp3.setGeometry(QtCore.QRect(330, 80, 51, 21))
        self.targetTemp3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.targetTemp3.setObjectName("targetTemp3")
        self.cost3 = QtGui.QLCDNumber(self.centralWidget)
        self.cost3.setGeometry(QtCore.QRect(330, 160, 51, 21))
        self.cost3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.cost3.setObjectName("cost3")
        self.curTemp3 = QtGui.QLCDNumber(self.centralWidget)
        self.curTemp3.setGeometry(QtCore.QRect(330, 40, 51, 21))
        self.curTemp3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.curTemp3.setObjectName("curTemp3")
        self.fanLevel4 = QtGui.QLCDNumber(self.centralWidget)
        self.fanLevel4.setGeometry(QtCore.QRect(450, 120, 51, 21))
        self.fanLevel4.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.fanLevel4.setObjectName("fanLevel4")
        self.targetTemp4 = QtGui.QLCDNumber(self.centralWidget)
        self.targetTemp4.setGeometry(QtCore.QRect(450, 80, 51, 21))
        self.targetTemp4.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.targetTemp4.setObjectName("targetTemp4")
        self.cost4 = QtGui.QLCDNumber(self.centralWidget)
        self.cost4.setGeometry(QtCore.QRect(450, 160, 51, 21))
        self.cost4.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.cost4.setObjectName("cost4")
        self.curTemp4 = QtGui.QLCDNumber(self.centralWidget)
        self.curTemp4.setGeometry(QtCore.QRect(450, 40, 51, 21))
        self.curTemp4.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.curTemp4.setObjectName("curTemp4")
        self.fanLevel5 = QtGui.QLCDNumber(self.centralWidget)
        self.fanLevel5.setGeometry(QtCore.QRect(570, 120, 51, 21))
        self.fanLevel5.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.fanLevel5.setObjectName("fanLevel5")
        self.targetTemp5 = QtGui.QLCDNumber(self.centralWidget)
        self.targetTemp5.setGeometry(QtCore.QRect(570, 80, 51, 21))
        self.targetTemp5.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.targetTemp5.setObjectName("targetTemp5")
        self.cost5 = QtGui.QLCDNumber(self.centralWidget)
        self.cost5.setGeometry(QtCore.QRect(570, 160, 51, 21))
        self.cost5.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.cost5.setObjectName("cost5")
        self.curTemp5 = QtGui.QLCDNumber(self.centralWidget)
        self.curTemp5.setGeometry(QtCore.QRect(570, 40, 51, 21))
        self.curTemp5.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.curTemp5.setObjectName("curTemp5")
        #self.modeLabel = QtGui.QLabel(self.centralWidget)
        #self.modeLabel.setGeometry(QtCore.QRect(80, 260, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        #self.modeLabel.setFont(font)
        #self.modeLabel.setText("")
        #self.modeLabel.setObjectName("modeLabel")
        self.bill1 = QtGui.QPushButton(self.centralWidget)
        self.bill1.setGeometry(QtCore.QRect(100, 220, 71, 31))
        self.bill1.setObjectName("bill1")
        self.detail1 = QtGui.QPushButton(self.centralWidget)
        self.detail1.setGeometry(QtCore.QRect(100, 190, 71, 31))
        self.detail1.setObjectName("detail1")
        self.detail2 = QtGui.QPushButton(self.centralWidget)
        self.detail2.setGeometry(QtCore.QRect(200, 190, 71, 31))
        self.detail2.setObjectName("detail2")
        self.bill2 = QtGui.QPushButton(self.centralWidget)
        self.bill2.setGeometry(QtCore.QRect(200, 220, 71, 31))
        self.bill2.setObjectName("bill2")
        self.detail3 = QtGui.QPushButton(self.centralWidget)
        self.detail3.setGeometry(QtCore.QRect(320, 190, 71, 31))
        self.detail3.setObjectName("detail3")
        self.bill3 = QtGui.QPushButton(self.centralWidget)
        self.bill3.setGeometry(QtCore.QRect(320, 220, 71, 31))
        self.bill3.setObjectName("bill3")
        self.detail4 = QtGui.QPushButton(self.centralWidget)
        self.detail4.setGeometry(QtCore.QRect(440, 190, 71, 31))
        self.detail4.setObjectName("detail4")
        self.bill4 = QtGui.QPushButton(self.centralWidget)
        self.bill4.setGeometry(QtCore.QRect(440, 220, 71, 31))
        self.bill4.setObjectName("bill4")
        self.detail5 = QtGui.QPushButton(self.centralWidget)
        self.detail5.setGeometry(QtCore.QRect(560, 190, 71, 31))
        self.detail5.setObjectName("detail5")
        self.bill5 = QtGui.QPushButton(self.centralWidget)
        self.bill5.setGeometry(QtCore.QRect(560, 220, 71, 31))
        self.bill5.setObjectName("bill5")
        self.dayReport = QtGui.QPushButton(self.centralWidget)
        self.dayReport.setGeometry(QtCore.QRect(310, 260, 91, 32))
        self.dayReport.setObjectName("dayReport")
        self.weekReport = QtGui.QPushButton(self.centralWidget)
        self.weekReport.setGeometry(QtCore.QRect(420, 260, 91, 32))
        self.weekReport.setObjectName("weekReport")
        self.monthReport = QtGui.QPushButton(self.centralWidget)
        self.monthReport.setGeometry(QtCore.QRect(530, 260, 91, 32))
        self.monthReport.setObjectName("monthReport")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar()
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 658, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "房间1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "房间2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "房间3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "房间4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "房间5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "当前温度", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "目标温度", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "当前风速", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "金额", None, QtGui.QApplication.UnicodeUTF8))
        #self.label_10.setText(QtGui.QApplication.translate("MainWindow", "模式", None, QtGui.QApplication.UnicodeUTF8))
        self.bill1.setText(QtGui.QApplication.translate("MainWindow", "账单", None, QtGui.QApplication.UnicodeUTF8))
        self.detail1.setText(QtGui.QApplication.translate("MainWindow", "详单", None, QtGui.QApplication.UnicodeUTF8))
        self.detail2.setText(QtGui.QApplication.translate("MainWindow", "详单", None, QtGui.QApplication.UnicodeUTF8))
        self.bill2.setText(QtGui.QApplication.translate("MainWindow", "账单", None, QtGui.QApplication.UnicodeUTF8))
        self.detail3.setText(QtGui.QApplication.translate("MainWindow", "详单", None, QtGui.QApplication.UnicodeUTF8))
        self.bill3.setText(QtGui.QApplication.translate("MainWindow", "账单", None, QtGui.QApplication.UnicodeUTF8))
        self.detail4.setText(QtGui.QApplication.translate("MainWindow", "详单", None, QtGui.QApplication.UnicodeUTF8))
        self.bill4.setText(QtGui.QApplication.translate("MainWindow", "账单", None, QtGui.QApplication.UnicodeUTF8))
        self.detail5.setText(QtGui.QApplication.translate("MainWindow", "详单", None, QtGui.QApplication.UnicodeUTF8))
        self.bill5.setText(QtGui.QApplication.translate("MainWindow", "账单", None, QtGui.QApplication.UnicodeUTF8))
        self.dayReport.setText(QtGui.QApplication.translate("MainWindow", "日报表", None, QtGui.QApplication.UnicodeUTF8))
        self.weekReport.setText(QtGui.QApplication.translate("MainWindow", "周报表", None, QtGui.QApplication.UnicodeUTF8))
        self.monthReport.setText(QtGui.QApplication.translate("MainWindow", "月报表", None, QtGui.QApplication.UnicodeUTF8))


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._db = MySqlDB()
        self.ui.detail1.clicked.connect(self.get_detail1)
        self.ui.detail2.clicked.connect(self.get_detail2)
        self.ui.detail3.clicked.connect(self.get_detail3)
        self.ui.detail4.clicked.connect(self.get_detail4)
        self.ui.detail5.clicked.connect(self.get_detail5)

        self.ui.bill1.clicked.connect(self.get_bill1)
        self.ui.bill2.clicked.connect(self.get_bill2)
        self.ui.bill3.clicked.connect(self.get_bill3)
        self.ui.bill4.clicked.connect(self.get_bill4)
        self.ui.bill5.clicked.connect(self.get_bill5)

        self.ui.dayReport.clicked.connect(self.get_day_report)
        self.ui.weekReport.clicked.connect(self.get_week_report)
        self.ui.monthReport.clicked.connect(self.get_month_report)

        #self.ui.modeLabel.setText()
        threading.Thread(target=self.update_thread).start()


    def update_thread(self):
        while True:
            item = self._db.query_client(0)
            if item['state'] == 'on':
                self.ui.curTemp1.display(item['curTemp'])
                self.ui.targetTemp1.display(item['targetTemp'])
                self.ui.fanLevel1.display(item['fanLevel'])
                self.ui.cost1.display(item['cost'])

            item = self._db.query_client(1)
            if item['state'] == 'on':
                self.ui.curTemp2.display(item['curTemp'])
                self.ui.targetTemp2.display(item['targetTemp'])
                self.ui.fanLevel2.display(item['fanLevel'])
                self.ui.cost2.display(item['cost'])

            item = self._db.query_client(2)
            if item['state'] == 'on':
                self.ui.curTemp3.display(item['curTemp'])
                self.ui.targetTemp3.display(item['targetTemp'])
                self.ui.fanLevel3.display(item['fanLevel'])
                self.ui.cost3.display(item['cost'])

            item = self._db.query_client(3)
            if item['state'] == 'on':
                self.ui.curTemp4.display(item['curTemp'])
                self.ui.targetTemp4.display(item['targetTemp'])
                self.ui.fanLevel4.display(item['fanLevel'])
                self.ui.cost4.display(item['cost'])

            item = self._db.query_client(4)
            if item['state'] == 'on':
                self.ui.curTemp5.display(item['curTemp'])
                self.ui.targetTemp5.display(item['targetTemp'])
                self.ui.fanLevel5.display(item['fanLevel'])
                self.ui.cost5.display(item['cost'])

            time.sleep(2)

    def get_detail1(self):
        cd = ControllerDialog(self)
        cd.setDetailTable(self._db, 0)
        cd.exec_()

    def get_detail2(self):
        cd = ControllerDialog(self)
        cd.setDetailTable(self._db, 1)
        cd.exec_()

    def get_detail3(self):
        cd = ControllerDialog(self)
        cd.setDetailTable(self._db, 2)
        cd.exec_()

    def get_detail4(self):
        cd = ControllerDialog(self)
        cd.setDetailTable(self._db, 3)
        cd.exec_()

    def get_detail5(self):
        cd = ControllerDialog(self)
        cd.setDetailTable(self._db, 4)
        cd.exec_()

    def get_bill1(self):
        cd = ControllerDialog(self)
        cd.setBillTable(self._db, 0)
        cd.exec_()

    def get_bill2(self):
        cd = ControllerDialog(self)
        cd.setBillTable(self._db, 1)
        cd.exec_()

    def get_bill3(self):
        cd = ControllerDialog(self)
        cd.setBillTable(self._db, 2)
        cd.exec_()

    def get_bill4(self):
        cd = ControllerDialog(self)
        cd.setBillTable(self._db, 3)
        cd.exec_()

    def get_bill5(self):
        cd = ControllerDialog(self)
        cd.setBillTable(self._db, 4)
        cd.exec_()

    def get_day_report(self):
        pass

    def get_week_report(self):
        pass

    def get_month_report(self):
        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
