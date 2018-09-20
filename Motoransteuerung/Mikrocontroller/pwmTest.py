import wavePWM
import pigpio
import time

pi=pigpio.pi()
pwm=wavePWM.PWM(pi)

pwm.set_frequency(8)
print(pwm.frequency)
print(pwm.get_cycle_length())

pwm.set_pulse_start_and_length_in_fraction(4,0,1.0/1.75)
pwm.set_pulse_start_and_length_in_fraction(23,1.0/6,1.0/1.75)
pwm.set_pulse_start_and_length_in_fraction(24,1.0/3,1.0/1.75)

##pwm.set_pulse_start_and_length_in_micros(4,0,5000)
##pwm.set_pulse_start_and_length_in_micros(23,50,5)
##pwm.set_pulse_start_and_length_in_micros(24,200,5)


pwm.update()

time.sleep(0.05)
pwm.cancel()
