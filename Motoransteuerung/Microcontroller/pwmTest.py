import wavePWM
import pigpio
import time

pi=pigpio.pi()
pwm=wavePWM.PWM(pi)

pwm.set_frequency(3)

pwm.set_pulse_start_and_length_in_fraction(7,0,1.0/3)
pwm.set_pulse_start_and_length_in_fraction(16,0,1.0/3)
pwm.set_pulse_start_and_length_in_fraction(18,0,1.0/3)

pwm.update()
