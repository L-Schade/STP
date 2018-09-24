import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_pin = 4 # gelb
coil_B_pin = 23 # gruen
coil_C_pin = 24 # blau
 
# Sequenz
StepCount = 6
Seq = list(range(0, StepCount))
Seq[0] = [1,0,0]
Seq[1] = [1,1,0]
Seq[2] = [0,1,0]
Seq[3] = [0,1,1]
Seq[4] = [0,0,1]
Seq[5] = [1,0,1]
 
#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_pin, GPIO.OUT)
GPIO.setup(coil_B_pin, GPIO.OUT)
GPIO.setup(coil_C_pin, GPIO.OUT)
 
#GPIO.output(enable_pin, 1)
 
def setStep(w1, w2, w3):
    GPIO.output(coil_A_pin, w1)
    GPIO.output(coil_B_pin, w2)
    GPIO.output(coil_C_pin, w3)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2])
            time.sleep(delay)
 
def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2])
            time.sleep(delay)
            
if __name__ == '__main__':
    while True:
        delay = raw_input("Zeitverzoegerung (ms)?")
        steps = raw_input("Wie viele Schritte vorwaerts? ")
        forward(int(delay) / 1000.0, int(steps))
        steps = raw_input("Wie viele Schritte rueckwaerts? ")
        backwards(int(delay) / 1000.0, int(steps))
