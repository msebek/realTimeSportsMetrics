#include <SoftwareSerial.h>

const int rxpin = 2;
const int txpin = 3;
String in, a, b;
//int a, b;
SoftwareSerial bluetooth(rxpin, txpin);

void setup()
{
  Serial.begin(115200);
  bluetooth.begin(11520);
  Serial.println("Serial ready");
  bluetooth.println("Bluetooth ready");
}


void loop()
{
  //delay(3);
  
  if(bluetooth.available() > 0)
  {
    Serial.println("Hi");
    char c = (char)bluetooth.read();
    in += c;
    Serial.write(c);
  
  }
  if(in.length() >0)
  {
    Serial.println(in);
    //a = in.substring(0,4);
    //b = in.substring(4,8);
   
    //Serial.println(a);
    //Serial.println(b);
  }
    
/*  while (Serial.available() > 0){
        SerialInput.concat(char(bluetooth.read()));
        Serial.write(SerialInput);
        if(SerialInput.length() == 127){
         Serial.flush(); 
        }
      }
*/
}
  
