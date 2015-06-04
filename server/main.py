#coding=utf-8
#__author__ = 'Garfield'
#启动文件，并没有什么乱用

from server_handle import ServerHandle

if __name__ == '__main__':
    server = ServerHandle()
    server.run()
