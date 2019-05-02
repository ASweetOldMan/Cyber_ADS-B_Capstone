#! /usr/bin/env python3

#I have this in 'C:\Program Files (x86)\Python37-32\Lib\site-packages\scapy'
#send command is: send(IP(dst="172.30.125.172")/ICMP()/"Hello") 
# Just enter whatever data you want to send in quotes where hello is and change IPs as needed
 
from scapy.all import send, IP, ICMP, sniff


while(1):
    print("sending")
    send(IP(dst="172.30.90.56")/ICMP()/"8D40621D58C382D690C8AC2863A7") 
    
    print('waiting')
    pkt = sniff(count=1, filter="icmp and host 172.30.90.56") #sender IP
    sniff(count=1, filter="icmp and host 172.30.90.56") #clear
    
    adsb_A = (pkt[0][ICMP].load).decode('UTF-8')
    print(adsb_A)
    
    
    