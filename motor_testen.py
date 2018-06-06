import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 16        # Pin fuer den Motor
Motor1B = 18
Motor1E = 22

# 2. Motor
Motor2A = 23        # 19
Motor2B = 21        # 21
Motor2E = 19        # 23

# alle als output setzen
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

print("Turning motor on, forwards")
GPIO.output(Motor1A, GPIO.HIGH)
GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1E, GPIO.HIGH)

sleep(2)

GPIO.output(Motor2A, GPIO.LOW)
GPIO.output(Motor2B, GPIO.HIGH)
GPIO.output(Motor2E, GPIO.HIGH)

sleep(2)

print("Now stop")
GPIO.output(Motor1E, GPIO.LOW)
GPIO.output(Motor2E, GPIO.LOW)


GPIO.cleanup()