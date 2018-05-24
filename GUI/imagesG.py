#python 3 Problem mit "pychairo" auf dem raspPi
from PIL import Image
from PIL import ImageFilter
from PIL import *
import numpy as np
from matplotlib import pyplot as plt
import distance_calculator

pointC = None
cid = None
fig = None

def loadImage(titel):
    img = Image.open(titel)
    return img


# wirklich noetig???
def imageSize(image):
    width, height = image.size
    return width,height


def edges(image):
    #img = image.filter(ImageFilter.EDGE_ENHANCE)
    img = image.filter(ImageFilter.FIND_EDGES)
    #img.show(title=edges,command=edges)
    global fig
    fig = plt.imshow(img)
    plt.show(fig)
    return img


def contour(image):
    img = image.filter(ImageFilter.CONTOUR)
    # img.show(title='contour',command='contour')
    plt.imshow(img)
    plt.show()
    return img


def pixel_color_search(image, color):
    index = 0
    x, y = image.size
    for px in range(0,x):
        for py in range(0,y):
            rgb = image.getpixel((px,py))
            #r, g, b = image.convert('RGB').getpixel((x,y))
            if rgb == color:
                w, h = index+1, index+1;
                pixel = [[0 for x in range(w)] for y in range(h)]
                pixel[index][index] = (px,py)
                print(pixel)


def focus(image):
    width, height = image.size
    x = distance_calculator.center(width,height)
    return x


def save_to_jpg(name):
    im = Image.new("RGB", (128, 128))
    im = Image.open('../Matlab/Bilder/'+name+'.png')
    im.save('../Matlab/Bilder/'+name+'.jpg')


def new_size(name):
    size = 128, 128
    im = Image.open('../Matlab/Bilder/'+name+'.png')
    im.thumbnail(size, Image.BICUBIC)
    im.save('../Matlab/Bilder/'+name+'.', "JPEG")


save_to_jpg('2018_05_24_14_47_27_669')
new_size('2018_05_24_14_47_27_669')