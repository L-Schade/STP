# -*- coding: utf-8 -*-

import datetime
# import motor_controlG

a = None
b = None
c = None
delay = None

# TODO
# methoden & variabeln umbennen sinnvoller


def read_position_delay():
    filename = open("position.txt")
    index = 0
    for line in filename:
        if index == 0:
            a = line.rstrip()
        elif index == 1:
            b = line.rstrip()
        elif index == 2:
            c = line.rstrip()
        elif index == 3:
            delay = line.rstrip()
        index += 1;
    return int(a), int(b), int(c), float(delay)


def read_position():
    filename = open("position.txt")
    index = 0
    for line in filename:
        if index == 0:
            a = line.rstrip()
        elif index == 1:
            b = line.rstrip()
        elif index == 2:
            c = line.rstrip()
        index += 1     # = index+1
    return int(a), int(b), int(c)


# position fits to image
def read_old_position(file_name):
    print(file_name)
    filename = open('Positionen/'+file_name+'.txt','r')
    index = 0
    for line in filename:
        if index == 0:
            a = line.rstrip()
        elif index == 1:
            b = line.rstrip()
        elif index == 2:
            c = line.rstrip()
        index += 1
    # save_position(a, b, c)
    return a, b, c


# save position in steps
def save_position(a, b, c,):
    filename = open("position.txt", "w")
    filename.write(str(a)+'\n')
    filename.write(str(b)+'\n')
    filename.write(str(c)+'\n')
    filename.write(str(1) + '\n')           # auto delay
    filename.write(str(datetime.datetime.now()))
    filename.close()
    print("save to file: position.txt")


def save_position_delay(a, b, c, delay):
    filename = open("position.txt", "w")
    filename.write(str(a)+'\n')
    filename.write(str(b)+'\n')
    filename.write(str(c)+'\n')
    filename.write(str(delay) + '\n')
    filename.write(str(datetime.datetime.now()))
    filename.close()
    print("save to file: position.txt")

