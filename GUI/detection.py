# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt
import numpy as np
import distance_calculator


class Segment:
    x_start = None
    x_end = None
    z = None
    ind = None

    def __init__(self, x_start, x_end, z, ind):
        self.x_start = x_start
        self.x_end = x_end
        self.z = z
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

            # if seg.ind == 1:            #
            #     seg2.parent.ind = 1
            # if seg.parent.ind == 1:
            #     seg2.parent.ind = 1

        return seg

    def get_size(self):
        pxl = self.x_end - self.x_start

        return pxl


class SegmentArea:
    x_start = None
    x_end = None
    z_start = None
    z_end = None
    ind = None
    elements = None     # in pixel
    root = None

    def __init__(self, x_start, x_end, z_start, z_end, ind, elements, root):
        self.x_start = x_start
        self.x_end = x_end
        self.z_start = z_start
        self.z_end = z_end
        self.ind = ind
        self.elements = elements
        self.root = root

    # TODO
    # vlt noch bessere Methode zur Mittelpunktbestimmung
    def center(self):
        x = (self.x_end + self.x_start)/2           # self.x_end - self.x_start
        z = (self.z_end + self.z_start)/2               # self.z_end - self.z_start

        print(x, z)
        return [x, z]

    # def set_element(self, ind):
    #     self.elements = ind


def load_image(img_name):
    img = cv2.imread(img_name)       # (img_name, 0) / (img_name, cv2.WINDOW_NORMAL)
    width = img.shape[1]
    height = img.shape[0]
    # print(width, height)

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


def compare_pixel_color(img, color, x_pixel, z_pixel):
    pxl_color = img[z_pixel, x_pixel]
    # print(pxl_color, x_pixel, z_pixel)
    if pxl_color[0] == color[0]:
        if pxl_color[1] == color[1]:
            if pxl_color[2] == color[2]:
                same_color = True
    else:
        same_color = False

    # print(same_color)
    return same_color


def color_area(img, color, color_range, x_pixel, z_pixel):
    pxl_color = img[z_pixel, x_pixel]
    # print pxl_color
    if (color[0]-int(color_range)) <= pxl_color[0] <= (color[0]+int(color_range)):
        if (color[1]-int(color_range)) <= pxl_color[1] <= (color[1]+int(color_range)):
            if (color[2] - int(color_range)) <= pxl_color[2] <= (color[2] + int(color_range)):
                same_color = True
    else:
        same_color = False

    # print(same_color)
    return same_color


def pixel_run(img, width, height, color, color_rng, x_coord, z_coord):
    # print(color)
    segment_list = []
    # segment_li = []
    for z in range(0, height, 1):
        # for x in range(0, width, 1):
        x = 0
        while x < width:
            if color_rng is None:
                same_color = compare_pixel_color(img, color, x, z)
            elif color_rng is not None:
                same_color = color_area(img, color, color_rng, x, z)

            while x < width and not same_color:
                x += 1

                if x < width:
                    if color_rng is None:
                        same_color = compare_pixel_color(img, color, x, z)
                    elif color_rng is not None:
                        same_color = color_area(img, color, color_rng, x, z)

            if x < width:
                x_start = x
                while x < width and same_color:
                    x += 1

                    if x < width:
                        if color_rng is None:
                            same_color = compare_pixel_color(img, color, x, z)
                        elif color_rng is not None:
                            same_color = color_area(img, color, color_rng, x, z)

                if x_coord is not None and z_coord is not None:
                    # print(x_start, x_coord, x, z, z_coord)
                    if int(x_start) <= int(x_coord) < int(x) and int(z) == int(z_coord):
                        print('Segment mit ind=1')
                        print(x_start, x, z,)
                        segment = Segment(x_start, x, z, 1)
                        segment_list.append(segment)
                    else:
                        segment = Segment(x_start, x, z, 0)
                        segment_list.append(segment)
                        # segment_li.append([x_start, x, z])
                else:
                    segment = Segment(x_start, x, z, 0)
                    segment_list.append(segment)

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
    if root1.z < root2.z or root1.z == root2.z and root1.x_start < root2.x_start:
        root2.parent = root1

        # if root1.ind == 1:          #
        #     root2.ind = 1

    else:
        root1.parent = root2

        # if root2.ind == 1:          #
        #     root1.ind = 1


def create_regions(segments):
    i = 0
    j = 0
    # print(len(segments))

    while i < len(segments):
        # if segments[j][2] + 1 == segments[i][2] and segments[j][0] < segments[i][1] and \
        #                 segments[i][0] < segments[j][1]:
        #     united_regions(segments[j], segments[i])
        # if segments[j][2] + 1 < segments[i][2] or segments[j][2] + 1 == segments[i][2] and\
        #                 segments[j][1] < segments[i][1]:
        #     j += 1
        # else:
        #     i += 1
        if segments[j].z + 1 == segments[i].z and segments[j].x_start < segments[i].x_end \
                and segments[i].x_start < segments[j].x_end:
            united_regions(segments[j], segments[i])
        if segments[j].z + 1 < segments[i].z or segments[j].z + 1 == segments[i].z \
                and segments[j].x_end < segments[i].x_end:
            j += 1
        else:
            i += 1


def count_roots(segments):
    root_list = []
    for segment in segments:
        if segment == segment.get_root():
            print(segment.ind)
            root_list.append(segment)

    return root_list


def define_area(roots, segments):
    areas = []
    ind = None
    for root in roots:
        x_start = root.x_start
        x_end = root.x_end
        z_start = root.z
        z_end = root.z
        elements = 0
        for segment in segments:
            if root == segment.get_root():
                if x_start > segment.x_start:
                    x_start = segment.x_start
                if x_end < segment.x_end:
                    x_end = segment.x_end
                if z_end < segment.z:
                    z_end = segment.z
                print(segment.ind)
                if segment.ind == 1:            # einrückung war verkehrt?!
                    ind = 1
                else:
                    ind = 0
                elements += segment.get_size()
        area = SegmentArea(x_start, x_end, z_start, z_end, ind, elements, root)
        print(x_start, x_end, z_start, z_end, ind)
        areas.append(area)

    return areas


# TODO
# Fehler finden, vlt beim vereinigen wird index nicht übertragen? -> müsste behoben sein
# WZ-Segment erkennen
# verfahrpunkt ermitteln


def define_wz(areas):
    # wz_area = None
    wz_area = SegmentArea(0, 0, 0, 0, 0, 0, 0)
    if len(areas) == 0:
        print("keine Elemente in der Liste\n"
              "Es wurden keine Bereiche gefunden")
        return None
    else:
        for area in areas:
            if area.ind == 0:
                # if wz_area < area.elements:
                if wz_area.elements < area.elements:
                    wz_area = area
                elif wz_area.elements == area.elements:
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
    if segments is not None:
        new_img = cv2.imread(img)
        dim = (250, 125)
        new_img = cv2.resize(new_img, dim)
        for segment in segments:
            # if segment.get_root() == segment:
            if segment.get_root() == wz.root:
                color = [072, 118, 255]
                for x in range(segment.x_start, segment.x_end, 1):
                    # new_img[segment.z, x] = [072, 118, 255]
                    new_img[segment.z, x] = color

        new_img = cv2.resize(new_img, (500, 250))
        cv2.imwrite("wz_detection.png", new_img)
        # plt.imshow(new_img)
        # plt.show()

        return img

    else:

        return None


def movement(img_width, img_height, wz):
    img_center = [(img_width/2), (img_height/2)]
    wz_center = wz.center()

    distance = distance_calculator.dist(img_center, wz_center)
    print(distance)
    x_distance = distance[0]        # wz_center[0] - img_width
    z_distance = distance[1]        # wz_center[1] - img_height
    # print(x_distance)
    # print(z_distance)

    # return wz_center
    return x_distance, z_distance


def algorithm(img_name, color_rng, color, x_coord, z_coord):
    print('algorithm')
    img, width, height = load_image(img_name)
    # img, width, height = load_image('schwarz_weiss.jpeg')

    width, height = 250, 125
    dim = (width, height)        # Bild in GUI (500, 250)
    img_size = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    if x_coord is not None and z_coord is not None:
        x, z = (x_coord / 2), (z_coord / 2)
        print(x, z)

        color = img_size[z, x]
        print(color)

        segments_list = pixel_run(img_size,  width, height, color, color_rng, x, z)
        # segments_list = pixel_run(img_size, 500, 250, [33, 33, 33], color_rng, x_coord, z_coord)
    else:
        segments_list = pixel_run(img_size,  width, height, color, color_rng, x_coord, z_coord)
        # segments_list = pixel_run(img_size, 500, 250, [33, 33, 33], color_rng, x_coord, z_coord)

    create_regions(segments_list)
    root_list = count_roots(segments_list)
    print(root_list)
    print(len(root_list))
    areas = define_area(root_list, segments_list)
    wz = define_wz(areas)

    if wz is not None:
        x_dist, z_dist = movement(width, height, wz)
        # print(x_dist, z_dist)

        draw_color(img_name, wz, segments_list)
        # draw_color('schwarz_weiss.jpeg', wz, segments_list)

        x_dist *= 2     # von 250x125 -> 500x250
        z_dist *= 2

        return x_dist, z_dist   # , img
    else:
        return None, None   # , None


# Scalar intensity = img.at<uchar>(y, x);
