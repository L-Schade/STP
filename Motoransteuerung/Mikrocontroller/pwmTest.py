import wavePWM
import pigpio
import time
import os
from subprocess import Popen, PIPE


sudo_password = 'dP5678901'
command = 'pigpiod'.split()

p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE,
          universal_newlines=True)
sudo_prompt = p.communicate(sudo_password + '\n')[1]

pi=pigpio.pi()
pwm=wavePWM.PWM(pi)

pwm.set_frequency(50000)
print(pwm.frequency)
print(pwm.get_cycle_length())

pwm.set_pulse_start_and_length_in_fraction(4,0,1.5)
pwm.set_pulse_start_and_length_in_fraction(23,1/3,1.5)
pwm.set_pulse_start_and_length_in_fraction(24,2/3,1.5)

##pwm.set_pulse_start_and_length_in_micros(4,0,5000)
##pwm.set_pulse_start_and_length_in_micros(23,50,5)
##pwm.set_pulse_start_and_length_in_micros(24,200,5)


pwm.update()

time.sleep(2)
pwm.cancel()
