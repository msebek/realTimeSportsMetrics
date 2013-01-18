#!/bin/python

# This script parses serial data, and sends it ot the redis server.
# It sends it via the 


import redis
import random
import time
import serial
import json

fakeHeartRate = False
fakeLocation = True

#host = '128.237.253.170'
host = '128.237.253.170'

r = redis.StrictRedis(host, port=6379, db=0)

if(fakeHeartRate==False or fakeLocation==False):
    print "connecting..."
    port = '/dev/ttyUSB1'
    ser = serial.Serial(port, 9600)
    print "connected!"

value = 0
timeElapsed = 0

# Sleep. Every second, emit a heartrate. Every five seconds, 
#  emit a GPS.
while(True):

    # Take in/make up data
    if(fakeHeartRate==True):
        time.sleep(.5)
        timeElapsed+=.5
        heartrate = 40 + int(random.normalvariate(10, 5))
    if(fakeLocation == True):
        if(timeElapsed % 5 == 0):
            tempLat = 40.442211 + random.normalvariate(0, .0001)
            tempLong = -79.946405 + random.normalvariate(0, .0001)
        else:
            tempLat = 0
            tempLong = 0
        timeElapsed+=.5

    if(fakeHeartRate==False):
        try:
            serialLine = ser.readline()
        except:
            serialLine="bad."
        print serialLine
        # See if it's a heartrate
        if('Hr:' in serialLine):
            heartrate = int(str(serialLine[3:]))
        # value is not a heart rate

    
    if(fakeLocation==False):
        assert(false)
            
    # Convert to JSON
    message = json.dumps({"hr":heartrate, "lat":tempLat, "lng":tempLong})
    #print message
    r.publish('foo', message)


