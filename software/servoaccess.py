#!/usr/bin/env python

import serial
import struct
import time

def initLED():
#Resets the cursor and displays 0000
  ser.write('\x76') 
  ser.write('0000')
  changeBrightness(245)
  
def closePort():
  #Closes the connection to the LED
  ser.close();

def resetLED():
  #Resets the cursor and displays 0000
  ser.write('\x76') 
  ser.write('0000')
'''  
def changeBrightness(bright):
'''#Takes a brightness argument between 0 and 254
'''
  if(bright<0 or bright>254): return 0
  invert=254-bright
  ser.write('\x7A'+struct.pack('B',invert))
'''  
def displayWord(word):
  #Displays a four character phrase with error checking to ensure length is correct'''
  l=len(word)
  if(l<4):
    word=word.rjust(4,'X')
  ser.write(word[0:4])

def setDecimal(pos):
  pass
  #Takes a number from 

ser=serial.Serial('/dev/ttyUSB0',baudrate=9600)

#ser.write('5')

for i in range(1,20):
  ser.write('6')
  time.sleep(.5)

'''
ser.write('44444444444')
time.sleep(2)
ser.write('88888888888')
time.sleep(1)
ser.write('22222222222')
time.sleep(1)
ser.write('66666666666')
closePort()
'''
#changeBrightness(245)
 
