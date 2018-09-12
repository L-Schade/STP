import cv2
from matplotlib import pyplot as plt
import numpy as np


def load_image(img_name):
    img = cv2.imread(img_name)       # (img_name, 0) / (img_name, cv2.WINDOW_NORMAL)
    height = img.shape[1]
    width = img.shape[0]
    print(height, width)

    # cv2.imshow('image', img)
    # k = cv2.waitKey(0)
    # if k == 27:  # wait for ESC key to exit
    #     cv2.destroyAllWindows()

    # plt.imshow(img)         # cmap='gray', interpolation='bicubic'
    # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    # plt.show()

    return img, height, width


def get_size(img):
    height = img.shape[1]
    width = img.shape[0]

    return height, width


def object_tracking(img_name, lower_color, upper_color):
    cap = load_image(img_name)     # cv2.VideoCapture(0)
    cap = cap[0]

    # Take each frame
    # _, frame = cap
    frame = cap

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array(lower_color)
    upper_blue = np.array(upper_color)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)         # (hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)        # schwarz-weiss-Bild, gesuchter Bereich ist weiss
    cv2.imshow('res', res)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()

    cv2.imwrite('test.png', mask)



def basic_operations(img_name):
    # lese Bild von Festplatte
    image = cv2.imread(img_name)

    # lese Farbwerte an Position y, x
    y = 100
    x = 50
    (b, g, r) = image[y, x]

    # gib Farbwerte auf Bildschirm aus
    print(b, g, r)

    # setze Farbwerte auf Rot (im BGR-Farbraum)
    image[y, x] = (0, 0, 255)

    # waehle ein Region auf Interest an Punkt: (y, x) mit Dimension 50x50 Pixel
    region_of_interest = image[y:y + 50, x:x + 50]

    # zeige Bild in Fenster an
    cv2.imshow("Bild", image)

    # zeige Region of Interest an
    cv2.imshow("ROI", region_of_interest)

    # setze ROI auf Gruen
    region_of_interest[:, :] = (0, 255, 0)

    # die ROI ist ein "Zeiger" auf das urspruenglich geladene Image. Es enthaelt nun eine gruene Box!
    cv2.imshow("Bild modifiziert", image)

    # warte auf Tastendruck (wichtig, sonst sieht man das Fenster nicht)
    cv2.waitKey(0)


def pixel_run(img, height, width, color):
    print(color)
    segment = []
    for y in range(0, height, 1):
        # for x in range(0, width, 1):
        x = 0
        while x < width:
            # TODO
            # Farbe wird nicht richtig "erkannt"
            pxl_color = img[x, y]
            print pxl_color
            if pxl_color[0] == color[0]:
                if pxl_color[1] == color[1]:
                    if pxl_color[2] == color[2]:
                        same_color = True
            else:
                same_color = False
            while x < width and not same_color:
                x += 1
            if x < width:
                x_start = x
                while x < width and same_color:
                    x += 1
                segment.append([x_start, x, y])
                # print(x, y)
            # print pxl_color
    print segment
    # segment.append([3, 4])
    # segment.append([7, 3])

    return segment


def define_regions(pxls):
    # TODO
    # vereinigen von segmenten
    print("define regions")
    for element in pxls:
        print element[0]
        print element[1]


# TODO
# WZ-Segment erkennen
# verfahrpunkt ermitteln

def execute(img):
    img, height, width = load_image(img)
    print img.shape
    pxl = pixel_run(img, height, width, [255, 255, 255])    # weiss
    define_regions(pxl)

    object_tracking('../Matlab/Bilder/frame1.jpg', [110, 50, 50], [130, 255, 255])
    new_img, height, width = load_image('test.png')
    pxl = pixel_run(new_img, height, width, [255, 255, 255])

    # basic_operations('../Matlab/Bilder/2018_05_24_14_43_25_647.png')


execute('../Matlab/Bilder/2018_05_24_14_43_25_647.png')
