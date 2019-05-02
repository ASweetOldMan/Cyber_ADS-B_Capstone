#! /usr/bin/env python3

#I have this in 'C:\Program Files (x86)\Python37-32\Lib\site-packages\scapy'
#send command is: send(IP(dst="172.30.125.172")/ICMP()/"Hello") 
# Just enter whatever data you want to send in quotes where hello is and change IPs as needed
 
from scapy.all import ICMP, sniff
from geographiclib.geodesic import Geodesic
import geopy.distance
import pyModeS as pms
import math
import adsb_out.ADSB_Encoder as out
import time

print('waiting super patiently')

while(1):
	pkt = sniff(count=1, filter="icmp and host 172.30.90.56") #sender IP
	#print(pkt.show)
	#print((pkt[0][ICMP].load).decode('UTF-8'))  #gets you just the message sent
	adsb_A = (pkt[0][ICMP].load).decode('UTF-8')
	print(adsb_A)
	#adsb_Ab= bin(int(adsb_A, 16))[2:]
	#print(adsb_A)
	#print(adsb_Ab)
	
	print("ICAO:        " + str(pms.adsb.icao(adsb_A)))
	print("Typecode:    " + str(pms.adsb.typecode(adsb_A)))
	print("BDS Reg.:    " + str(pms.bds.infer(adsb_A)))
	
	sniff(count=1, filter="icmp and host 172.30.90.56")
	
	
	

# Just change the print to a var like: 'var = pkt[0][ICMP].load' and you should be able to use that data however you need
