#!/bin/python

# This script parses serial data, and sends it ot the redis server.
# It sends it via the 


import redis
import random
import time
import serial
import json

FAKEDATA = True

#host = '128.237.253.170'
host = '128.237.253.170'

r = redis.StrictRedis(host, port=6379, db=0)

if(FAKEDATA==False):
    port = '/dev/ttyUSB0'
    ser = serial.Serial(port, 9600)

value = 0
timeElapsed = 0

# Sleep. Every second, emit a heartrate. Every five seconds, 
#  emit a GPS.
while(True):

    # Take in/make up data
    if(FAKEDATA==True):
        time.sleep(.5)
        timeElapsed+=.5
        heartrate = 40 + int(random.normalvariate(10, 5))
        if(timeElapsed % 5 == 0):
            tempLat = 40.442211 + random.normalvariate(0, .0001)
            tempLong = -79.946405 + random.normalvariate(0, .0001)
        else:
            tempLat = 0
            tempLong = 0

    else:
        value = ser.readline()
        print value
        # Check if value is a heartrate
        #if('=>' in value):
        #    #print value[14:]
        #    newValue = value[14:]
        #    heartrate = int(newValue[-5:])
        #    print value
        # value is not a heart rate
        #else:
            # find out if GPS coordinates
        heartrate=0
        tempLat = 40.442211
        tempLong = -79.946405



    # Convert to JSON
    message = json.dumps({"hr":heartrate, "lat":tempLat, "lng":tempLong})
    #print message
    r.publish('foo', message)


