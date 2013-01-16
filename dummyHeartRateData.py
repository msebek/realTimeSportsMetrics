#!/bin/python

# This script parses serial data, and sends it ot the redis server.

# This is a nasty, gross version. Will be repalced by matt kusbit's upon his completion.

import redis
import random
import time
import serial

FAKEDATA = False

host = '128.237.119.135'

r = redis.StrictRedis(host, port=6379, db=0)

port = '/dev/ttyUSB0'
ser = serial.Serial(port, 9600)
value = 0

while(True):
    time.sleep(.5)
    value = ser.readline()
    if(FAKEDATA == FALSE):
        if('=>' in value):
            #print value[14:]
            newValue = value[14:]
            heartrate = int(newValue[-5:])
            print value

    else:
        heartrate = 40 + int(random.normalvariate(10, 5))

    r.publish('foo', heartrate)

