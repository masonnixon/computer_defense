#include "Servo.h"

unsigned char angle=255;
unsigned char servoNum=255;

Servo servo1;
Servo servo2;


void setup()
{
    Serial.begin(9600);
    servo1.attach(9);
    servo2.attach(10);
}

void loop()
{
  while(servoNum==255)
 {
   servoNum=Serial.read();
   //Serial.println((int)servoNum);
 }
 while(angle==255)
 {
   angle=Serial.read();
   //Serial.println((int)angle);
 }
 
 
 
 switch(int(servoNum))
 {
   case 0:
     servo1.write((int)angle);
     break;
   case 1:
     servo2.write((int)angle);
     break;
 }
 
 
 angle=255;
 servoNum=255;
}
