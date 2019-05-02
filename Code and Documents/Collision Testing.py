from pyparrot.Bebop import Bebop
#from pyparrot.DroneVisionGUI import DroneVisionGUI
#from pyparrot.networking.wifiConnection import WifiConnection
#from pyparrot.utils.colorPrint import color_print
#from pyparrot.commandsandsensors.DroneCommandParser import DroneCommandParser
#from pyparrot.commandsandsensors.DroneSensorParser import DroneSensorParser

from termcolor import cprint, colored
import multiprocessing as mp
from _thread import *
import netifaces as net
import socket, logging, ctypes, sys, os
import cv2
import math, time
from datetime import datetime

from geographiclib.geodesic import Geodesic
import geopy.distance

#import pyModeS as pms


def flight_plan(keepGoing):
    #Video Config
    bebop.set_video_framerate("30_FPS")
    bebop.set_video_resolutions("rec1080_stream480")
    bebop.set_video_recording("quality")

    print("in flight plan")
    print("sleeping")
    bebop.smart_sleep(5)
    
    bebop.safe_land(10)
    
    keepGoing.value = 0
    
    
def threaded_client(conn):
    conn.send(str.encode("Welcome, Type your info\n"))
    
    while True:
        data = conn.recv(2048)
        reply = "Server Output: " + data.decode("utf-8")
        if not data:
            break
        conn.sendall(str.encode(reply))
    
    conn.close()


def collision_avoidance(keepGoing, personalSpace = 5.0, interval = 1.0):
    """
    Begin Collision Avoidance Routine
    
    :param keepGoing:
    :param personalSpace:
    :param interval:
    :return:
    """
    print("collision avoidance started")
    
    host = str(net.ifaddresses('en0')[net.AF_INET][0]['addr'])
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((host, port))
    except socket.error as e:
        print(str(e))
        
    s.listen(5)

    print("Waiting for a connection")
    
    conn, addr = s.accept()
    print('connected to: ' + addr[0] + ':' + str(addr[1]))
    
    servProc = mp.Process(threaded_client, (conn, ))
    servProc.start()

    currentTime = time.time()
    lastTime = 0

    collisionState = 0
    safe, caution, danger = 0, 1, 2

    while(1):
        lastTime = currentTime

        currentLat = bebop.sensors.sensors_dict["GpsLocationChanged_latitude"]
        currentLon = bebop.sensors.sensors_dict["GpsLocationChanged_longitude"]
        currentAlt = bebop.sensors.sensors_dict["GpsLocationChanged_altitude"]

        if(currentLat == 500.0):
            cprint("GPS Signal Inadequate", "red")
            flightProc.terminate()
            keepGoing.value = 0
            return

        if(currentLon == 500.0):
            cprint("GPS Signal Inadequate", "red")
            flightProc.terminate()
            keepGoing.value = 0
            return

        if(currentAlt == 500.0):
            cprint("GPS Signal Inadequate", "red")
            flightProc.terminate()
            keepGoing.value = 0
            return

        currentCoords = (currentLat, currentLon)

        threatLat = currentLat
        threatLon = currentLon
        threatAlt = currentAlt

        threatCoords = (threatLat, currentLon)

        threatDistance = geopy.distance.distance(currentCoords, threatCoords).feet
        deltaAlt = abs(currentAlt - threatAlt)
        threatSeparation = math.hypot(threatDistance, deltaAlt)

        if(threatSeparation <= personalSpace):
            cprint("Collision Evasion Activated", "red")
            flightProc.terminate()
            keepGoing.value = 0
            return

        currentTime = time.time()
        timeUntilNextFrame = pollRate - (currentTime - lastTime)
        drone.smart_sleep(timeUntilNextFrame)


class UserVision:
    def __init__(self, vision):
        self.index = 0
        self.vision = vision

    def save_pictures(self, args):
        #print("saving picture")
        img = self.vision.get_latest_valid_picture()

        if (img is not None):
            filename = "test_image_%06d.png" % self.index
            cv2.imwrite(filename, img)
            self.index +=1


if __name__ == "__main__":
    
    keepGoing = mp.Value('i', 1)
    
    host = str(net.ifaddresses('en0')[net.AF_INET][0]['addr'])
    port = 5555

    print("Server:  " + host + ":" + str(port))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((host, port))
    except socket.error as e:
        print(str(e))
        
    s.listen(5)
    print("Waiting for a connection")

    # make my bebop object
    bebop = Bebop()

    # connect to the bebop
    success = bebop.connect(5)
    
    if(success):
        bebop.smart_sleep(3)
        bebop.ask_for_state_update()

        flightProc = mp.Process(target = flight_plan, args = (keepGoing, ))
        flightProc.start()

        collisionProc = mp.Process(target = collision_avoidance, args = (keepGoing, ))
        collisionProc.start()


    while(keepGoing.value == 1):
        
        continue

    bebop.disconnect()

    sys.exit("Collision Warning")
