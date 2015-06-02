#coding=utf-8
#__author__ = 'Garfield'
#启动文件，并没有什么乱用

from controller import Controller
import sys
from PySide.QtCore import *
from PySide.QtGui import *
# Create a Qt application


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Create a Label and show it
    label = QLabel("Hello World")
    label.show()
    # Enter Qt application main loop

    sys.exit(app.exec_())
    #controller = Controller(0)
    #controller.run()
