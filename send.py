# -*- coding: utf-8 -*
import serial

import time
import predict
import cv2
import RPi.GPIO as GPIO

import picamera
from time import sleep


from threading import Thread

class deal:
    def __init__(self):
        # 设置不显示警告
        global ser
        global c

        GPIO.setwarnings(False)

        # 设置读取面板针脚模式

        # 将引脚设置为输入模式

        GPIO.setmode(GPIO.BCM)
        # 设置读取针脚标号

        GPIO.setup(4, GPIO.IN)

       # GPIO.setup(2, GPIO.OUT)
        # 串口初始化
        ser = serial.Serial("/dev/ttyAMA0", 9600  ,timeout=0)
        time.sleep(1)
        c = predict.CardPredictor()

        c.train_svm()
        print('init ok!')


    def serial_send(self,strcar):#串口发送程序
        print('in serial')
        if ser.isOpen == False:
           ser.open()
           print('open')
           ser.write(strcar.encode(encoding="GB2312"))
           try:
               while True:
                     size = ser.inWaiting()
                     if size != 0:
                        response = ser.read(size)
                        print (response)
                        print('send ok!')
                        ser.flushInput()
                        time.sleep(0.1)
           except KeyboardInterrupt:
               if ser != None:
                  print('none')
                  ser.close()
        else:
            print('opened')
            print(strcar.encode(encoding="GB2312"))
            ser.write(strcar.encode(encoding="GB2312"))

            print('send ok!')
            print('income')
            size = ser.inWaiting()
            if size != 0:
                print('size')
                response = ser.read(size)
                print(response)
                print('send ok!')
                ser.flushInput()
                time.sleep(0.1)

                ser.close()

    def camera_vedio(self):
       #global img_bgr
        #if self.camera is None:
            #self.camera = cv2.VideoCapture(0)
            #if not self.camera.isOpened():
             #   print('警告,摄像头打开失败！')
              #  self.camera = None
               # return
       #predict_time = time.time()
       # _, img_bgr = self.camera.read()
      #print('Already photographed')
       camera = picamera.PiCamera()
       camera.capture('img_bgr.jpg')
       camera.start_preview()
       camera.vflip = True
       camera.hflip = True
       camera.brightness = 30
       sleep(0.01)
       camera.close()



if __name__ == '__main__':
    b = deal()
    while True:
            b.__init__()
            try:
             if GPIO.input(4) == GPIO. LOW:
                 print('Exorbitant vehicles')
                 time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things

                 b.camera_vedio()
                 time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
                 img_bgr = "img_bgr.jpg"
                 r, roi, color = c.predict(img_bgr)
                 car_str = ''.join(r)
                 if car_str.strip() != "":
                     b.serial_send('#')
                     print('recongnize ok！')
                     print(car_str)
                     b.serial_send(car_str)
                     b.serial_send('%')
             print('Runing')
            except KeyboardInterrupt:
                 if ser != None:
                    ser.close()





