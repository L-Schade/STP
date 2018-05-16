#python 3 Problem mit "pychairo" auf dem raspPi
from PIL import Image
from PIL import ImageFilter
from PIL import ImageColor
import numpy as np
from matplotlib import pyplot as plt
import distance_calculator

pointC = None


def loadImage(titel):
    img = Image.open(titel)
    return img


#wirklich noetig???
def imageSize(image):
    width, height = image.size
    return width,height


def edges(image):
    #img = image.filter(ImageFilter.EDGE_ENHANCE)
    img = image.filter(ImageFilter.FIND_EDGES)
    #img.show(title=edges,command=edges)
    plt.imshow(img)
    plt.show()
    return img


def contour(image):
    img = image.filter(ImageFilter.CONTOUR)
    # img.show(title='contour',command='contour')
    plt.imshow(img)
    plt.show()
    return img


def pixelColorSearch(image, color):
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


def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    x = event.xdata
    y = event.ydata
    global pointC
    pointC = [x,y]
    # print(pointC)
    plt.close()


def execute(imageName):
    # ???
    fig, ax = plt.subplots()
    ax.plot(np.random.rand(10))
    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    # imageName = "../Bilder_BSP/filter1.jpg"

    img = loadImage(imageName)
    edgesImg = edges(img)
    # contourImg = contour(img)

    # print(pointC)
    # print(focus(img))
    distance = distance_calculator.distance(focus(img),pointC)
    # print (distance)
    print('Abstand von {} zum Mittelpunkt: {}'.format(pointC,distance))