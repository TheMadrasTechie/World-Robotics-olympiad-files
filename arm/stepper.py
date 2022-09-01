import RPi.GPIO as gpio
import time
import sys
csv = open("Stepper.csv", "w") 
csv.write("Time,stepper-1,stepper-2")
gpio.setwarnings(False)

gpio.setmode(gpio.BCM)

gpio.setup(18,gpio.OUT)
gpio.setup(17,gpio.OUT)

gpio.setup(22,gpio.OUT)
gpio.setup(23,gpio.OUT)

current_step=[0,0]
tim = time.time()
def l1(stp):
    current_step[0]+=stp
    if (stp<0):
       gpio.output(18,gpio.HIGH)
       csv.write(str(int(time.time()-tim))",L1-,")
    else:
        gpio.output(18,gpio.LOW)
        csv.write(str(int(time.time()-tim))",L1+,")
    
    temp=abs(stp)
    for i in range(temp):
        gpio.output(17,gpio.HIGH)
        time.sleep(1/1000)
        gpio.output(17,gpio.LOW)
        time.sleep(1/1000)
        print('steps...')
    return current_step[0]
        
        
        
        

def l2(stp):
    current_step[1]+=stp
    if (stp<0):
       gpio.output(23,gpio.LOW)
       csv.write(str(int(time.time()-tim))",L2-")
    else:
        gpio.output(23,gpio.HIGH)
        csv.write(str(int(time.time()-tim))",L2+")
    
    temp=abs(stp)
    for i in range(temp):
        gpio.output(22,gpio.HIGH)
        time.sleep(1/1000)
        gpio.output(22,gpio.LOW)
        time.sleep(1/1000)
        print('steps...')
    return current_step[1]
        