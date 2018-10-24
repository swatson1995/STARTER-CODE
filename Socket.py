# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 04:51:21 2018

@author: Lab1
"""

import socket 

t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = '10.1.1.2'
Port = 1067
address = (IP,Port)

InputBuffer= 2018880

t.bind(address)
t.listen(1)

client, addr = t.accept()
print ("bollocks")
while True:
    data = client.recv(512)
    print (data) 
    print ("starting to process data")
    if( data=="Hello server"):
        client.send("Hello Bitch")
        
    elif(data=="discoennected"):
        client.send("good bye")
    else:
        client.send("Invalid data")
        

        