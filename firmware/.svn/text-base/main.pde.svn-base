#include "Servo.h"

Servo servo1;								//Horizontal: +-90 degrees from center (Total: 180)
Servo servo2;								//Vertical:   +-45 degrees from center (Total: 90)
Servo servo3;

//PWM pins 3,5,6,9,10,11
int servoPin1 = 6;
int servoPin2 = 5;
int servoPin3 = 3;
int servoPin4 = 12;

int direction;								//Direction read from Serial port
int minPos = 0;
int maxPos = 180;
int centerPos = 90;
int currentPos1, currentPos2, currentPos3;

//Setup 
void setup()
{
	pinMode(servoPin1, OUTPUT);
	pinMode(servoPin2, OUTPUT);
	pinMode(servoPin3, OUTPUT);
	
	servo1.attach(servoPin1);
  	servo1.write(centerPos);  
	delay(15);
	servo2.attach(servoPin2);
  	servo2.write(centerPos); 
	delay(15);
	servo3.attach(servoPin3);
  	servo3.write(0); // Stop servo from moving initially
	
	currentPos1 = centerPos;
        currentPos2 = centerPos;
	currentPos3 = 0;
	
	pinMode(servoPin4, OUTPUT);
	Serial.begin(9600);						
}

void loop()
{
	if(Serial.available()) {
		direction = Serial.read();
		if(direction == 52) 						//Servo 1: Left (4)
		{
			if(currentPos1 > minPos)
			{
				currentPos1 = currentPos1 - 1;
				servo1.write(currentPos1);
			}
                      
		}
		else if(direction == 54)					//Servo 1: Right (6)
		{
			if(currentPos1 < maxPos)
			{
				currentPos1 = currentPos1 + 1;
				servo1.write(currentPos1);
			}
		}				
		else if(direction == 56)					//Servo 2: Up (8)
		{
			if(currentPos2 > 75)
			{
				currentPos2 = currentPos2 - 1;
				servo2.write(currentPos2);
			}
		}		
                else if(direction == 50)			                //Servo 2: Down (2) 
		{
			if(currentPos2 < 100)
			{
				currentPos2 = currentPos2 + 1;
				servo2.write(currentPos2);
			}
		}
		else if(direction == 43)					//Servo 3: Fire (+)
		{
			//Code air compressor
			digitalWrite(servoPin4, HIGH);   
			delay(100);              // wait for a second
			digitalWrite(servoPin4, LOW);  
                        delay(50);
			
			//Rotate 
            
			//digitalWrite(servoPin3, HIGH); 
                          
                          if(currentPos3 < 180)
                          {
    		  	  currentPos3 = currentPos3 + 37;
  
  			  servo3.write(currentPos3);
  			  }
                          else
                          {
                            currentPos3 = 0;
                            servo3.write(currentPos3);
                          }
			//servo3.writeMicroseconds(1500);
			//delay(1500);
			//servo3.write(0);
                        //digitalWrite(6, LOW); 
		}
		else if(direction == 53 || direction == 115)					//Center Servo 1 & Servo 2 (5 or s)
		{
			servo1.write(centerPos);
                        delay(500);
			servo2.write(centerPos);
			currentPos1 = centerPos;
                        currentPos2 = centerPos;
                        delay(1000);
		}
                else if(direction == 97)					//Turn Left All the way (a)
		{
                        servo1.write(5);
			currentPos1 = 5;
                        delay(1000);
		}
                else if(direction == 100)					//Turn Left All the way (d)
		{
                        servo1.write(175);
			currentPos1 = 175;
                        delay(1000);
		}
                else if(direction == 120)					//Go up All the way (e)
		{
                        servo2.write(100);
			currentPos2 = 100;
                        delay(1000);
		}
                else if(direction == 101)					//Go down All the way (x)
		{
                        servo2.write(75);
			currentPos2 = 75;
                        delay(1000);
		}
		
	}	
}
