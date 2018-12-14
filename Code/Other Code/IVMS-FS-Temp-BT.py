#!/usr/bin/python

import RPi.GPIO as GPIO, time, os
import bme680
import bluetooth
import time

# Wia Setup
from wia import Wia
wia = Wia()
wia.access_token = ""   # Change to whatever secret key for your wia 


# Pressure Sensor
DEBUG = 1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)


# Temperature Sensor
sensor = bme680.BME680()
sensor.set_temperature_oversample(bme680.OS_8X)


def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(1)
    
    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

print ("================================================")
print ("     Vehicle Interior Safety System Check       ")
print ("================================================")	
	
# Loop to continuously check variable status values
while True:   
	#Pressure Sensor
    sensorvalue = RCtime(13)
	#Bluetooth Proximity
	nearby_devices = bluetooth.discover_devices()
	result = bluetooth.lookup_name("AA:BB:CC:DD:EE:FF", timeout=3)    # Enter MAC address of the BT device to lookout for 
	#Temperature Sensor 
	check_sensors = sensor.get_sensor_data():
    temp = sensor.data.temperature
    #temp1 = "{0:.2f} C".format(sensor.data.temperature)
	
	print ("Checking" + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
	print ("...")
    
    if (temp > 25 and sensorvalue < 500 and result == None):
	    print ("----------------------------------------------------------------------------")
        print ("    Passenger Seat: Occupied | Parent: Absent | Status: Unsafe [CAUTION]    ")
		print ("----------------------------------------------------------------------------")
        GPIO.output(11, True) #switch on
        lightstate = "On"
        time.sleep(1)
		
        alert = 'Unsafe'
		wia.Event.publish(name="Alert", data=alert)
			
    else:
	    print ("-------------------------------------------------------------")
        print ("             Vehicle Status | Under control                  ")
		print ("-------------------------------------------------------------")
        GPIO.output(11, False) #switch off
        lightstate="Off"
        time.sleep(1)
   
    print ("")
	print ("Pressure Sensor:")
    print (sensorvalue)
	print ("")
	print ("Temperature Sensor:")
	print (temp)
    time.sleep(20) 
	
    

    
    
