# coding:utf-8
import socket
import SimpleHTTPServer


def make_socks(sock_num):
    socks = []
    for i in range(sock_num):
        tmp_sock = socket.socket()
        tmp_sock.connect(("127.0.0.1", 1234))
        socks.append(tmp_sock)

    return socks


if __name__ == "__main__":
    make_socks(5)