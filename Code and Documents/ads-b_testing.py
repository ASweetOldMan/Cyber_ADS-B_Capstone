import pyModeS as pms
import math
import adsb_out.ADSB_Encoder as out
import time
from termcolor import cprint, colored


def adsbPrint(adsb, textColor = "white", attrs=[]):
	cprint("ADS-B Hex:   " + str(adsb), textColor)
	cprint("ADS-B Binary:   " + str(bin(int(adsb, 16))[2:]), textColor)
	cprint("")
	cprint("ICAO:   " + str(pms.adsb.icao(adsb)) + "          " + 
		   "Typecode:   " + str(pms.adsb.typecode(adsb)) + "          " + 
		   "BDS Reg.:   " + str(pms.bds.infer(adsb)) + "          " + 
		   "Altitude:   " + str(pms.decoder.bds.bds05.altitude(adsb)) + "ft.", textColor)
	cprint("")


def adsbEncode(ca, icao, tc, ss, nicsb, alt, time, lat, lon, surface):
	ca = 5
	tc = 11
	ss = 0
	nicsb = 0
	time = 0
	icao = int(icao, 16)
	surface = False
	
	trash = []
	
	(df17_even, df17_odd) = df17_pos_rep_encode(ca, icao, tc, ss, nicsb, alt, time, lat, lon, surface)

	print(''.join(format(x, '02x').upper() for x in df17_even))
	print(''.join(format(x, '02x').upper() for x in df17_odd))
	
	even = (''.join(format(x, '02x').upper() for x in df17_even))
	odd = (''.join(format(x, '02x').upper() for x in df17_odd))
	
	return (df17_even, df17_odd)


adsb_A = "8D40621D58C382D690C8AC2863A7"
adsb_Ax = adsb_A
adsb_Ab = bin(int(adsb_A, 16))[2:]
adsb_A_time = 0		#time.time()

time.sleep(1)

adsb_B = "8D40621D58C386435CC412692AD6"
adsb_Bx = adsb_B
adsb_Bb = bin(int(adsb_B, 16))[2:]
adsb_B_time = 0	#time.time()

ca = 5
tc = 11
ss = 0
nicsb = 0
time = 0
icao = int("40621D", 16)
surface = False

trash = []

alt = pms.decoder.bds.bds05.altitude(adsb_A)

lat, lon = pms.decoder.bds.bds05.airborne_position(adsb_A, adsb_B, 1, 0)
#print(lat, lon)
df17_even, trash = out.df17_pos_rep_encode(ca, icao, tc, ss, nicsb, alt, time, lat, lon, surface)

lat, lon = pms.decoder.bds.bds05.airborne_position(adsb_A, adsb_B, 0, 0)
#print(lat, lon)
trash, df17_odd = out.df17_pos_rep_encode(ca, icao, tc, ss, nicsb, alt, time, lat, lon, surface)

even = (''.join(format(x, '02x').upper() for x in df17_even))
odd = (''.join(format(x, '02x').upper() for x in df17_odd))


cprint("Original Even Message: ", "magenta", attrs=["underline"])
adsbPrint(adsb_A, "magenta")
cprint("Encoded Even Message: ", "blue", attrs=["underline"])
adsbPrint(even, "blue")
cprint("Original Odd Message: ", "magenta", attrs=["underline"])
adsbPrint(adsb_B, "magenta")
cprint("Encoded Odd Message: ", "blue", attrs=["underline"])
adsbPrint(odd, "blue")

cprint(pms.decoder.bds.bds05.airborne_position(even, odd, 0, 0), "green")

#for i in range(10):
#	lat = float('%.5f'%(lat))
#	lon = float('%.5f'%(lon))
#	
#	lat = lat - (0.00001 * i)
##	cprint(lat, "cyan")
##	cprint(lon, "green")
#
#	alt = 38000
#
#	(df17_even, df17_odd) = out.df17_pos_rep_encode(ca, icao, tc, ss, nicsb, alt, 0, lat, lon, surface)
#	
#	even = (''.join(format(x, '02x').upper() for x in df17_even))
#	odd = (''.join(format(x, '02x').upper() for x in df17_odd))
#	
#	even1, odd1 = pms.decoder.bds.bds05.airborne_position(even, odd, 0, 0)
#	even2, odd2 = pms.decoder.bds.bds05.airborne_position(even, odd, 1, 0)
#	
##	cprint(even1, "yellow")
##	cprint(odd1, "cyan")
##	cprint(even2, "yellow")
##	cprint(odd2, "cyan")
#	
#	even = (even1 + even2)/2
#	odd = (odd1 + odd2)/2
#	
#	even = float('%.5f'%(even))
#	odd = float('%.5f'%(odd))
#	
#	cprint(even, "cyan")
#	cprint(odd, "cyan")
#	cprint("")
	
	
#	cprint(pms.decoder.bds.bds05.airborne_position(even, odd, 0, 0), "magenta")
#	cprint(pms.decoder.bds.bds05.airborne_position(even, odd, 1, 0), "cyan")



#lat = 52.2572
#lon = 3.91937
#lat = 52.26578
#lon = 3.93891

#lat = 34.61705
#lon = -112.453415
#lat = '%.5f'%(34.616954)
#lon = '%.5f'%(-112.453304)

#lat = float('%.5f'%(34.616921))
#lon = float('%.5f'%(-112.453415))
#lat = '%.5f'%(34.616954)
#lon = '%.5f'%(-112.453304)
#alt = 38000

#(df17_even, df17_odd) = out.df17_pos_rep_encode(ca, icao, tc, ss, nicsb, alt, 1, lat, lon, surface)

#even = (''.join(format(x, '02x').upper() for x in df17_even))
#odd = (''.join(format(x, '02x').upper() for x in df17_odd))
#
#print(even)
#print(odd)
#
#even_bin = bin(int(even, 16))[2:]
#odd_bin = bin(int(odd, 16))[2:]
#cprint("")

#cprint("Original Even Message: ", "magenta", attrs=["underline"])
#adsbPrint(adsb_A, "magenta")
#cprint("Encoded Even Message: ", "cyan", attrs=["underline"])
#adsbPrint(even, "cyan")
#cprint("Original Odd Message: ", "magenta", attrs=["underline"])
#adsbPrint(adsb_B, "magenta")
#cprint("Encoded Odd Message: ", "yellow", attrs=["underline"])
#adsbPrint(odd, "yellow")


#lat = float('%.5f'%(34.616921))
#lon = float('%.5f'%(-112.453415))
#lat = '%.5f'%(34.616954)
#lon = '%.5f'%(-112.453304)
#
#for i in range(1):
#	
#	lat = 34.61705 - (0.00001 * i)
#	print(lat)
#	lon = -112.453415
#	print(lon)
#
#	alt = 38000
#
#	(df17_even, df17_odd) = out.df17_pos_rep_encode(ca, icao, tc, ss, nicsb, alt, 0, lat, lon, surface)
#	
#	even = (''.join(format(x, '02x').upper() for x in df17_even))
#	odd = (''.join(format(x, '02x').upper() for x in df17_odd))
	
#	cprint(pms.decoder.bds.bds05.airborne_position(even, odd, 0, 0), "magenta")
#	cprint(pms.decoder.bds.bds05.airborne_position(even, odd, 1, 0), "cyan")