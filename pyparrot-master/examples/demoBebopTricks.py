"""
Demos the tricks on the bebop. Make sure you have enough room to perform them!

Author: Amy McGovern
"""

from pyparrot.Bebop import Bebop
from geographiclib.geodesic import Geodesic
import geopy.distance

bebop = Bebop()

print("connecting")
success = bebop.connect(10)
print(success)

print("sleeping")
#bebop.smart_sleep(1)

bebop.ask_for_state_update()

bebop.set_max_altitude(5)
bebop.set_max_distance(10)
bebop.enable_geofence(1)


#GPS Coordinates calculator
coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

print(geopy.distance.vincenty(coords_1, coords_2).km)

Geodesic.WGS84.Inverse(-112.45003066666953, 34.61611566666679, -112.45009966666666, 34.616099166666665) #{'lat1': -41.32, 'a12': 179.6197069334283, 's12': 19959679.26735382, 'lat2': 40.96, 'azi2': 18.825195123248392, 'azi1': 161.06766998615882, 'lon1': 174.81, 'lon2': -5.5}

print("GpsLocationChanged_longitude: " + str(bebop.sensors.sensors_dict["GpsLocationChanged_longitude"]))
print("GpsLocationChanged_latitude: " + str(bebop.sensors.sensors_dict["GpsLocationChanged_latitude"]))
print("GpsLocationChanged_altitude " + str(bebop.sensors.sensors_dict["GpsLocationChanged_altitude"]))

print("PositionChanged_longitude: " + str(bebop.sensors.sensors_dict["PositionChanged_longitude"]))
print("PositionChanged_latitude: " + str(bebop.sensors.sensors_dict["PositionChanged_latitude"]))
print("PositionChanged_altitude: " + str(bebop.sensors.sensors_dict["PositionChanged_altitude"]))

print("HomeChanged_longitude: " + str(bebop.sensors.sensors_dict["HomeChanged_longitude"]))
print("HomeChanged_latitude: " + str(bebop.sensors.sensors_dict["HomeChanged_latitude"]))
print("HomeChanged_altitude: " + str(bebop.sensors.sensors_dict["HomeChanged_altitude"]))


#bebop.smart_sleep(5)


bebop.safe_takeoff(10)
#bebop.smart_sleep(3)

bebop.move_relative(0, 0, -1.5, 0)  #move_relative(self, dx, dy, dz, dradians)
print("First Move Done")
#
#bebop.smart_sleep(1)
#
print("flip left")
print("flying state is %s" % bebop.sensors.flying_state)
success = bebop.flip(direction="left")
print("mambo flip result %s" % success)
bebop.smart_sleep(2)


#bebop.move_relative(0, 0, 0, 6.28)
#print("Second Move Done")

#print("flip right")
#print("flying state is %s" % bebop.sensors.flying_state)
#success = bebop.flip(direction="right")
#print("mambo flip result %s" % success)
#bebop.smart_sleep(5)
#
#print("flip front")
#print("flying state is %s" % bebop.sensors.flying_state)
#success = bebop.flip(direction="front")
#print("mambo flip result %s" % success)
#bebop.smart_sleep(5)
#
#print("flip back")
#print("flying state is %s" % bebop.sensors.flying_state)
#success = bebop.flip(direction="back")
#print("mambo flip result %s" % success)
#bebop.smart_sleep(5)

bebop.smart_sleep(5)
bebop.safe_land(10)

print("DONE - disconnecting")
bebop.disconnect()