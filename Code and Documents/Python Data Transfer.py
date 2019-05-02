import socket
import sys
from _thread import *
import threading
import netifaces as net
from termcolor import cprint, colored
import atexit

host = str(net.ifaddresses('en0')[net.AF_INET][0]['addr'])
port = 5555

print("Server:  ", end="")
cprint(host + ":" + str(port), "magenta")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))
    
s.listen(5)
cprint("Waiting for a connection", "green")

def threaded_client(conn):
    print("Connected")
    conn.send(str.encode("Welcome, Type your info\n"))
    
    print("Assigning dataLat and dataLon")
    dataLat = 34.616921
    
    while True:
        print("Sending")
        conn.send(str.encode(str(dataLat)))
        
        print("Receiving")
        dataLat = conn.recv(512)
        
        ("Received")
        print(dataLat)
        
        if not dataLat:
            break
        conn.sendall(str.encode(str(dataLat)))
    conn.close()
    
while True:    
    conn, addr = s.accept()
    print('connected to: ' + addr[0] + ':' + str(addr[1]))
    
    start_new_thread(threaded_client, (conn, ))
