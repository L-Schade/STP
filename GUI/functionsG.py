# -*- coding: utf-8 -*-

import math
# import motor_controlG
import read_save_position

distance = None
a = None
b = None
c = None
old_a = None
old_b = None
old_c = None

def pixel_resize():
	org_width = 1390
	org_height = 1040


def pixel_distance(pixel):
    dstnc = pixel * 0.0011465

    return dstnc


def angle_to_steps(angle):
    angle_per_step = 6
    if angle < 6:
        return 1
    steps = float(angle) / float(angle_per_step)

    return steps


def update_position():
    print("")
    # a, b, c =read_save_position.read_position()
    # update a, b, c
    # motion_control_scriptG.save_position(a, b, c)


def set_distance(dstnc):
    global distance
    distance = dstnc
    print(distance)


def set_old_position(file_name):
    global old_a, old_b, old_c
    old_a, old_b, old_c = read_save_position.read_old_position(file_name)


def set_current_position():
    a, b, c = read_save_position.read_position()
    print(a, b, c)


def motor(steps, delay, motor):
    print("")
    # motor_controlG.get_direction(delay, steps, a):
    if motor == 'a':
        correction_b(steps)
        correction_c(steps)
    elif motor == 'b':
        correction_c(steps)


def motor_a(x_pixel, delay):        # distance,
    global distance
    x_distance = pixel_distance(x_pixel)
    alpha = math.atan2(x_distance/distance)
    a_steps = angle_to_steps(alpha)
    # motor_controlG.get_direction(delay, a_steps, a):


def motor_b(delay):
    global distance
    target_distance = int(8)
    correction = target_distance - distance
    # beta =
    # b_steps = angle_to_steps(beta)
    # motor_controlG.get_direction(delay, b_steps, b):


def motor_c(y_pixel, delay):       # distance,
    global distance
    y_distance = pixel_distance(y_pixel)
    gamma = math.atan2(y_distance / distance)
    c_steps = angle_to_steps(gamma)
    # motor_controlG.get_direction(delay, c_steps, c):


def correction_b(steps):
    # TODO
    print("")


def correction_c(steps):
    steps_c = steps * (-1)  # TODO



def automatic():
    print("class automatic")
    # TODO
    # printScript()

    read_save_position.save_position(a, b, c)


def coordinate(x, y, wait):
    print('test')
    # neue Koordinatwen berechnen und speichern
    read_save_position.save_position(a, b, c)


# TODO
# delay mit übergeben
def up():
    a, b, c = read_save_position.read_position()
    c += 1
    read_save_position.save_position(a, b, c)

    motor(1, 1, 'c')


def left():
    a, b, c = read_save_position.read_position()
    a -= 1
    read_save_position.save_position(a, b, c)

    motor(-1, 1, 'a')


def right():
    a, b, c = read_save_position.read_position()
    a += 1
    read_save_position.save_position(a, b, c)

    motor(1, 1, 'c')


def down():
    a, b, c = read_save_position.read_position()
    c -= 1
    read_save_position.save_position(a, b, c)

    motor(-1, 1, 'c')


def delay(time):
    a, b, c = read_save_position.read_position()
    delay = float(time)
    read_save_position.save_position_delay(a, b, c, delay)


def opposite(image_name):
    print(image_name)
    print("Positionen/"+image_name)
    a, b, c = read_save_position.read_position()
    new_position = -1 * int(a)
    print(new_position)
    # print("illegal type")

    # TODO
    # Motoren ansteuern


