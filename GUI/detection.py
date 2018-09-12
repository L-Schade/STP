import cv2
from matplotlib import pyplot as plt
import numpy as np


def load_image(img_name):
    img = cv2.imread(img_name)       # (img_name, 0) / (img_name, cv2.WINDOW_NORMAL)

    # cv2.imshow('image', img)
    # k = cv2.waitKey(0)
    # if k == 27:  # wait for ESC key to exit
    #     cv2.destroyAllWindows()

    # plt.imshow(img)         # cmap='gray', interpolation='bicubic'
    # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    # plt.show()

    return img


def object_tracking(img_name, lower_color, upper_color):
    cap = load_image(img_name)     # cv2.VideoCapture(0)
    while True:

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
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()


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


def execute(img):
    load_image(img)


# execute('../Matlab/Bilder/2018_05_24_14_43_25_647.png')
object_tracking('../Matlab/Bilder/frame1.jpg', [110, 50, 50], [130, 255, 255])
# basic_operations('../Matlab/Bilder/2018_05_24_14_43_25_647.png')
