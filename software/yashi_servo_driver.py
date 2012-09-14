import serial
import time
from struct import *

ard=serial.Serial("/dev/ttyUSB0");

def setServoPos(ser, servoNum, angle):
        servo=pack('B', int(servoNum))
        ang=pack('B', int(angle))
        ser.write(servo)
        ser.write(ang)

while 1:

        num=raw_input("servo num:  ")
        ang=raw_input("angle:   ")
        setServoPos(ard, num, ang)
