# -*- coding:utf-8 -*-
# -------------------------------
# Filename:
# Revision:
# Date:        2013-02-5
# Author:      simonzhang
# Email:       simon-zzm@163.com
# WWW:         www.simonzhang.net
# -------------------------------
import serial
import time

#### 定义小灯亮灭初始值
i = 0
#### 实例化串口
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=0.5)
print('send satrt')
for j in range(10):
    if ser.isOpen() == False:
        ser.open()
        #### 每次循环对上值次取反
        if i == 0:
          i = 1
        else:
          i = 0
          ser.write(chr(i)) #### 向串口发送字符

          print('send ok')
       #### 获取串口返回值
       #### linux为福阻塞模式，在阻塞模式下
       #### 会报错，所以抱起来就好了。
    ser.write('open')  #### 向串口发送字符
    try:
       re = ser.readlines()
    except:
       pass
       print(re)
       time.sleep(2)