import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(04, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

pwm=GPIO.PWM(24, 100)
pwm.start(0)

GPIO.output(04, True)
GPIO.output(23, False)

pwm.ChangeDutyCycle(50)

GPIO.output(24, True)

sleep(2)

GPIO.output(24, False)
GPIO.output(04, False)
GPIO.output(23, True)

pwm.ChangeDutyCycle(75)

GPIO.output(24, True)

sleep(3)

GPIO.output(24, False)

# stop the Pulse
pwm.stop()

# and cleanup all of the GPIO channels.
GPIO.cleanup()
