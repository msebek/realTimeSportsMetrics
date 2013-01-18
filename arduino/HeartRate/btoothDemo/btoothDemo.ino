#include <SoftwareSerial.h>

const int rxpin = 2;
const int txpin = 3;
//String in, a, b;
//int a, b;
SoftwareSerial bluetooth(rxpin, txpin);

void setup()
{
  Serial.begin(115200);
  bluetooth.begin(115200);
  Serial.println("Serial ready");
  bluetooth.println("Bluetooth ready");
}


void loop()
{
  String rec, lat, lon;
  char c = -1;
  char fx = -1;
  char ly = -1;
  //delay(3);
  
  while(!rec.endsWith("y")){
    if(bluetooth.available() > 0) rec += (char)bluetooth.read(); 
  }
  if(rec.length() > 0){
    Serial.println(rec);//prints "latitudexlongitudey"
    //Serial.flush();
   /* fx = rec.indexOf("x");
    ly = rec.lastIndexOf("y");
    Serial.println(fx);
    if(fx > 0 && ly < fx){
      lat = rec.substring(0, fx);
      lon = rec.substring(fx+1, ly);
      //Serial.print('lat: ');
      //Serial.println(lat);
      //Serial.print('lon: ');
      //Serial.println(lon);
    } 
    else{
      Serial.println('Error: Bad data');
    }  */

  }

    
  /*  
  }
  while(lat.length() < 12 || bluetooth.available() > 0){
    if(bluetooth.available() > 0){ 
      c = (char)bluetooth.read();
      if(c == 'x') break;
      lat += c;
    }
  }
  while(lon.length() < 12 || bluetooth.available() > 0){
    if(bluetooth.available() > 0){
      c = (char)bluetooth.read();
      if(c == 'x') break;
      lon += c;
    }
  }
  
  
  if(lat.length() >0 && lon.length() > 0)
  {
    Serial.println(lat.length());
    Serial.println(lat);
    Serial.println(lon);
    //a = in.substring(0,4);
    //b = in.substring(4,8);
   
    //Serial.println(a);
    //Serial.println(b);
  }
 */
/*  while (Serial.available() > 0){
        SerialInput.concat(char(bluetooth.read()));
        Serial.write(SerialInput);
        if(SerialInput.length() == 127){
         Serial.flush(); 
        }
      }
*/

}
  
