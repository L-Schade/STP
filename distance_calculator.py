import numpy as np
import math
import matplotlib.pyplot as plt


def distance(pointA,pointB):
   dist = math.sqrt(math.pow((pointA[0]-pointB[0]),2)+math.pow((pointA[1]-pointB[1]),2))
   return dist


def dist(pointA,pointB):
    distX = pointA[0]-pointB[0]
    distY = pointA[1]-pointB[1]
    return distX, distY



def calculate_line(pointA,pointB):
    #y = m * x + b
    m = (pointB[1] - pointA[1]) / (pointB[0] - pointA[0])   #slope
    return m


def center(x,y):
    xM = x/2
    yM = y/2
    return [xM,yM]


print (distance([3,6],[3,2]))
print (calculate_line([2,5],[3,4]))