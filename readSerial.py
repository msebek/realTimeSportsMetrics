import serial
ser = serial.Serial(6) # COMX so serial(X-1)
while 1:
    string = ser.readline()
    #print string
    x = [int(s) for s in string.split() if s.isdigit()]
    #print x
    #print len(x)
    avg = 0;
    if( len(x) != 0):
        for i in x[2:]:
            avg += i
        avg /= len(x)
        #print x
    print avg
    
