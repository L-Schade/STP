import math
# import motor_controlG


def pixel_distance(pixel):
    distance = pixel * 0.0011465

    return distance


def angle_to_steps(angle):
    angle_per_step = 4
    steps = float(angle) / float(angle_per_step)

    return steps


def motor_a(x_pixel, distance):
    x_distance = pixel_distance(x_pixel)
    alpha = math.atan2(x_distance/distance)
    a_steps = angle_to_steps(alpha)


def motor_b(actual_distance):
    target_distance = int(8)
    correction = actual_distance - target_distance
    # beta =
    # b_steps = angle_to_steps(beta)


def motor_c(y_pixel, distance):
    y_distance = pixel_distance(y_pixel)
    gamma = math.atan2(y_distance / distance)
    c_steps = angle_to_steps(gamma)


def correction_b(steps):
    # TODO
    print("")


def correction_c(steps):
    steps_c = steps * (-1)  # TODO

