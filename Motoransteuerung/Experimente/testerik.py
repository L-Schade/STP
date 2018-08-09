from time import sleep
import pigpio

GPIO.setmode(GPIO.BCM)

pi = pigpio.pi() 

ESC_GPIO = 4
pi.set_servo_pulsewidth(ESC_GPIO, 2000) # Maximum throttle.
sleep(2)
pi.set_servo_pulsewidth(ESC_GPIO, 1000) # Minimum throttle.
sleep(2)

while 1:
     pi.set_servo_pulsewidth(ESC_GPIO, 2000)
