#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import os
import sys

HOST = '0.0.0.0'
PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    conn, addr = s.accept()
    print('connected by ' + str(addr))

    indata1 = conn.recv(1024)
    if indata1.decode()=='listapps':
     	print("xmutil listapps")
     	indata2 = conn.recv(1024)
     	sting = 'echo '+indata2.decode()
     	print(sting)
    if indata1.decode()=='quit':
     	sys.exit()
    print('recv: ' + indata1.decode())
    #os.system("touch 123.txt")
    outdata = 'echo ' + indata1.decode()
    conn.send(outdata.encode())
    conn.close()
