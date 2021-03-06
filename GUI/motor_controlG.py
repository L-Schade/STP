# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# global ind

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

coil_1A_pin = 15  # gelb
coil_2A_pin = 18  # gruen
coil_3A_pin = 14  # blau
coil_1B_pin = 12  # gelb
coil_2B_pin = 16  # gruen
coil_3B_pin = 7  # blau
coil_1C_pin = 26  # gelb
coil_2C_pin = 19  # gruen
coil_3C_pin = 21  # blau

# Sequenz
ind_a = 0
ind_b = 0
ind_c = 0
# half-steps
Seq = list(range(0, 6))
Seq[0] = [1, 0, 0]
Seq[1] = [1, 1, 0]
Seq[2] = [0, 1, 0]
Seq[3] = [0, 1, 1]
Seq[4] = [0, 0, 1]
Seq[5] = [1, 0, 1]
# Seq[0] = [1,1,0]
# Seq[1] = [1,0,0]
# Seq[2] = [1,0,1]
# Seq[3] = [0,0,1]
# Seq[4] = [0,1,1]
# Seq[5] = [0,1,0]

# full-steps
# Seq = list(range(0, 3))
# Seq[0] = [1,0,0]
# Seq[1] = [0,1,0]
# Seq[2] = [0,0,1]


# GPIO.setup(enable_pin, GPIO.OUT)
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(coil_1A_pin, GPIO.OUT)
    GPIO.setup(coil_2A_pin, GPIO.OUT)
    GPIO.setup(coil_3A_pin, GPIO.OUT)

    GPIO.setup(coil_1B_pin, GPIO.OUT)
    GPIO.setup(coil_2B_pin, GPIO.OUT)
    GPIO.setup(coil_3B_pin, GPIO.OUT)
   
    GPIO.setup(coil_1C_pin, GPIO.OUT)
    GPIO.setup(coil_2C_pin, GPIO.OUT)
    GPIO.setup(coil_3C_pin, GPIO.OUT)

# GPIO.output(enable_pin, 1)


def set_step(motor, w1, w2, w3):
    if motor == 'a':
        GPIO.output(coil_1A_pin, w1)
        GPIO.output(coil_2A_pin, w2)
        GPIO.output(coil_3A_pin, w3)
    elif motor == 'b':
        GPIO.output(coil_1B_pin, w1)
        GPIO.output(coil_2B_pin, w2)
        GPIO.output(coil_3B_pin, w3)
    elif motor == 'c':
        GPIO.output(coil_1C_pin, w1)
        GPIO.output(coil_2C_pin, w2)
        GPIO.output(coil_3C_pin, w3)
    else:
        print('')


def reference_point():
    GPIO.cleanup()  
    print("GPIO cleanup")


def forward(delay, steps, motor):
    global ind_a, ind_b, ind_c
    ind = 0
    if motor == 'a':
        ind = ind_a
    elif motor == 'b':
        ind = ind_b
    elif motor == 'c':
        ind = ind_c
    for i in range(0, steps, 1):
        ind += 1
        ind %= 6
        print(ind)

        print(Seq[ind][0], Seq[ind][1], Seq[ind][2])
        set_step(motor, Seq[ind][0], Seq[ind][1], Seq[ind][2])
        time.sleep(delay)
        
   	if motor == 'a':
		ind_a = ind
	elif motor == 'b':
		ind_b = ind
	elif motor == 'c':
		ind_c = ind


def backwards(delay, steps, motor):
    global ind_a, ind_b, ind_c
    ind = 0
    if motor == 'a':
        ind = ind_a
    elif motor == 'b':
        ind = ind_b
    elif motor == 'c':
        ind = ind_c
    for i in range(0, steps, 1):
        ind -= 1
        ind %= 6
        print(ind)

        print(Seq[ind][0], Seq[ind][1], Seq[ind][2])
        set_step(motor, Seq[ind][0], Seq[ind][1], Seq[ind][2])
        time.sleep(delay)
        
  	if motor == 'a':
  		ind_a = ind
	elif motor == 'b':
		ind_b = ind
	elif motor == 'c':
		ind_c = ind


def get_direction(delay, steps, motor):
    if steps > 0:
        forward((float(delay) / 1000.0), int(steps), motor)
        print("vorwärts" + str(steps))
    elif steps < 0:
        backwards((float(delay) / 1000.0), int(-1 * steps), motor)
        print("rückwärts" + str(steps))


if __name__ == '__main__':
    try:
        delay = raw_input("Zeitverzoegerung (ms)?")
        setup()
        while True:
            ##            delay = raw_input("Zeitverzoegerung (ms)?")
            steps = raw_input("Wie viele Schritte vorwaerts? ")
            forward((float(delay) / 1000.0), int(steps))
            steps = raw_input("Wie viele Schritte rueckwaerts? ")
            backwards((float(delay) / 1000.0), int(steps))
    except KeyboardInterrupt:
        GPIO.cleanup()
