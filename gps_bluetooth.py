import android, time

def send_btooth(droid):
    BT_DEVICE_ID = '00:06:66:45:0C:FF'

    """The first parameter is the service UUID for SerialPortServiceClass.
    The second one is the address of your bluetooth module.
    If the second one is ommited, Android shows you a selection at program start.
    When this function succeeds the little led on the bluetooth module should stop blinking.
    """
    droid.bluetoothConnect('00001101-0000-1000-8000-00805F9B34FB', BT_DEVICE_ID)

    while True:
        coordinates = get_location(droid)
        lat = coordinates[0]
        lon = coordinates[1]
        print 'Latitude: ' + str(lat) + ' Longitude: ' + str(lon) +'\n'
        if((lat != None) and (lon != None)):
            for s in list(str(lat)):
                droid.bluetoothWrite(s)
                time.sleep(0.1)
            droid.bluetoothWrite('x')
            for s in list(str(lon)):
                droid.bluetoothWrite(s)
                time.sleep(0.1)
            droid.bluetoothWrite('y')
        time.sleep(5)


def get_location(droid):
  latitude = None;
  longitude = None;
  count = 0;
  print 'Finding location'
  droid.startLocating(5000)
  time.sleep(10)
  while 1:
    count += 1
    failed = True
    location = droid.readLocation().result
    if location == {}:
      print "Current location unknown"
      location = droid.getLasKnownLocation().result
    if location != {}:
      if 'gps' in location:
        print 'GPS: '
        latitude = location['gps']['latitude']
        longitude = location['gps']['longitude']
        return (latitude, longitude)
      elif 'network' in location:
        print 'Network: '
        latitude = location['network']['latitude']
        longitute = location['network']['longitude']
        print 'Latitude: ' + str(latitude) + ' Longitude: ' + str(longitude) +'\n'
        return (latitude, longitude)
    if count == 5:
      print 'Timeout: Failed to get location\n'
      return (None, None)
    time.sleep(5)


if __name__ == '__main__':
  droid = android.Android()
  send_btooth(droid)

