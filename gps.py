import android, time, string

latitude = None
longitude = None
failed = True

def get_location(droid):
  print 'Finding location'
  droid.startLocating(5000)
  time.sleep(10)
  while 1:
    failed = True;
    location = droid.readLocation().result
    if location == {}:
      print "Current location unknown"
      location = droid.getLasKnownLocation().result
    if location != {}:
      if location['gps'] != None:
        print 'GPS: '
        latitude = location['gps']['latitude']
        longitude = location['gps']['longitude']
        failed = False
      elif location['network'] != {}:
        print 'Network: '
        latitude = location['network']['latitude']
        longitute = location['network']['longitude']
        failed = False
    if not failed:
      print 'Latitude: ' + str(latitude) + ' Longitude: ' + str(longitude) +'\n'
    else:
        print 'Failed to get location'
    time.sleep(5)
                             
                             
if __name__ == '__main__':
  droid = android.Android()
  get_location(droid)





