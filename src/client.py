"""
    Author: 1806exe
    Email: 1806exe@gmail.com
    GitHub: https://www.github.com/1806exe


    ** Description **
     This is very simple TCP python client,
"""

import socket
import sys


class Client:

    def __init__(self):
        self.tcp_ip = '127.0.0.1'
        self.tcp_port = 8090
        self.buffer_size = 1024
        self.message_to_server = 'Hello, Server!'

    def send_to_client(self):

        try:
            # create IPv4 TCP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except socket.error as e:
            print 'Error occurred during socket creation', e
            sys.exit()
        sock.connect((self.tcp_ip, self.tcp_port))

        # after establish connection we try to send message to server
        try:
            sock.send(self.message_to_server)

        except socket.error as e:
            print 'Error occur try to send message to the server', e
            sys.exit()

        # receive message from server
        data = sock.recv(self.buffer_size)
        print 'Server: ', data


if __name__ == '__main__':
    client = Client()
    client.send_to_client()
