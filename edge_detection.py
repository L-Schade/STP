from PIL import Image
from PIL import ImageFilter
from PIL import ImageColor
import cv2
import numpy as np
from matplotlib import pyplot as plt

def opencvPython(image):
    img = cv2.imread(image,0)
    edges = cv2.Canny(img,100,200)

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()


def loadImage(titel):
    img = Image.open(titel)
    return img

def grayscale(image):
    width, height = image.size
    for x in range (width):
        for y in range (height):
            r,g,b = image.getpixel((x,y))
            intensity = int((r+g+b) / 3)
            image.putpixel((int(x),int(y)),( intensity,intensity,intensity))
    #image.show()
    return image

def edges(image):
    #img = image.filter(ImageFilter.EDGE_ENHANCE)
    img = image.filter(ImageFilter.FIND_EDGES)
    img.show(title=edges,command=edges)

def contour(image):
    img = image.filter(ImageFilter.CONTOUR)
    #img.show(title='contour',command='contour')

def edge_inking():
    color = ImageColor.getrgb('red')
    return color

img = loadImage("Bilder_BSP/filter1.jpg")
imageName = "Bilder_BSP/filter1.jpg"

#Funktion execute
imgG = grayscale(img)
edges(imgG)
contour(img)
edgeColor = edge_inking()
print (edgeColor)

opencvPython(imageName)