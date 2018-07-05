import os
import edge_detection
# import datetime

name = None
x = None
y = None
z = None


# read old coordinates
def read_coordinates():
    file = open("coordinates.txt")
    index = 0
    for line in file:
        if (index == 0):
            x = line.rstrip()
        elif (index == 1):
            y = line.rstrip()
        elif(index == 2):
            z = line.rstrip()
        index = index+1;
    return x, y, z


# save the current position
def save_coordinates(x, y, z):
    file = open("coordinates.txt", "w")
    file.write(str(x)+'\n')
    file.write(str(y)+'\n')
    file.write(str(z)+'\n')
    # file.write(str(datetime.datetime.now()))
    file.close()


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
    print("class automatic")
    edge_detection.execute(name)

    # printScript(x,y,z,wait)
    # save_coordinates(x,y,z)


# coordinate modus
def coordinate():
    print("class coordinate")
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
    x, y, z = read_coordinates()
    key = raw_input("\n"
                "j: left \n"
                "k: down \n"
                "l: right \n"
                "i: up \n"
                "input:")
    if (key == "j"):
        x, y, z = left(x, y, z)
    elif (key == 'k'):
        x, y, z = down(x, y, z)
    elif (key == 'l'):
        x, y, z = right(x, y, z)
    elif (key == 'i'):
        x, y, z = up(x, y, z)
    else:
        print("undefined key pressed")
        exit()
    wait = input("enter the time to wait:")

    # printScript(x, y, z, wait)
    save_coordinates(x, y, z)

    key_in = (input("\n"
                    "m: Menu \n"
                    "n: navigate \n"
                    "q: exit"))
    if(key_in == 'm'):
        execute()
    elif(key_in == 'n'):
        navigate()
    elif(key_in == 'q'):
        exit()
    else:
        print("undefined key pressed")
        exit()

    return x, y, z, wait


# camera move to the left
def left(x, y, z):
    x = int(x) + 1
    print("moved to the left")
    return x, y, z


# camera move down
def down(x, y, z):
    y = int(y) + 1
    print("moved down")
    return x, y, z


# camera move to the right
def right(x, y, z):
    z = int(z) + 1
    print("moved to the right")
    return x, y, z


# camera move up
def up(x, y, z):
    x = int(x) + 1
    y = int(y) + 1
    print("moved up")
    return x, y, z


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
    file = open('Positionen/' + filename + '.txt', 'r')
    index = 0
    for line in file:
        if (index == 0):
            x = line.rstrip()
        elif (index == 1):
            y = line.rstrip()
        elif (index == 2):
            z = line.rstrip()
        index += 1
    return x, y, z


# x,y,z = read_coordinates()
# print(x, y, z)


def execute():
    print("choose the right mode:")
    print("press 1 for the automatically mode")
    print("press 2 for the coordinate mode")
    print("press 3 for the navigation mode")
    print("press 4 to choose an other image")

    key = input("choose your mode:")
    print(key)
    if(key == 1):
        automatic()
    elif (key == 2):
        x, y, z, wait = coordinate()
    elif(key == 3):
        x, y, z, wait = navigate()
    elif(key == 4):
       images()
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
