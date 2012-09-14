from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import ui_cdsGUI
import time
import cv

import serial


class CDSGUI(QDialog,ui_cdsGUI.Ui_Dialog):
  def __init__(self,parent=None):
    super(CDSGUI, self).__init__(parent)
    self._ser=serial.Serial('COM20',baudrate=9600)
    self.setupUi(self)
    self.DownButton.setAutoRepeat(True)
    self.UpButton.setAutoRepeat(True)
    self.LeftButton.setAutoRepeat(True)
    self.RightButton.setAutoRepeat(True)
    self.running = True
    self.xvalue = 90
    self.yvalue = 90
    
    

    
  def getImages(self):
    self.capture = cv.CaptureFromCAM(0)
    #i=0
    while self.running: 
      frame = cv.QueryFrame(self.capture)
      #print("here")
      if (not(frame==None)):
        cv.SaveImage("newImage.png",frame)
        self.Image= QImage("newImage.png")
        self.label.setPixmap(QPixmap().fromImage(self.Image))
        QApplication.processEvents()
        #cv.ShowImage("New Image", frame)
        cv.WaitKey(7)
        #print(i)
        #i=i+1
    
  #def event(self,event):
  #  if (event.type()==QEvent.KeyPress):
  #    print(event.key) 
  #  return True     
      
  #def keyPressEvent(self,event):
  #    print(event.key())
  #    if (event.key()==Qt.Key_Left):
  #        print("space")
      
  def keyPressEvent(self,event):  #Defined key presses on keypad
      print(event.key())     
      if (event.key()==43):
          print("+")
          self._ser.write("+")
      elif (event.key()==52):
          print("4")
          self._ser.write("4")
      elif (event.key()==50):
          print("2")
          self._ser.write("2")
      elif (event.key()==54):
          print("6")
          self._ser.write("6") 
      elif (event.key()==56):
          print("8")
          self._ser.write("8")
      elif (event.key()==16777216):
          print("close")
          self.close()
          self.running = False
         #cv.WaitKey(1000)
         #self._ser.write('.')
          self._ser.close() 
  
  @pyqtSignature("")
  def on_UpButton_clicked(self):
    print("8")
    self.yvalue = self.yvalue + 1
    self.verticalSlider.setValue(self.yvalue)
    self._ser.write("8")
  
  @pyqtSignature("")
  def on_DownButton_clicked(self):
    print ("2")
    self.yvalue = self.yvalue - 1
    self.verticalSlider.setValue(self.yvalue)
    self._ser.write("2")

  @pyqtSignature("")
  def on_LeftButton_clicked(self):
    print("4")
    self.xvalue = self.xvalue - 1
    self.horizontalSlider.setValue(self.xvalue)
    self._ser.write("4")
    
  @pyqtSignature("")
  def on_RightButton_clicked(self):
    print("6")
    self.xvalue = self.xvalue + 1
    self.horizontalSlider.setValue(self.xvalue)
    self._ser.write("6")
    
  @pyqtSignature("")
  def on_ExitButton_clicked(self):
    self.close()
    
  @pyqtSignature("")
  def on_FireButton_clicked(self):
    print("+")
    self._ser.write("+")
    
  def on_horizontalSlider_valueChanged(self, value):
    
    movement = value - self.xvalue
    if (movement > 0):
      while (movement > 0):  
        print("6")
        self._ser.write('6')
        movement = movement - 1
    else:
      movement = movement * -1
      while (movement > 0):  
        print("4")
        self._ser.write('4')
        movement = movement - 1      
    self.xvalue = value
    print(value)
    
  def on_verticalSlider_valueChanged(self, value):
    
    movement = value - self.yvalue
    if (movement > 0):
      while (movement> 0):  
        print("8")
        self._ser.write('8')
        movement = movement - 1
    else:
      movement = movement * -1
      while (movement > 0):  
        print("2")
        self._ser.write('2')
        movement = movement - 1      
    self.yvalue = value
    print(value)


  def closeEvent(self, event):
    print("close")
    self.running = False
    #cv.WaitKey(1000)
    self._ser.write('.')
    self._ser.close()
    
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  form = CDSGUI()
  form.show()
  QApplication.processEvents()
  #cv.WaitKey(1000)
  form.getImages()
  app.exec_()