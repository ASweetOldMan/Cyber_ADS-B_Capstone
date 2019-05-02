"""
Demos the tricks on the bebop. Make sure you have enough room to perform them!

Author: Amy McGovern
"""

from pyparrot.Bebop import Bebop

bebop = Bebop()

print("connecting")
success = bebop.connect(10)
print(success)

print("sleeping")
bebop.smart_sleep(1)
#
#bebop.ask_for_state_update()
#
#bebop.set_max_altitude(5)
#bebop.set_max_distance(10)
#bebop.enable_geofence(1)
#
#
#bebop.safe_takeoff(10)

#bebop.smart_sleep(1)
bebop.safe_land(10)

print("DONE - disconnecting")
bebop.disconnect()