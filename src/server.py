
"""
    Author: 1806exe
    Email: 1806exe@gmail.com
    GitHub: https://www.github.com/1806exe


    ** Description **
     This is very simple TCP python server,
"""

import socket
import sys


class Server:

    def __init__(self):
        self.tcp_ip = '127.0.0.1'
        self.tcp_port = 8090
        self.buffer_size = 1024

    def server(self):
        # creating TCP IPv4 stream
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except socket.error as e:
            print 'Error during socket establishment: ', e
            sys.exit()
        sock.bind((self.tcp_ip, self.tcp_port))

        # listening to the connection (max 5)
        sock.listen(5)
        print 'Listening......'

        # waits for incoming connection
        connection, address = sock.accept()
        print 'Connected to: ', address

        # accept data from client, limit 1024KB
        data = connection.recv(self.buffer_size)
        print 'Client: ', data

        # respond to the message
        connection.sendall('Thanks for connecting....')

        # close the connection
        connection.close()

        # keep the server alive for more connection
        while True:
            # establish the connection
            connection, address = sock.accept()
            print 'Client connected', address

            data = connection.recv(self.buffer_size)
            print 'Client: ', data

            # echo the message from client
            connection.sendall('Thanks for connecting')


if __name__ == '__main__':
    server = Server()
    server.server()
