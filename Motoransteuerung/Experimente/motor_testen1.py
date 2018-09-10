import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)

enable_pin = 19
pin_1 = 23
pin_2 = 2

GPIO.setup(enable_pin, GPIO.OUT) 
GPIO.setup(pin_1, GPIO.OUT) 
GPIO.setup(pin_2, GPIO.OUT) 
pwm_motor=GPIO.PWM(enable_pin,500) 
pwm_motor.start(0)

def forward(duty_cycle): 
    GPIO.output(pin_1, True) 
    GPIO.output(pin_2, False) 
    pwm_motor.ChangeDutyCycle(duty_cycle)


def reverse(duty_cycle): 
    GPIO.output(pin_1, False) 
    GPIO.output(pin_2, True) 
    pwm_motor.ChangeDutyCycle(duty_cycle)


def stop(): 
    GPIO.output(pin_1, False)
    GPIO.output(pin_2, False)
    pwm_motor.ChangeDutyCycle(0)

try: 
    while True: 
        direction = raw_input('w – forward, x – reverse, t - stop') 
        if (direction[0]=='t'):
            stop() 
        else:
            duty_cycle= input('Duty cycle (0-100%)')
            if (direction [0]=='w'):
                forward(duty_cycle)
            elif(direction [0]=='s'):
                reverse(duty_cycle)
 
finally: 
    print("Cleaning up") 
    GPIO.cleanup() 
