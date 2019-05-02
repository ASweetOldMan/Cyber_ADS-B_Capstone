import time
from pyparrot.networking.wifiConnection import WifiConnection
from pyparrot.utils.colorPrint import color_print
from pyparrot.commandsandsensors.DroneCommandParser import DroneCommandParser
from pyparrot.commandsandsensors.DroneSensorParser import DroneSensorParser
from datetime import datetime

from pyparrot.Bebop import Bebop
from geographiclib.geodesic import Geodesic
import geopy.distance
import pyModeS as pms

import math


def collision_avoidance(self, personalSpace = 5.0, pollRate = 1.0):
    """
    Begin Collision Avoidance Routine
    
    :param personalSpace:
    :return:
    """
    currentTime = time.time()
    lastTime = 0
    
    safe, caution, danger = 0, 1, 2
    
    while(true):
        lastTime = currentTime
        
        currentLat = self.sensors_dict("GpsLocationChanged_lat")
        currentLon = self.sensors_dict("GpsLocationChanged_lon")
        currentAlt = self.sensors_dict("GpsLocationChanged_alt")
        
        currentCoords = (currentLat, currentLon)
        
        threatLat = currentLat
        threatLon = currentLon
        threatAlt = currentAlt
        
        threatCoords = (threatLat, currentLon)
        
        threatDistance = geopy.distance.distance(, Drone_1b_Coords).meters
        deltaAlt = abs(currentAlt - threatAlt)
        threatSeparation = math.hypot(threatDistance, deltaAlt)
        
        if(threatSeparation <= personalSpace):
            print("Collision Evasion Activated")
            self.safe_land(10)
            return
        
        currentTime = time.time()
        timeUntilNextFrame = pollRate - (currentTime - lastTime)
        self.smart_sleep(timeUntilNextFrame)
    
    