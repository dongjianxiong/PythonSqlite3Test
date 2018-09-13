# coding:utf-8   
# server.py                                                               
import socket
import MySQLdb
from SocketServer import ThreadingTCPServer, StreamRequestHandler
import traceback
import LNEmployeeDb

class MyStreamRequestHandlerr(StreamRequestHandler):
    """
    #StreamRequestHandler，并重写handle方法
    #（StreamRequestHandler继承自BaseRequestHandler）
    """
    def handle(self):
        while True:
            #客户端主动断开连接时，self.rfile.readline()会抛出异常
            try:
                #self.rfile类型是socket._fileobject,读写模式是"rb",方法有
                #read,readline,readlines,write(data),writelines(list),close,flush
                data = self.rfile.readline().strip()
                # if data == '\'\'':

                # print data
                print("receive from (%r):%r" % (self.client_address, data))
                # data = self.request.recev(1024).strip

                #self.client_address是客户端的连接(host, port)的元组)

                #self.wfile类型是socket._fileobject,读写模式是"wb"
                self.wfile.write(data.upper())
            except:
                traceback.print_exc()
                break

if __name__ == "__main__":
    #telnet 127.0.0.1 9999
    host = "127.0.0.1"       #主机名，可以是ip,像localhost的主机名,或""
    port = 9999     #端口
    addr = (host, port)

    LNEmployeeDb.sqliteHandler()

    #ThreadingTCPServer从ThreadingMixIn和TCPServer继承
    #class ThreadingTCPServer(ThreadingMixIn, TCPServer): pass
    server = ThreadingTCPServer(addr, MyStreamRequestHandlerr)

    #启动服务监听
    server.serve_forever()

# sock_server = socket.socket()
# sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ip_port = ("127.0.0.1",1234)
# sock_server.bind(ip_port)
# sock_server.listen(3)
# print("server start ...")
# while True:
#     tmp = sock_server.accept()
#     print(tmp,"\n\n")