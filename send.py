#!/usr/bin/python2

import socket
rec_ip="127.0.0.1"

rec_port=4444 #0 -1024 --you can check free udp port netstat -nulp

# creating Socket
#       ip type   v4  ,            UDP

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# sendig data to target

s.sendto("hello",(rec_ip,rec_port))
