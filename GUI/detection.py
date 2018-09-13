import cv2
from matplotlib import pyplot as plt
import numpy as np
# from segment.py import Segment

# segments:
# segment[0]        x_start
# segment[1]        x_end
# segment[2]        y
# segment[3]        root
# segment[4]        parent


class Segment:
    x_start = None
    x_end = None
    y = None

    def __init__(self, x_start, x_end, y):
        self.x_start = x_start
        self.x_end = x_end
        self.y = y
        self.parent = self

    def parent(self):
        self.parent = self

    def get_root(self):
        seg = self
        while not seg == seg.parent:
            seg2 = seg                  # aktuellen Knoten merken
            seg = seg.parent
            seg2.parent = seg.parent    # Elternknoten wird zu Grosselternknoten
        return seg


class SegmentArea:
    x_start = None
    x_end = None
    y_start = None
    y_end = None

    def __init__(self, x_start, x_end, y_start, y_end, members):
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.memmbers = members

    def center(self):
        x = self.x_end-self.x_start
        y = self.y_end-self.y_start

        return [x,y]


def load_image(img_name):
    img = cv2.imread(img_name)       # (img_name, 0) / (img_name, cv2.WINDOW_NORMAL)
    height = img.shape[1]
    width = img.shape[0]
    print(height, width)

    # cv2.imshow('image', img)
    # k = cv2.waitKey(0)
    # if k == 27:  # wait for ESC key to exit
    #     cv2.destroyAllWindows()

    plt.imshow(img)         # cmap='gray', interpolation='bicubic'
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

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


def pixel_run(img, height, width, color):
    print(color)
    segment_list = []
    # segment_li = []
    for y in range(0, height, 1):
        # for x in range(0, width, 1):
        x = 0
        while x < width:
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
                segment = Segment(x_start, x, y)
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
    for root in roots:
        x_start = root.x_start
        x_end = root.x_end
        y_start = root.y
        y_end = root.y
        ind = 0
        for segment in segments:
            if root == segment.get_root():
                if x_start > segment.x_start:
                    x_start = segment.x_start
                if x_end < segment.x_end:
                    x_end = segment.x_end
                if y_end < segment.y:
                    y_end = segment.y
                ind += 1
        area = SegmentArea(x_start, x_end, y_start, y_end, ind)
        areas.append(area)

    return areas

# TODO
# koennte noch fehler enthalten
# wird wahrscheinlich gar nicht benoetigt


def draw_color(img, segments):
    for segment in segments:
        if segment.get_root() == segment:
            color = [255, 255, 255]
            for x in range(segment.x_start, segment.x_end, 1):
                img[x, segment.y] = color
        else:
            parent = segment.get_root()
            color = img[parent.x_start, parent.y]
            for x in range(segment.x_start, segment.x_end, 1):
                img[x, segment.y] = color
        return img


# TODO
# WZ-Segment erkennen
# verfahrpunkt ermitteln


def define_wz(areas):
    wz_area = None
    for area in areas:
        if wz_area < area.members:
            wz_area = area




def algorithm():
    img, height, width = load_image('schwarz_weiss.jpeg')     # weiss_mit_scharzem_punkt.png
    segments_list = pixel_run(img, height, width,  [33, 33, 33])
    create_regions(segments_list)
    root_list = count_roots(segments_list)
    print(root_list)
    print(len(root_list))
    areas = define_area(root_list, segments_list)
    define_wz(areas)


def execute(img):
    img, height, width = load_image(img)
    print img.shape
    # pxl = pixel_run(img, height, width, [255, 255, 255])    # weiss
    # united_regions(seg1, seg2)

    object_tracking('../Matlab/frame1.jpg', [110, 50, 50], [130, 255, 255])
    # new_img, height, width = load_image('test.png')
    new_img, height, width = load_image('schwarz_weiss.jpeg')

    # Testbild
    # pxl = pixel_run(new_img, height, width, [255, 255, 255])
    pxl = pixel_run(new_img, height, width, [33, 33, 33])

    # basic_operations('../Matlab/Bilder/2018_05_24_14_43_25_647.png')


# execute('../Matlab/Bilder/2018_05_24_14_43_25_647.png')
algorithm()

