# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt
import numpy as np


class Segment:
    x_start = None
    x_end = None
    y = None
    ind = None

    def __init__(self, x_start, x_end, y, ind):
        self.x_start = x_start
        self.x_end = x_end
        self.y = y
        self.parent = self
        self.ind = ind

    def parent(self):
        self.parent = self

    def get_root(self):
        seg = self
        while not seg == seg.parent:
            seg2 = seg                  # aktuellen Knoten merken
            seg = seg.parent
            seg2.parent = seg.parent    # Elternknoten wird zu Grosselternknoten
        return seg

    def get_size(self):
        pxl = self.x_end - self.x_start

        return pxl


class SegmentArea:
    x_start = None
    x_end = None
    y_start = None
    y_end = None
    ind = None
    elements = None     # in pixel
    root = None

    def __init__(self, x_start, x_end, y_start, y_end, ind, elements, root):
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.ind = ind
        self.elements = elements
        self.root = root

    # TODO
    # vlt noch bessere Methode zur Mittelpunktbestimmung
    def center(self):
        x = self.x_end-self.x_start
        y = self.y_end-self.y_start

        return [x, y]

    # def set_element(self, ind):
    #     self.elements = ind


def load_image(img_name):
    img = cv2.imread(img_name)       # (img_name, 0) / (img_name, cv2.WINDOW_NORMAL)
    width = img.shape[1]
    height = img.shape[0]
    print(width, height)

    # cv2.imshow('image', img)
    # k = cv2.waitKey(0)
    # if k == 27:  # wait for ESC key to exit
    #     cv2.destroyAllWindows()

    # plt.imshow(img)         # cmap='gray', interpolation='bicubic'
    # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    # plt.show()

    return img, width, height


def get_size(img):
    width = img.shape[1]
    height = img.shape[0]

    return width, height


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
    print(res)

    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)        # schwarz-weiss-Bild, gesuchter Bereich ist weiss
    # cv2.imshow('res', res)
    # k = cv2.waitKey(0) & 0xFF
    # if k == 27:
    #     cv2.destroyAllWindows()

    # TODO
    # bild wird nicht richtig gespeichert, farben
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


def compare_pixel_color(img, color, x_pixel, y_pixel):
    pxl_color = img[y_pixel, x_pixel]
    # print pxl_color
    if pxl_color[0] == color[0]:
        if pxl_color[1] == color[1]:
            if pxl_color[2] == color[2]:
                same_color = True
    else:
        same_color = False

    # print(same_color)
    return same_color


def color_area(img, color, color_range, x_pixel, y_pixel):
    pxl_color = img[y_pixel, x_pixel]
    # print pxl_color
    if (color[0]-color_range) <= pxl_color[0] <= (color[0]+color_range):
        if (color[1]-color_range) <= pxl_color[1] <= (color[1]+color_range):
            if (color[2] - color_range) <= pxl_color[2] <= (color[2] + color_range):
                same_color = True
    else:
        same_color = False

    # print(same_color)
    return same_color


# TODO
# gewissen bereich fuer pixelfarbe tolerieren?
def pixel_run(img, width, height, color):
    # print(color)
    segment_list = []
    # segment_li = []
    for y in range(0, height, 1):
        # for x in range(0, width, 1):
        x = 0
        while x < width:
            same_color = compare_pixel_color(img, color, x, y)

            while x < width and not same_color:
                x += 1

                if x < width:
                    same_color = compare_pixel_color(img, color, x, y)

            if x < width:
                x_start = x
                while x < width and same_color:
                    x += 1

                    if x < width:
                        same_color = compare_pixel_color(img, color, x, y)

                segment = Segment(x_start, x, y, 0)
                segment_list.append(segment)
                # segment_li.append([x_start, x, y])
    print segment_list
    # print segment_li
    print(len(segment_list))
    # print(len(segment_li))
    # segment_list.append([3, 4, 7])
    # segment_list.append([7, 3, 9])
    # print(segment[1][2])

    return segment_list


def pixel_run_(img, width, height, color, x_coord, y_coord):
    # print(color)
    segment_list = []
    # segment_li = []
    for y in range(0, height, 1):
        # for x in range(0, width, 1):
        x = 0
        while x < width:
            same_color = compare_pixel_color(img, color, x, y)
            # same_color = color_area(img, color, 10, x, y)

            while x < width and not same_color:
                x += 1

                if x < width:
                    same_color = compare_pixel_color(img, color, x, y)
                    # same_color = color_area(img, color, 10, x, y)

            if x < width:
                x_start = x
                while x < width and same_color:
                    x += 1

                    if x < width:
                        same_color = compare_pixel_color(img, color, x, y)
                        # same_color = color_area(img, color, 10, x, y)

                if x_start <= x_coord < x and y == y_coord:
                    segment = Segment(x_start, x, y, 1)
                    segment_list.append(segment)
                else:
                    segment = Segment(x_start, x, y, 0)
                    segment_list.append(segment)
                    # segment_li.append([x_start, x, y])
            # print pxl_color
    print segment_list
    # print segment_li
    print(len(segment_list))
    # print(len(segment_li))
    # segment_list.append([3, 4, 7])
    # segment_list.append([7, 3, 9])
    # print(segment[1][2])

    return segment_list


# algorithm
def united_regions(segment1, segment2):
    # root1 = segment1[3]
    # root2 = segment2[3]
    # if root1[2] < root2[2] or root1[2] == root2[2] and root1[0] < root2[0]:
    #     root2[4] = root1
    # else:
    #     root1[4] = root2
    # print("united regions")
    # for element in segment1:
    #     print element[0]
    #     print element[1]
    root1 = segment1.get_root()
    root2 = segment2.get_root()
    if root1.y < root2.y or root1.y == root2.y and root1.x_start < root2.x_start:
        root2.parent = root1
    else:
        root1.parent = root2


def create_regions(segments):
    i = 0
    j = 0
    print(len(segments))

    while i < len(segments):
        # if segments[j][2] + 1 == segments[i][2] and segments[j][0] < segments[i][1] and \
        #                 segments[i][0] < segments[j][1]:
        #     united_regions(segments[j], segments[i])
        # if segments[j][2] + 1 < segments[i][2] or segments[j][2] + 1 == segments[i][2] and\
        #                 segments[j][1] < segments[i][1]:
        #     j += 1
        # else:
        #     i += 1
        if segments[j].y + 1 == segments[i].y and segments[j].x_start < segments[i].x_end and \
                        segments[i].x_start < segments[j].x_end:
            united_regions(segments[j], segments[i])
        if segments[j].y + 1 < segments[i].y or segments[j].y + 1 == segments[i].y and \
                        segments[j].x_end < segments[i].x_end:
            j += 1
        else:
            i += 1


def count_roots(segments):
    root_list = []
    for segment in segments:
        if segment == segment.get_root():
            root_list.append(segment)

    return root_list


def define_area(roots, segments):
    areas = []
    ind = None
    for root in roots:
        x_start = root.x_start
        x_end = root.x_end
        y_start = root.y
        y_end = root.y
        elements = 0
        for segment in segments:
            if root == segment.get_root():
                if x_start > segment.x_start:
                    x_start = segment.x_start
                if x_end < segment.x_end:
                    x_end = segment.x_end
                if y_end < segment.y:
                    y_end = segment.y
                elements += segment.get_size()
            if segment.ind == 1:
                ind = 1
            else:
                ind = 0
        area = SegmentArea(x_start, x_end, y_start, y_end, ind, elements, root)
        areas.append(area)

    return areas


# TODO
# WZ-Segment erkennen
# verfahrpunkt ermitteln


def define_wz(areas):
    wz_area = None
    if len(areas) == 0:
        print("keine Elemente in der Liste\n"
              "Es wurden keine Bereiche gefunden")
        return None
    else:
        for area in areas:
            if area.ind == 0:
                if wz_area < area.elements:
                    wz_area = area
                elif wz_area == area.elements:
                    print("2 gleich grosse bereiche")
                    # TODO
                    #
            elif area.ind == 1:
                # TODO
                # koennte noch fehler enthalten
                wz_area = area
                break

        return wz_area


def draw_color(img, wz, segments):
    # TODO
    # schutzfunktion pixel farbe ueberhaupt enthalten

    new_img = cv2.imread(img)
    dim = (250, 125)
    new_img = cv2.resize(new_img, dim)
    for segment in segments:
        # if segment.get_root() == segment:
        if segment.get_root() == wz.root:
            color = [072, 118, 255]
            for x in range(segment.x_start, segment.x_end, 1):
                # new_img[segment.y, x] = [072, 118, 255]
                new_img[segment.y, x] = color
        # else:                                                 # alle segmente einer Farbe umfaerben/ anzeigen
        #     parent = segment.get_root()
        #     color = new_img[parent.y, parent.x_start]
        #     for x in range(segment.x_start, segment.x_end, 1):
        #         new_img[segment.y, x] = color

    plt.imshow(new_img)
    plt.show()

    return img


def movement(img_width, img_height, wz):
    img_center = [(img_width/2), (img_height/2)]
    # print(img_center)
    wz_center = wz.center()
    x_distance = wz_center[0]
    y_distance = wz_center[1]
    # print(x_distance)
    # print(y_distance)

    # return wz_center
    return x_distance, y_distance


def algorithm(img_name, color):
    # img, width, height = load_image(img_name)
    img, width, height = load_image('schwarz_weiss.jpeg')     # weiss_mit_scharzem_punkt.png
    dim = (250, 125)
    img_size = cv2.resize(img, dim)
    segments_list = pixel_run(img_size, 250, 125, color)
    # segments_list = pixel_run(img, width, height, color)
    # segments_list = pixel_run(img, width, height, [33, 33, 33])
    create_regions(segments_list)
    root_list = count_roots(segments_list)
    print(root_list)
    print(len(root_list))
    areas = define_area(root_list, segments_list)
    wz = define_wz(areas)

    if wz is not None:
        x_dist, y_dist = movement(width, height, wz)
        print(x_dist, y_dist)

        # draw_color(img_name, wz, segments_list)
        draw_color('schwarz_weiss.jpeg', wz, segments_list)

        return x_dist, y_dist
    else:
        return None, None


def algorithm_(img_name, color_rng, color, x_coord, y_coord):
    print('test')
    img, width, height = load_image(img_name)
    # img, width, height = load_image('schwarz_weiss.jpeg')     # weiss_mit_scharzem_punkt.png
    dim = (250, 125)
    img_size = cv2.resize(img, dim)
    segments_list = None

    if color_rng is None:
        segments_list = pixel_run_(img_size, 250, 125, color, x_coord, y_coord)
        # segments_list = pixel_run_(img_size, 500, 250, [33, 33, 33], x_coord, y_coord)
    elif color_rng is not None:
        segments_list = pixel_run_(img_size, 250, 125, color, x_coord, y_coord)
        # TODO
        # noch anpassen

    create_regions(segments_list)
    root_list = count_roots(segments_list)
    print(root_list)
    print(len(root_list))
    areas = define_area(root_list, segments_list)
    wz = define_wz(areas)

    if wz is not None:
        x_dist, y_dist = movement(width, height, wz)
        print(x_dist, y_dist)

        draw_color(img_name, wz, segments_list)
        # draw_color('schwarz_weiss.jpeg', wz, segments_list)

        return x_dist, y_dist
    else:
        return None, None


def execute(img):
    img, width, height = load_image(img)
    print img.shape
    # pxl = pixel_run(img, width, height, [255, 255, 255])    # weiss
    # united_regions(seg1, seg2)

    object_tracking('../Matlab/frame1.jpg', [110, 50, 50], [130, 255, 255])
    # new_img, width, height = load_image('test.png')
    new_img, width, height = load_image('schwarz_weiss.jpeg')

    # Testbild
    # pxl = pixel_run(new_img, height, width, [255, 255, 255])
    pxl = pixel_run(new_img, width, height [33, 33, 33])

    # basic_operations('../Matlab/Bilder/2018_05_24_14_43_25_647.png')


# execute('../Matlab/Bilder/2018_05_24_14_43_25_647.png')
# algorithm('d', 'd')


# for(int y = 0; y < outputFrame.rows; y++)
# {
#     for(int x = 0; x < outputFrame.cols; x++)
#     {
#         // I don't know which datatype I should use
#         if (outputFrame.at<INSERT_DATATYPE_HERE>(x,y) == 255)
#            //define area
#     }
# }

# Scalar intensity = img.at<uchar>(y, x);
