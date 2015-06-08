#coding=utf-8
#__author__ = 'Garfield'
#JsonRpc服务端，使用cyclone非阻塞式处理客户端的远端调用请求

import sys
import types

import cyclone.httpclient
import cyclone.jsonrpc
import cyclone.xmlrpc
import cyclone.escape
from cyclone.web import HTTPError, RequestHandler

from twisted.internet import defer, reactor
from twisted.python import log, failure

from server_handle import ServerHandle
from database import MySqlDB

# room = [{ "ison": True, "fanlevel": 2, "temperature": 26, "cost": 10.2,
#    "isCentralOn": True, "maxTemperature": 30, "minTemperature": 20 }]

room = {}
server = ServerHandle()


class JsonrpcHandler(cyclone.jsonrpc.JsonrpcRequestHandler):
    def post(self, *args):
        self._auto_finish = False
        try:
            req = cyclone.escape.json_decode(self.request.body)
            jsonid = req["id"]
            method = req["method"]
            assert isinstance(method, types.StringTypes), \
                              "Invalid method type: %s" % type(method)
            params = req.get("params", [])
            assert isinstance(params, (types.ListType, types.TupleType)), \
                              "Invalid params type: %s" % type(params)
        except Exception, e:
            log.msg("Bad Request: %s" % str(e))
            raise HTTPError(400)

        function = getattr(self, "jsonrpc_%s" % method, None)
        if callable(function):
            args = list(args) + params
            d = defer.maybeDeferred(function, *args)
            d.addBoth(self._cbResult, jsonid)
        else:
            self._cbResult(AttributeError("method not found: %s" % method),
                           jsonid)

    def _cbResult(self, result, jsonid):
        if isinstance(result, failure.Failure):
            error = {'code': 0, 'message': str(result.value)}
            result = None
        else:
            data = {"jsonrpc": "2.0", "result": result, "id": jsonid}
        data = {"jsonrpc": "2.0", "result": result, "id": jsonid}
        print cyclone.escape.json_encode(data)
        self.finish(cyclone.escape.json_encode(data))

    def jsonrpc_echo(self, text):
        return text

    def jsonrpc_sort(self, items):
        return sorted(items)

    def jsonrpc_count(self, items):
        return len(items)

    def jsonrpc_get(self, i):
        if server.get_controller(i) is not None:
            return server.get(i)

    def jsonrpc_set(self, i, d):
        #根据房间请求在主控端进行处理，完成返回true，未完成返回
        room_id = i
        if server.get_controller(i) is not None:
            item =  (d['ison'], d['targetTemperature'], d['fanLevel'], i)
            temp = server.get(i)['temperature']
            server.get_controller(i).set_task(d['targetTemperature'], d['fanLevel'], temp)
            print "- [test-msg] <set>", item
            return server.set(item)
        else:
            return False

    @defer.inlineCallbacks
    def jsonrpc_geoip_lookup(self, address):
        result = yield cyclone.httpclient.fetch(
            "http://freegeoip.net/json/%s" % address.encode("utf-8"))
        defer.returnValue(result.body)

def main():
    log.startLogging(sys.stdout)
    application = cyclone.web.Application([
        (r"/jsonrpc", JsonrpcHandler),
    ])

    reactor.listenTCP(8888, application)
    reactor.run()

if __name__ == "__main__":
    main()
