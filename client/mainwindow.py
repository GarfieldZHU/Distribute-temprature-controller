# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Jun  2 16:12:17 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PySide import QtCore, QtGui

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
        self.targetTemp = QtGui.QLCDNumber(self.frame)
        self.targetTemp.setGeometry(QtCore.QRect(30, 110, 151, 31))
        self.targetTemp.setObjectName("targetTemp")
        self.stateLabel = QtGui.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(30, 10, 141, 31))
        self.stateLabel.setText("")
        self.stateLabel.setObjectName("stateLabel")
        self.totalCost = QtGui.QLCDNumber(self.frame)
        self.totalCost.setGeometry(QtCore.QRect(30, 200, 151, 31))
        self.totalCost.setObjectName("totalCost")
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
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
