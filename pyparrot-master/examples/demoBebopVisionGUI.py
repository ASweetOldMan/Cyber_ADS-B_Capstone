"""
Demo of the Bebop vision using DroneVisionGUI (relies on libVLC).  It is a different
multi-threaded approach than DroneVision

Author: Amy McGovern
"""
from pyparrot.Bebop import Bebop
from pyparrot.DroneVisionGUI import DroneVisionGUI
import threading
import cv2
import time

isAlive = False

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


def demo_user_code_after_vision_opened(bebopVision, args):
    bebop = args[0]

    print("Vision successfully started!")
    #removed the user call to this function (it now happens in open_video())
    
    #Video Config
    bebop.set_video_framerate("30_FPS")
    bebop.set_video_resolutions("rec1080_stream480")
    bebop.set_video_recording("quality")
    
#    bebopVision.start_video_buffering()
    print("Starting video stream")
    bebop.start_video_stream()

    # takeoff
    
    print("Take Off")
    bebop.safe_takeoff(5)
    
    bebop.smart_sleep(2)
    
    print(bebop.sensors.sensors_dict)
    bebop.smart_sleep(2)
    print(bebop.sensors.sensors_dict)
    
    bebop.move_relative(0, 0, -1, 0)  #move_relative(self, dx, dy, dz, dradians)
    print("First Move Done")
#    bebop.move_relative(0, 0, -0.5, 3.14)  #move_relative(self, dx, dy, dz, dradians)
#    print("Second Move Done")
    
#    print("Flying direct 1")
#    bebop.fly_direct(roll=0, pitch=-20, yaw=0, vertical_movement=0, duration=2)
    
    
#    bebop.move_relative(2, 0, 0, 0)
#    print("Second Move Done")
#    
#    bebop.move_relative(0, 0, 0, 3.14)
#    print("Third Move Done")
    
#    print("Flying direct 1")
#    bebop.fly_direct(roll=0, pitch=-20, yaw=0, vertical_movement=0, duration=2)
#    
#    bebop.move_relative(1, 0, 0, 0)
#    print("Fourth Move Done")
#    
#    bebop.move_relative(0, 0, 0, 3.14)
#    print("Fifth Move Done")

#    bebop.smart_sleep(2)
    
#    bebop.move_relative(0, 0, -1, 0)  #move_relative(self, dx, dy, dz, dradians)
#    print("First Move Done")
#    
    bebop.smart_sleep(1)
#
    print("flip left")
    print("flying state is %s" % bebop.sensors.flying_state)
    success = bebop.flip(direction="left")
    print("mambo flip result %s" % success)
    bebop.smart_sleep(2)
#    
#    bebop.move_relative(0, 2, 0, 0)  #move_relative(self, dx, dy, dz, dradians)
#    print("Second Move Done")
#
    bebop.safe_land(5)
    

    # skipping actually flying for safety purposes indoors - if you want
    # different pictures, move the bebop around by hand
#    print("Fly me around by hand!")
#    bebop.smart_sleep(15)
#
#    if (bebopVision.vision_running):
#        print("Moving the camera using velocity")
#        bebop.pan_tilt_camera_velocity(pan_velocity=0, tilt_velocity=-2, duration=4)
#        bebop.smart_sleep(5)
#
#        # land
#        bebop.safe_land(5)
#
#        print("Finishing demo and stopping vision")
#        bebopVision.close_video()

    # disconnect nicely so we don't need a reboot
    print("disconnecting")
    bebop.disconnect()

if __name__ == "__main__":
    # make my bebop object
    bebop = Bebop()

    # connect to the bebop
    success = bebop.connect(5)

    if (success):
        # start up the video
        bebopVision = DroneVisionGUI(bebop, is_bebop=True, user_code_to_run=demo_user_code_after_vision_opened,
                                     user_args=(bebop, ))

        userVision = UserVision(bebopVision)
        bebopVision.set_user_callback_function(userVision.save_pictures, user_callback_args=None)
        bebopVision.open_video()

    else:
        print("Error connecting to bebop.  Retry")

