#!/usr/bin/env python

######IMPORTS#################
import cv2
import time
import math
import numpy as np
from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
from pymavlink import mavutil

### Global Variables - Vehicle ###
vehicle = connect('udp:127.0.0.1:14551', wait_ready=True) # connect to drone in SITL
vehicle.parameters['PLND_ENABLED'] = 1 # PLND is parameter of ardupilot
vehicle.parameters['PLND_TYPE'] = 1 # companion computer

print('Connecting..')
connection_string = 'dev/ttyTHS1'
baud = 921600

vehicle = connect(connection_string , wait_ready =True, baud=baud)

print("Type : %s" % vehicle._vehicle_type)
print("Armed : %s" % vehicle.armed)
print("System status : %s" % vehicle.system_status.state)
print("GPS : %s" % vehicle.gps_0)
print("Alt : %s" % vehicle.location.global_relative_frame.alt)