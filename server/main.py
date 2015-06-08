#coding=utf-8
#__author__ = 'Garfield'
#启动文件，并没有什么乱用

import jsonrpc_handle

if __name__ == '__main__':
    jsonrpc_handle.server.init()
    jsonrpc_handle.main()
    jsonrpc_handle.server.run()
