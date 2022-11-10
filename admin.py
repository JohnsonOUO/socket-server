#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import sys

HOST = '0.0.0.0'
PORT = 7000
#n = len(sys.argv)-1
#if n>2:
#  print("Input must be two!")
#  sys.exit()
#if n==0:
#  print("please input parameters!")
#  sys.exit()
#print("sys.argv",sys.argv)
#print(n)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    cmd = input(">>>")
    print("my cmd : ",cmd)
    s.send(cmd.encode())

#outdata1 = sys.argv[1]
#outdata2 = sys.argv[2]
#print('send: ' + outdata1)
#s.send(outdata1.encode())
#print('send: ' + outdata2)
#s.send(outdata2.encode())

    #indata = s.recv(1024)
    #print('recv: ' + indata.decode())
s.close()
