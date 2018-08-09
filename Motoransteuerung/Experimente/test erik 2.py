import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(0)
print ("Start mit 0")
time.sleep(10)

p.ChangeDutyCycle(3)
print("3")
time.sleep(10)

while True:
    i = 4
    while i<10:

        print(i)
        p.ChangeDutyCycle(i)
        time.sleep(.05)
        i +=.02

    while i>4:
        print(i)
        p.ChangeDutyCycle(i)
        time.sleep(.05)
        i-=.05
