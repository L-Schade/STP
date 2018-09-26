import os
import thread
import time
# import gui        # GUI kennt dann nicht mehr die Module
from PIL import Image
from PIL import  ImageFilter
# from PIL import *
# import numpy as np
from matplotlib import pyplot as plt
import distance_calculator

list_len = 0
started_thread = 0

pointC = None
cid = None
fig = None


# list the latest images (only png), the number depend on maxi
def list_images(maxi):
    file_list = os.listdir('../Matlab/Bilder')
    # file_list = os.listdir('../Matlab/Bilder')
    file_list.sort(reverse=True)
    update_list_len()
    index = 1
    for file in file_list:
        if file.find('.png') == -1:     # TODO wirklich noetig
            file_list.remove(file)
        elif index == maxi:
            file_list.remove(file)
        else:
            # print(file)
            index += 1
    # delete_old_images()

    return file_list


# get the latest image
def latest_image():
    file_list = os.listdir('../Matlab/Bilder')
    file_list.sort(reverse=True)
    update_list_len()
    # print(fileList[0])

    return file_list[0]


def delete_old_images():
    file_list = os.listdir('../Matlab/Bilder')
    # file_list = os.listdir('../Matlab/Bilder')
    file_list.sort(reverse=True)
    for i in range(15, len(file_list),1):
        file_name = '../Matlab/Bilder/'+file_list[i]
        # file_name = '../Matlab/Bilder/'+file_list[i]
        os.remove(str(file_name))
    update_list_len()


def update_list_len():
    global list_len
    file_list = os.listdir('../Matlab/Bilder')
    # file_list = os.listdir('../Matlab/Bilder')
    list_len = len(file_list)


# TODO
# Thread richtig beenden

def update_images(thread):
    while True:
        global list_len, thread_started
        if int(list_len) == len(os.listdir('../Matlab/Bilder')):
        # if int(list_len) == len(os.listdir('../Matlab/Bilder')):
            print("...")
        elif int(list_len) < len(os.listdir('../Matlab/Bilder')):
        # elif int(list_len) < len(os.listdir('../Matlab/Bilder')):
            print("neues Bild wurde erstellt")
			# thread_started -= 1
            # gui.comment('Bild')
			# update_list_len()
            # thread.exit()
            break
        time.sleep(5)


def create_thread():
    try:
		# thread_started += 1
        thread.start_new_thread(update_images, (thread, ))
		
    except:
        print "Error: unable to start thread"
	while 1:
		pass
    # while 0 < thread_started:
        # pass

delete_old_images()
create_thread()

# list_img = list_images(4)
# print(list_img)

# latest_image()
# save_to_jpg('2018_05_24_14_47_27_669')
# new_size('2018_05_24_14_47_27_669')
