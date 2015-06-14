# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Sat Jun 13 19:20:59 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from datetime import datetime

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(680, 200)
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 480, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))


class ControllerDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ControllerDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def setDetailTable(self, db, id):
        res = db.query_list(id)
        row = len(res)
        self.ui.tableWidget.setGeometry(QtCore.QRect(20, 10, 660, 180))
        self.ui.tableWidget.setColumnCount(8)
        self.ui.tableWidget.setRowCount(row)
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 150)
        self.ui.tableWidget.setColumnWidth(3, 50)
        self.ui.tableWidget.setColumnWidth(4, 40)
        self.ui.tableWidget.setColumnWidth(5, 70)
        self.ui.tableWidget.setColumnWidth(6, 70)
        self.ui.tableWidget.setColumnWidth(7, 60)
        labels = ['Room', 'begin time', 'end time', 'mode', 'fan', \
            'begin temp', 'end temp', 'cost']
        self.ui.tableWidget.setHorizontalHeaderLabels(labels)

        for i in range(row):
            item = res[i]
            begin_time = datetime.strftime(item[1], '%Y-%m-%d %H:%M:%S')
            end_time = datetime.strftime(item[2], '%Y-%m-%d %H:%M:%S')
            self.ui.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(str(item[0])))
            self.ui.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(begin_time))
            self.ui.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem(end_time))
            self.ui.tableWidget.setItem(i, 3, QtGui.QTableWidgetItem(item[3]))
            self.ui.tableWidget.setItem(i, 4, QtGui.QTableWidgetItem(str(item[4])))
            self.ui.tableWidget.setItem(i, 5, QtGui.QTableWidgetItem(str(item[5])))
            self.ui.tableWidget.setItem(i, 6, QtGui.QTableWidgetItem(str(item[6])))
            self.ui.tableWidget.setItem(i, 7, QtGui.QTableWidgetItem(str(item[7])))


    def setBillTable(self, db, id):
        sum = db.query_list_sum(id)
        check_in = db.query_user(id)['check_in']
        check_out = datetime.now()
        check_in_time = datetime.strftime(check_in, '%Y-%m-%d %H:%M:%S')
        check_out_time = datetime.strftime(check_out, '%Y-%m-%d %H:%M:%S')
        self.ui.tableWidget.setGeometry(QtCore.QRect(80, 10, 560, 180))
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setColumnWidth(0, 40)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 150)
        self.ui.tableWidget.setColumnWidth(3, 60)
        labels = ['Room', 'check in', 'check out', 'sum']
        self.ui.tableWidget.setHorizontalHeaderLabels(labels)

        self.ui.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem(str(id)))
        self.ui.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem(check_in_time))
        self.ui.tableWidget.setItem(0, 2, QtGui.QTableWidgetItem(check_out_time))
        self.ui.tableWidget.setItem(0, 3, QtGui.QTableWidgetItem(str(sum)))

    def setReport(self, db, i):
        rooms = db.query_user_room()
        self.ui.tableWidget.setGeometry(QtCore.QRect(140, 10, 400, 180))
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(len(rooms))
        self.ui.tableWidget.setColumnWidth(0, 60)
        self.ui.tableWidget.setColumnWidth(1, 150)

        self.ui.tableWidget.setHorizontalHeaderLabels(['Room', 'total cost'])

        j = 0
        for item in rooms:
            id = item[0]
            res = db.query_list_report(id, i)
            self.ui.tableWidget.setItem(j, 0, QtGui.QTableWidgetItem(str(id)))
            self.ui.tableWidget.setItem(j, 1, QtGui.QTableWidgetItem(str(res)))
            j += 1
