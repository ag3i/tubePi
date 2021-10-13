# speak.py

import os,time,sys,RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    try:
        if  GPIO.input(23) != False:
            os.system('./aquestalkpi/AquesTalkPi -f speak.txt | aplay')
        time.sleep(0.1)                       
    except KeyboardInterrupt:               
        GPIO.cleanup()                      
        sys.exit()  
