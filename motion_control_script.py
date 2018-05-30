import os
import edge_detection
# import datetime

name = None


def readCoordinates():
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
    return x,y,z


def printScript(x,y,z,wait):
    file = open("script.mcs","w")
    file.write("UseMavlinkEmbedding( 57600, 82, 67, 71, 67 ); \n")
    file.write("SetAngle( {},{},{} );  # sets pitch, roll, yaw, in degrees \n"
               "Wait( {} );  # waits {} seconds \n".format(x,y,z,wait,wait))
    file.write("DoCamera('Shutter');  # ??? \n"
               "RecenterCamera();  # recenters all three axes\n"
               "TextOut('End');  # eigentlich: TextOut( 'End !mit Umbruch!' );")
    file.close()


def saveCoordinates(x,y,z):
    file = open("coordinates.txt", "w")
    file.write(str(x)+'\n')
    file.write(str(y)+'\n')
    file.write(str(z)+'\n')
    # file.write(str(datetime.datetime.now()))
    file.close()


def list_images(max):
    fileList = os.listdir('Matlab/Bilder')
    fileList.sort(reverse=True)
    index = 0
    for file in fileList:
        if file.find('.png') == -1:
            fileList.remove(file)
        elif index >= max:
            fileList.remove(file)
        else:
            # print(file)
            index += 1
    return fileList


def automatic():
    global name
    print("class automatic")
    edge_detection.execute(name)

    # printScript(x,y,z,wait)
    # saveCoordinates(x,y,z)


def coordinate():
    print("class coordinate")
    x = input("enter the x coordinate:")
    y = input("enter the y coordinate:")
    z = input("enter the z coordinate:")
    wait = input("enter the time to wait:")

    printScript(x,y,z,wait)
    saveCoordinates(x, y, z)

    return x,y,z,wait


def navigate():
    print("class navigate")
    x,y,z = readCoordinates()
    key = input("")
    if (key == 'j'):
        x = int(x)+1
    elif (key == 'k'):
        y = int(y)+1
    elif (key == 'l'):
        z = int(z)+1
    elif (key == 'i'):
        x = int(x)+1
        y = int(y)+1
    else:
        print("undefined key pressed")
        exit()
    wait = input("enter the time to wait:")

    printScript(x,y,z,wait)
    saveCoordinates(x, y, z)

    return x,y,z,wait


def latest_image():
    global name
    fileList = os.listdir('Matlab/Bilder')
    fileList.sort(reverse=True)
    # print(fileList[0])
    name = fileList[0]
    print(name)



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

    execute()

# x,y,z = readCoordinaten()
# print(x,y,z)


def execute():
    print("choose the right mode:")
    print("press 1 for the automatically mode")
    print("press 2 for the coordinate mode")
    print("press 3 for the navigation mode")
    print("press 4 to choose an other image")

    key = input("choose your mode:")
    print(key)
    if(key == '1'):   # python3 key == '1'
        automatic()
    elif (key == '2'):
        x,y,z,wait = coordinate()
    elif(key == '3'):
        x,y,z,wait = navigate()
    elif(key == '4'):
       images()
    else:
        print("undefined key pressed")
        exit()


latest_image()
execute()