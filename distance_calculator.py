# import numpy as np
import math
# import matplotlib.pyplot as plt


# distance
def distance(point_a, point_b):
    distance_a_b = math.sqrt(math.pow((point_a[0]-point_b[0]), 2) + math.pow((point_a[1]-point_b[1]), 2))
    return distance_a_b


# ???
def distance_image(di):
    return di


# distance in x,y direction
def dist(point_a, point_b):
    dist_x = point_a[0]-point_b[0]
    dist_y = point_a[1]-point_b[1]
    return dist_x, dist_y


# gradient
def calculate_line(point_a, point_b):
    # y = m * x + b
    m = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])   # slope
    return m


# focus
def center(x, y):
    x_m = x / 2
    y_m = y / 2
    return [x_m, y_m]


print(distance([3, 6], [3, 2]))
print(calculate_line([2, 5], [3, 4]))
