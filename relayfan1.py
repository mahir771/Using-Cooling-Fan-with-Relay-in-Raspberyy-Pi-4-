import RPi.GPIO as GPIO
import os
import sys

PIN = 18
FAN_basla = 52

def GPIOsetup():
       GPIO.setwarnings(False)
       GPIO.setmode(GPIO.BCM)
       GPIO.setup(PIN, GPIO.OUT)
def fanON():
    GPIO.output(PIN, 0)
    return()
def fanOFF():
    GPIO.output(PIN, 1)
    return()
def CPUtemp():
       res = os.popen('vcgencmd measure_temp').readline() #"vcgencmd measure_temp" gives that CPU temp.
       return(res.replace("temp=","").replace("'C\n",""))  #return temp const
def temp():
     CPU_temp = float(CPUtemp())
     if CPU_temp>FAN_basla:
         fanON()
     else:
         fanOFF()
     return()
def basla():
   GPIOsetup()
   temp()
   fanOFF()
try:
   basla()
finally:
   GPIO.cleanup()
