import RPi.GPIO as GPIO
import time

global ind
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_pin = 4 # gelb
coil_B_pin = 23 # gruen
coil_C_pin = 24 # blau
 
# Sequenz
ind = 0
# half-steps
Seq = list(range(0, 6))
Seq[0] = [1,1,0]
Seq[1] = [1,0,0]
Seq[2] = [1,0,1]
Seq[3] = [0,0,1]
Seq[4] = [0,1,1]
Seq[5] = [0,1,0]
Seq[5] = [0,1,0]
# full-steps
##Seq = list(range(0, 3))
##Seq[0] = [1,0,0]
##Seq[1] = [0,1,0]
##Seq[2] = [0,0,1]


#GPIO.setup(enable_pin, GPIO.OUT)
##def setup():
##GPIO.setmode(GPIO.BCM)
GPIO.setup(coil_A_pin, GPIO.OUT)
GPIO.setup(coil_B_pin, GPIO.OUT)
GPIO.setup(coil_C_pin, GPIO.OUT)
 
#GPIO.output(enable_pin, 1)
 
def setStep(w1, w2, w3):
    GPIO.output(coil_A_pin, w1)
    GPIO.output(coil_B_pin, w2)
    GPIO.output(coil_C_pin, w3)

 
def forward(delay, steps):
    global ind
    for i in range(0, steps, 1):
        ind += 1
        ind = ind % 6
        print(ind)
        
        print(Seq[ind][0], Seq[ind][1], Seq[ind][2])
        setStep(Seq[ind][0], Seq[ind][1], Seq[ind][2])
        time.sleep(delay)


def backwards(delay, steps):
    global ind
    for i in range(0, steps, 1):
        ind -= 1
        ind = ind % 6
        print(ind)
        
        print(Seq[ind][0], Seq[ind][1], Seq[ind][2])
        setStep(Seq[ind][0], Seq[ind][1], Seq[ind][2])
        time.sleep(delay)      


def reference_point():
    # TODO
    # Warnung das nichts im Weg steht 
    GPIO.cleanup() 				# move to reference point


def move(x_angle, y_angle, delay):
    if x_angle > 0:
        forward((float(delay) / 1000.0), int(steps))
    else:
        backwards((float(delay) / 1000.0), int(steps))
    if y_angle > 0:
        forward((float(delay) / 1000.0), int(steps))
    else:
        backwards((float(delay) / 1000.0), int(steps))

              
if __name__ == '__main__':
    try:
        delay = raw_input("Zeitverzoegerung (ms)?")
        while True:
            ##        delay = raw_input("Zeitverzoegerung (ms)?")
            steps = raw_input("Wie viele Schritte vorwaerts? ")
            forward((float(delay) / 10.0),int(steps))
            steps = raw_input("Wie viele Schritte rueckwaerts? ")
            backwards((float(delay) / 10.0), int(steps))
    except KeyboardInterrupt:
        GPIO.cleanup()


# import datetime
# x = None
# y = None
# z = None
# wait = None
#
#
# def read_coordinates():
#     file = open("coordinates.txt")
#     index = 0
#     for line in file:
#         if (index == 0):
#             x = line.rstrip()
#         elif (index == 1):
#             y = line.rstrip()
#         elif(index == 2):
#             z = line.rstrip()
#         elif (index == 3):
#             wait = line.rstrip()
#         index += 1;
#     return x, y, z, wait
#
#
# def save_coordinates(x, y, z, wait):
#     file = open("coordinates.txt", "w")
#     file.write(str(x)+'\n')
#     file.write(str(y)+'\n')
#     file.write(str(z)+'\n')
#     file.write(str(wait) + '\n')
#     file.write(str(datetime.datetime.now()))
#     file.close()
#
#
# def automatic():
#     print("class automatic")
#
#     save_coordinates(x, y, z, wait)
#
#
# def coordinate(x, y, z, wait):
#     print('test')
#
#
# def up():
#     x, y, z, wait = read_coordinates()
#     x = int(x)+1
#
#     save_coordinates(x, y, z, wait)
#
#
# def left():
#     x, y, z, wait = read_coordinates()
#     y = int(y) + 1
#
#     save_coordinates(x, y, z, wait)
#
#
# def right():
#     x, y, z, wait = read_coordinates()
#     z = int(z)+1
#
#     save_coordinates(x, y, z, wait)
#
#
# def down():
#     x, y, z, wait = read_coordinates()
#     x = int(x)+1
#     y = int(y)+1
#
#     save_coordinates(x, y, z, wait)
#
#
# def wait3():
#     x, y, z, wait = read_coordinates()
#     wait = 3
#     save_coordinates(x, y, z, wait)
#
#
# def wait5():
#     x, y, z, wait = read_coordinates()
#     wait = 5
#     save_coordinates(x, y, z, wait)
