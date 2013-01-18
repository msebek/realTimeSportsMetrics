import android, time

BT_DEVICE_ID = '00:06:66:45:0C:FF'

droid = android.Android()
"""The first parameter is the service UUID for SerialPortServiceClass.
The second one is the address of your bluetooth module.
If the second one is ommited, Android shows you a selection at program start.
When this function succeeds the little led on the bluetooth module should stop blinking.
"""
droid.bluetoothConnect('00001101-0000-1000-8000-00805F9B34FB', BT_DEVICE_ID)

#droid.webViewShow('file:///sdcard/sl4a/scripts/androino.html')
while True:
    a = str(40.12345672238945)
    print a + '\n'
    #result = droid.eventWaitFor('fetch_data').result
    #droid.bluetoothWrite('a')  # send a space to your arduino to signal it to read a value from the sensor.
    #droid.bluetoothWrite('b')
    #droid.bluetoothWrite('c')
    for s in list(a):
        droid.bluetoothWrite(s)
        time.sleep(0.1)

    #sensor_data = droid.bluetoothReadLine().result  # read the line with the sensor value from arduino.
    #droid.eventClearBuffer()  # workaround for a bug in SL4A r4.
    #droid.eventPost('display_data', sensor_data)  # send an event with the sensor data back to the html page.
    time.sleep(5)
