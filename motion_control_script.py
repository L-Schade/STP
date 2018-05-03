
x = None
y = None
z = None
wait = None


def readCoordinaten():
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


def printScript():
    file = open("script.mcs","w")
    file.write("UseMavlinkEmbedding( 57600, 82, 67, 71, 67 ); \n")
    file.write("SetAngle( {},{},{} );  # sets pitch, roll, yaw, in degrees \n"
               "Wait( {} );  # waits 3 seconds \n".format(x,y,z,wait))
    file.write("DoCamera('Shutter');  # ??? \n"
               "RecenterCamera();  # recenters all three axes\n"
               "TextOut('End');  # eigentlich: TextOut( 'End !mit Umbruch!' );")
    file.close()


def saveCoordinaten(x,y,z):
    file = open("coordinates.txt", "w")
    file.write(str(x)+'\n')
    file.write(str(y)+'\n')
    file.write(str(z)+'\n')
    file.close()


def automatic():
    print("class automatic")


def coordinate():
    print("class coordinate")
    x = input("enter the x coordinate:")
    y = input("enter the y coordinate:")
    z = input("enter the z coordinate:")
    wait = input("enter the time to wait:")
    return x,y,z,wait


def navigate(x,y,z):
    print("class navigate")
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
    return x,y,z,wait


x,y,z = readCoordinaten()
print(x,y,z)

print("choose the right mode:")
print("press 1 for the automatically mode")
print("press 2 for the coordinate mode")
print("press 3 for the navigation mode")

key = input("choose your mode:")
print(key)
if(key == '1'):
    automatic()
elif key == '2':
    x,y,z,wait = coordinate()
elif(key == '3'):
    x,y,z,wait = navigate(x,y,z)
else:
    print("undefined key pressed")
    exit()

printScript()
saveCoordinaten(x,y,z)
