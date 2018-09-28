# -*- coding: utf-8 -*-

import math
import motor_controlG
import read_save_position

a = 0
b = 0
c = 0
old_a = 0
old_b = 0
old_c = 0
delay = 100
distance = 75
target_distance = 0
radius_a = 0
radius_b = 0


def pixel_resize(dist, axis):
	org_width = 1390
	org_height = 1040
	if axis == 'x':
		org_dist = (org_width * dist) / 500
	elif axis == 'z':
		org_dist = (org_height * dist) / 250
	return org_dist


def pixel_distance(pixel):
    dstnc = pixel * 0.00115

    return dstnc


def angle_to_steps(angle):
	print('Winkel: ' + str(angle))
	angle_per_step = 5.4545
	if 0.005 < angle < 5.54545:
		return 1
	elif -0.00115 < angle < 0.005:
		return 0
	elif -0.00115 > angle > -5.54545:
		return -1
	else:
		steps = float(angle) / float(angle_per_step)
		return int(steps)


def steps_to_angle(steps):
	angle = steps * 5.4545

	return angle


# update
def update_position(new_a, new_b, new_c):
    global a, b, c
    read_save_position.save_position(new_a, new_b, new_c)
    a = int(new_a)
    b = int(new_b)
    c = int(new_c)


def set_old_position(file_name):
    global old_a, old_b, old_c
    old_a, old_b, old_c = read_save_position.read_old_position(file_name)
    print('old Position: '+ old_a +' '+ old_b +' '+ old_c)


def set_current_position():
	global a, b, c
	a, b, c = read_save_position.read_position()
	print('current position: ' + str(a) +' '+ str(b) +' '+ str(c))
	
	
def set_delay(value):
	global delay
	delay = value


def set_distance(value):
    global distance
    distance = value
    print('distance: '+ str(distance))


def set_target_distance(value):
    global target_distance
    target_distance = value
    print('target_distance: '+ str(target_distance))


def set_radius_a(value):
    global radius_a
    radius_a = value
    print('radius_a: '+ str(radius_a))


def set_radius_b(value):
    global radius_b
    radius_b = value
    print('radius_b: '+ str(radius_b))


def motor(steps, delay, motor):
    print("")
    motor_controlG.setup()
    motor_controlG.get_direction(delay, steps, motor)
    # if motor == 'a':
    #     correction_b(steps)
    #     correction_c(steps)
    # elif motor == 'b':
    #     correction_c(steps)


def motor_a(x_pixel, delay):        # distance,
    global distance
    x_distance = pixel_resize(x_pixel,'x')
    org_x_distance = pixel_distance(x_distance)
    
    x = (org_x_distance / distance)
    alpha = math.atan(x)
    alpha = math.degrees(alpha)
    steps_a = angle_to_steps(alpha)
    
    motor_controlG.setup()
    motor_controlG.get_direction(int(delay), int(steps_a), 'a')
    
    print('Motor a: ' + str(steps_a))
    return steps_a


def motor_b(delay):
    global distance
    target_distance = int(8)
    correction = target_distance - distance
    # beta =
    # b_steps = angle_to_steps(beta)
    
    motor_controlG.setup()
    # motor_controlG.get_direction(delay, b_steps, 'b')


def motor_c(z_pixel, delay):       # distance,
    global distance
    z_distance = pixel_resize(z_pixel, 'z')
    org_z_distance = pixel_distance(z_distance)
    
    z = (org_z_distance / distance)
    gamma = math.atan(z)
    gamma = math.degrees(gamma)
    steps_c = angle_to_steps(gamma)
    
    motor_controlG.setup()
    motor_controlG.get_direction(delay, steps_c, 'c')
    
    print('Motor c: ' + str(steps_c))
    return steps_c


def correction_b(steps_a):
	alpha = steps_to_angle(steps_a)
	x = (((-1 * distance) - (radius_a * math.degrees(math.cos(alpha))) + target_distance) / (radius_b))
   	beta = math.asin(x)
   	beta = math.degrees(beta)
	new_position = angle_to_steps(beta)

	read_save_position.save_position(a, new_position, c)

	return new_position


def correction_c(steps_b):
	steps_c1 = steps_b * (-1)
	beta = steps_to_angle(steps_b)
	steps_c2 = radius_b - ((math.degrees(math.acos(beta)) * radius_b))
	steps_c = steps_c1 + steps_c2
	
	print('Korrektur c: ' + str(steps_c))
	return steps_c


def define_target_distance(alpha, beta):
	global target_distance, distance, radius_a, radius_b
	target_distance = distance + (radius_a * math.degrees(math.cos(alpha))) + (radius_b * math.degrees(math.sin(beta)))


def reference_point():
	global a, b, c
	set_current_position()
	
	motor((-1 * a), 100, 'a')
	motor((-1 * b), 100, 'b')
	motor((-1 * c), 100, 'c')
	


def latest_position():
	global old_a, old_b, old_c, a, b, c
	print(old_a, old_b, old_c, a, b, c)
	steps_a = (int(old_a) - int(a))
	steps_b = (int(old_b) - int(b))
	steps_c = (int(old_c) - int(c))
	
	motor(int(steps_a), 1, 'a')
	motor(int(steps_b), 1, 'b')
	motor(int(steps_c), 1, 'c')

	read_save_position.save_position(old_a, old_b, old_c)
	print('steps: '+ str(steps_a) +' '+ str(steps_b) +' '+ str(steps_c))

# TODO
# korrektur b
def automatic(x_dist, z_dist):
	global old_a, old_b, old_c, a, b, c

	steps_a = motor_a(x_dist, 1)
	steps_c = motor_c(z_dist, 1)
	
	new_a = int(old_a) + int(steps_a)
	new_b = int(old_b) - int(b)		# TODO
	# steps_b = int(correction_b(steps_a)
	# new_b = int(old_b) + )
	new_c = int(old_c) + int(steps_c)
	# steps_c = (int(steps_c) + int(correction_c(steps_b))
	# new_c = int(old_c) + int(steps_c)
	read_save_position.save_position(new_a, new_b, new_c)
	
	motor(steps_a, 1, 'a')
	motor(1, 1, 'b')
	motor(steps_c, 1, 'c')

	print(steps_a, 1, steps_c)
    

def tracking(x_dist, z_dist):
	global old_a, old_b, old_c, a, b, c

	steps_a = motor_a(x_dist, 1)
	steps_c = motor_c(z_dist, 1)
	
	new_a = int(old_a) + int(steps_a)
	new_b = int(old_b) - int(b)		# TODO
	new_c = int(old_c) + int(steps_c)
	read_save_position.save_position(new_a, new_b, new_c)
	
	motor(steps_a, 1, 'a')
	motor(1, 1, 'b')
	motor(steps_c, 1, 'c')

	print(steps_a, 1, steps_c)
    


def coordinate1(x, z, delay):
    global old_a, old_b, old_c, a, b, c
    
    steps_a = motor_a(int(x), 1)
    steps_c = motor_c(int(z), 1)
    
    new_a = int(old_a) + int(steps_a)
    new_b = int(old_b) - int(b)		# TODO
    new_c = int(old_c) + int(steps_c)
    read_save_position.save_position(new_a, new_b, new_c)
    
    motor(steps_a, 1, 'a')
    motor(1, 1, 'b')
    motor(steps_c, 1, 'c')
    
    print(steps_a, 1, steps_c)

	
def coordinate2(m_a, m_b, m_c, delay):
	global a, b, c
	print(old_a, old_b, old_c, a, b, c)
	steps_a = (int(m_a) - int(a))
	steps_b = (int(m_b) - int(b))
	steps_c = (int(m_c) - int(c))
	
	motor(int(steps_a), delay, 'a')
	motor(int(steps_b), delay, 'b')
	motor(int(steps_c), delay, 'c')

	read_save_position.save_position(m_a, m_b, m_c)
	print('steps: '+ str(steps_a) +' '+ str(steps_b) +' '+ str(steps_c))




# TODO
# delay mit übergeben
def up():
    global old_a, old_b, old_c, a, b, c, delay
    a, b, c = read_save_position.read_position()
    # update_position(old_a, old_b, old_c)
    c += 1
    read_save_position.save_position_delay(a, b, c, delay)

    motor(1, delay, 'c')


def left():
	global old_a, old_b, old_c, a, b, c, delay
	a, b, c = read_save_position.read_position()
	# update_position(old_a, old_b, old_c)
	a -= 1
	read_save_position.save_position_delay(a, b, c, delay)
	
	motor(-1, delay, 'a')


def right():
	global old_a, old_b, old_c, a, b, c, delay
	a, b, c = read_save_position.read_position()
	# update_position(old_a, old_b, old_c)
	a += 1
	read_save_position.save_position_delay(a, b, c, delay)
	
	motor(1, delay, 'a')


def down():
    global old_a, old_b, old_c, a, b, c, delay
    a, b, c = read_save_position.read_position()
    # update_position(old_a, old_b, old_c)
    c -= 1
    read_save_position.save_position_delay(a, b, c,delay)

    motor(-1, delay, 'c')




# def opposite(image_name):
    # print(image_name)
    # print("Positionen/"+image_name)
    # a, b, c = read_save_position.read_position()
    # new_position = -2 * int(a)
    # print(new_position)
    
    # motor((new_position), 1, 'a')
    # read_save_position.save_position_delay((new_position), b, c)
    
    # correction_b((2*new_position))
    # correction_c((2*new_position))



