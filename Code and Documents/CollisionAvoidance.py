from pyparrot.Bebop import Bebop
from geographiclib.geodesic import Geodesic
import geopy.distance

bebop = Bebop()

print("connecting")
success = bebop.connect(10)
print(success)

print("sleeping")
bebop.smart_sleep(1)

bebop.ask_for_state_update()

bebop.set_max_altitude(5)
bebop.set_max_distance(10)
bebop.enable_geofence(1)

#print("HomeChanged_longitude: " + str(bebop.sensors.sensors_dict["HomeChanged_longitude"]))
#print("HomeChanged_latitude: " + str(bebop.sensors.sensors_dict["HomeChanged_latitude"]))
#print("HomeChanged_altitude: " + str(bebop.sensors.sensors_dict["HomeChanged_altitude"]) + "\n\n")

print("First State Update: ")

Drone_1a_Lat = bebop.sensors.sensors_dict["GpsLocationChanged_latitude"]
print("GpsLocationChanged_latitude:  " + str(bebop.sensors.sensors_dict["GpsLocationChanged_latitude"]))
Drone_1a_Lon = bebop.sensors.sensors_dict["GpsLocationChanged_longitude"]
print("GpsLocationChanged_longitude: " + str(bebop.sensors.sensors_dict["GpsLocationChanged_longitude"]))
Drone_1a_Alt = bebop.sensors.sensors_dict["GpsLocationChanged_altitude"]
print("GpsLocationChanged_altitude:  " + str(bebop.sensors.sensors_dict["GpsLocationChanged_altitude"]) + "\n")

bebop.smart_sleep(1)

bebop.ask_for_state_update()

Drone_1b_Lat = bebop.sensors.sensors_dict["GpsLocationChanged_latitude"]
print("GpsLocationChanged_latitude:  " + str(bebop.sensors.sensors_dict["GpsLocationChanged_latitude"]))
Drone_1b_Lon = bebop.sensors.sensors_dict["GpsLocationChanged_longitude"]
print("GpsLocationChanged_longitude: " + str(bebop.sensors.sensors_dict["GpsLocationChanged_longitude"]))
Drone_1b_Alt = bebop.sensors.sensors_dict["GpsLocationChanged_altitude"]
print("GpsLocationChanged_altitude:  " + str(bebop.sensors.sensors_dict["GpsLocationChanged_altitude"]) + "\n")


Drone_1a_Coords = (Drone_1a_Lat, Drone_1a_Lon)
Drone_1b_Coords = (Drone_1b_Lat, Drone_1b_Lon)

#Drone Simulation
#
#	Drone 1.1:
#	Approx. Heading:  70.22 Degrees
#	Approx. Distance: 35.49 Feet


print("Drone 1.1:\n")
print("Lat1:          " + str(Geodesic.WGS84.Inverse(Drone_1a_Lat, Drone_1a_Lon, Drone_1b_Lat, Drone_1b_Lon)['lat1']))
print("Lon1:          " + str(Geodesic.WGS84.Inverse(Drone_1a_Lat, Drone_1a_Lon, Drone_1b_Lat, Drone_1b_Lon)['lon1']))
print("Lat2:          " + str(Geodesic.WGS84.Inverse(Drone_1a_Lat, Drone_1a_Lon, Drone_1b_Lat, Drone_1b_Lon)['lat2']))
print("Lon2:          " + str(Geodesic.WGS84.Inverse(Drone_1a_Lat, Drone_1a_Lon, Drone_1b_Lat, Drone_1b_Lon)['lon2']))
print("a12:           " + str(Geodesic.WGS84.Inverse(Drone_1a_Lat, Drone_1a_Lon, Drone_1b_Lat, Drone_1b_Lon)['a12']))
print("s12:           " + str(Geodesic.WGS84.Inverse(Drone_1a_Lat, Drone_1a_Lon, Drone_1b_Lat, Drone_1b_Lon)['s12']))
print("Azi1:          " + str(Geodesic.WGS84.Inverse(Drone_1a_Lat, Drone_1a_Lon, Drone_1b_Lat, Drone_1b_Lon)['azi1']))
print("Azi2:          " + str(Geodesic.WGS84.Inverse(Drone_1a_Lat, Drone_1a_Lon, Drone_1b_Lat, Drone_1b_Lon)['azi2']))
print("Distance (ft): " + str((geopy.distance.distance(Drone_1a_Coords, Drone_1b_Coords).feet)) + "\n\n")


#bebopVision = DroneVisionGUI(bebop, is_bebop=True, user_args=(bebop, ))
#
#userVision = UserVision(bebopVision)
#bebopVision.set_user_callback_function(userVision.save_pictures, user_callback_args=None)
#bebopVision.open_video()
#
#print("turning on the video")
#bebop.start_video_stream()
#bebop.smart_sleep(5)
#
#
#bebop.safe_takeoff(10)
#bebop.smart_sleep(10)

#print("flip left")
#print("flying state is %s" % bebop.sensors.flying_state)
#success = bebop.flip(direction="left")
#print("mambo flip result %s" % success)
#bebop.smart_sleep(5)

#bebop.move_relative(0, 0, -1, -1)  #move_relative(self, dx, dy, dz, dradians)
#print("First Move Done")
#bebop.move_relative(0, 0, 0, 1)
#print("Second Move Done")

bebop.smart_sleep(5)
#bebop.safe_land(10)

print(bebop.sensors.battery)

print("DONE - disconnecting")
bebop.disconnect()