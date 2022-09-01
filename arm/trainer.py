import time
import RPi.GPIO as GPIO

import a
import b
print('you can proceed now...')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


'''l0'''
GPIO.setup(5, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, GPIO.PUD_UP)          

'''l1'''
GPIO.setup(13, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, GPIO.PUD_UP)

'''l2'''
GPIO.setup(26, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, GPIO.PUD_UP)

'''l3'''
GPIO.setup(20, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)

'''speed control pin'''
GPIO.setup(12, GPIO.IN, GPIO.PUD_UP)   

'''dummy pin'''
GPIO.setup(7, GPIO.IN, GPIO.PUD_UP)    
 

while True:
    if (GPIO.input(5)==GPIO.LOW):
        a.l0(1)                                      #lo ++
        print('l0 ++')
        
    if (GPIO.input(6)==GPIO.LOW):
        a.l0(-1)                                      #l0 --
        print('l0 --')
    
    if (GPIO.input(13)==GPIO.LOW):
        b.l1(1)
        print('l1 ++')
        
    if (GPIO.input(19)==GPIO.LOW):
        b.l1(-1)
        print('l1 --')
        
    if (GPIO.input(26)==GPIO.LOW):
        b.l2(1)
        print('l2 ++')
        
    if (GPIO.input(21)==GPIO.LOW):
        b.l2(-1)
        print('l2 --')
        
    if (GPIO.input(20)==GPIO.LOW):
        a.l3(1)
        print('l3 ++')
        
    if (GPIO.input(16)==GPIO.LOW):
        a.l3(-1)
        print('l3 --')
        
    if (GPIO.input(12)==GPIO.LOW):
        time.sleep(0.4)
        
    time.sleep(0.0001)