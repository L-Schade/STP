import RPi.GPIO as GPIO
import  time

pin_m1 = 11
pin_m2 = 17
pin_m3 = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_m1, GPIO.OUT)
# GPIO.setup(pin_m2, GPIO.OUT)
# GPIO.setup(pin_m3, GPIO.OUT)

m1 = GPIO.PWM(pin_m1, 50)
# m2 = GPIO.PWM(pin_m2, 50)
# m3 = GPIO.PWM(pin_m3, 50)

m1.start(0)
# m2.start(0)
# m3.start(0)

try:
    while True:
        m1.ChangeDutyCycle(10)
        time.sleep(0.5)

except KeyboardInterrupt:
    m1.stop()
    # m2.stop()
    # m3.stop()



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