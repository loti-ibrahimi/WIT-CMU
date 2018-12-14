#!/usr/bin/python

'''
 
Setup:
- sudo apt-get install bluez
- sudo apt-get install python-bluez

'''

from wia import Wia
import bluetooth
import time

wia = Wia()
wia.access_token = "" # Wia secret key.

print ("Proximity Check")

while True:
    print ("Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))

    nearby_devices = bluetooth.discover_devices()

    result = bluetooth.lookup_name("AA:BB:CC:DD:EE:FF", timeout=3)  # Enter your device MAC address found in mobile settings. [Settings -> about (if on iphone)].
    if (result != None):
        print ("Parent: Present")
        presence = 'Present'
    else:
        print ("Parent: Absent")
        presence = 'Absent'

    wia.Event.publish(name="Parent", data=presence)

    time.sleep(20)
