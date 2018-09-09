import os
import edge_detection
from termcolor import colored
# import datetime

name = None
x = None
y = None
z = None
block = False
hold = False


# TODO
# Motoren sperren einbauen
def blocked():
    global block
    if block:       # True
        block = False
        print colored("Motoren wurden freigegeben!", 'green')
    elif not block:     # False
        block = True
        print colored("Motoren sind gesperrt!", 'red')
        # print("Motoren wurden gesperrt!\n")

    execute()


def motor_blocked():
    global block
    if block:   # True
        print colored("Motoren sind gesperrt", 'red')
        print("Motoren muessen erst noch freigegeben werden")
        # print("Um die Motoren freizugeben muss die Taste 0 gedrueckt werden\n")
        execute()

        return True
    elif not block:     # False
        print colored("Motoren sind freigegeben\n", 'green')
        return False
        # execute()


# Motoren halten einbauen


# read old coordinates
def read_coordinates():
    filename = open("coordinates.txt")
    ind = 0
    for line in filename:
        if ind == 0:
            x = line.rstrip()
        elif ind == 1:
            y = line.rstrip()
        elif ind == 2:
            z = line.rstrip()
        ind = ind+1;
    return x, y, z


# save the current position
def save_coordinates(x, y, z):
    filename = open("coordinates.txt", "w")
    filename.write(str(x)+'\n')
    filename.write(str(y)+'\n')
    filename.write(str(z)+'\n')
    # filename.write(str(datetime.datetime.now()))
    filename.close()


# list of images (number depent on maxi)
def list_images(maxi):
    file_list = os.listdir('Matlab/Bilder')
    file_list.sort(reverse=True)
    index = 0
    for file in file_list:
        if file.find('.png') == -1:
            file_list.remove(file)
        elif index >= maxi:
            file_list.remove(file)
        else:
            # print(file)
            index += 1
    return file_list


# automatic modus
def automatic():
    global name
    if not motor_blocked():     # False
        print("class automatic")
        edge_detection.execute(name)

    # printScript(x,y,z,wait)
    # save_coordinates(x,y,z)


# coordinate modus
def coordinate():
    print("class coordinate")
    if not motor_blocked():         # False
        x = input("enter the x coordinate:")
        y = input("enter the y coordinate:")
        z = input("enter the z coordinate:")
        wait = input("enter the time to wait:")

        # printScript(x,y,z,wait)
        save_coordinates(x, y, z)

        return x, y, z, wait


# navigate modus
def navigate():
    print("class navigate:")
    if not motor_blocked():     # False
        x, y, z = read_coordinates()
        key = raw_input("\n"
                    "j: left \n"
                    "k: down \n"
                    "l: right \n"
                    "i: up \n"
                    "o: auf die andere Seite fahren"
                    "input:")
        if key == "j":
            x, y, z = left(x, y, z)
        elif key == 'k':
            x, y, z = down(x, y, z)
        elif key == 'l':
            x, y, z = right(x, y, z)
        elif key == 'i':
            x, y, z = up(x, y, z)
        elif key == 'o':
            raw_in = raw_input ("Wollen Sie wirklich auf die andere Seite fahren?\n"
                               "Gehen Sie, dass keine Gegenstaende im weg sind,\n "
                               "dass der Verfahrweg frei ist!!!\n"
                               "j: ja\n"
                               "q: abbrechen\n")
            if raw_in == 'j':
                x, y, z = read_coordinates()
                new_position = -1 * int(x)
                print(new_position)

                # TODO
                # Motoren ansteuern

                execute()
            elif raw_in == 'q':
                execute()
        else:
            print("undefined key pressed")
            exit()
        wait = input("enter the time to wait:")

        # printScript(x, y, z, wait)
        save_coordinates(x, y, z)

        key_in = raw_input("\n"
                        "m: Menu \n"
                        "n: navigate \n"
                        "q: exit\n")
        if key_in == 'm':
            execute()
        elif key_in == 'n':
            navigate()
        elif key_in == "q":
            exit()
        else:
            print("undefined key pressed")
            exit()

        return x, y, z, wait


# camera move to the left
def left(x, y, z):
    new_x = int(x) + 1
    print("moved to the left")
    return new_x, y, z


# camera move down
def down(x, y, z):
    new_y = int(y) + 1
    print("moved down")
    return x, new_y, z


# camera move to the right
def right(x, y, z):
    new_z = int(z) + 1
    print("moved to the right")
    return x, y, new_z


# camera move up
def up(x, y, z):
    new_x = int(x) + 1
    new_y = int(y) + 1
    print("moved up")
    return new_x, new_y, z


# get the latest images
def latest_image():
    global name
    file_list = os.listdir('Matlab/Bilder')
    file_list.sort(reverse=True)
    # print(fileList[0])
    name = file_list[0]
    print(name)


# set an image from the latest
def images():
    global name
    images = list_images(9)
    index = 1
    for image in images:
        print(str(index)+": "+image)
        index +=1
    key = input("please select a picture:\n")
    name = images[(int(key)-1)]
    print(name+"\n")
    name = name.split('.')
    print(name[0])
    x, y, z = load_old_coordinates(name[0])
    save_coordinates(x, y, z)
    print(x, y, z)

    execute()


# get the position to an image
def load_old_coordinates(filename):
    global x, y, z
    #  print(filename)
    filename = open('Positionen/' + filename + '.txt', 'r')
    index = 0
    for line in filename:
        if index == 0:
            x = line.rstrip()
        elif index == 1:
            y = line.rstrip()
        elif index == 2:
            z = line.rstrip()
        index += 1
    return x, y, z


# x,y,z = read_coordinates()
# print(x, y, z)


def execute():
    print("choose the right mode:")
    print("press 0 to block the motors")
    print("press 1 for the automatically mode")
    print("press 2 for the coordinate mode")
    print("press 3 for the navigation mode")
    print("press 4 to choose an other image")

    key = input("choose your mode:")
    print(key)
    if key == 1:
        automatic()
    elif key == 2:
        x, y, z, wait = coordinate()
    elif key == 3:
        x, y, z, wait = navigate()
    elif key == 4:
       images()
    elif key == 0:
        blocked()
    else:
        print("undefined key pressed")
        exit()


latest_image()
execute()

# def printScript(x,y,z,wait):
#     file = open("script.mcs","w")
#     file.write("UseMavlinkEmbedding( 57600, 82, 67, 71, 67 ); \n")
#     file.write("SetAngle( {},{},{} );  # sets pitch, roll, yaw, in degrees \n"
#                "Wait( {} );  # waits {} seconds \n".format(x,y,z,wait,wait))
#     file.write("DoCamera('Shutter');  # ??? \n"
#                "RecenterCamera();  # recenters all three axes\n"
#                "TextOut('End');  # eigentlich: TextOut( 'End !mit Umbruch!' );")
#     file.close()
