import time
import RPi.GPIO as io

import a
import b

io.setmode(io.BCM)
io.setwarnings(False)

GPIO.setup(, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(, GPIO.IN, GPIO.PUD_UP)

while True:
    button_state = GPIO.input(button)
    if button_state == GPIO.HIGH:
      print ("HIGH")
    else:
      print ("LOW")
    time.sleep(0.5)