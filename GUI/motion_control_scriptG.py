x = None
y = None
z = None
wait = None


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
        elif (index == 3):
            wait = line.rstrip()
        index = index+1;
    return x,y,z,wait


def printScript():
    file = open("script.mcs","w")
    file.write("UseMavlinkEmbedding( 57600, 82, 67, 71, 67 ); \n")
    file.write("SetAngle( {},{},{} );  # sets pitch, roll, yaw, in degrees \n"
               "Wait( {} );  # waits {} seconds \n".format(x,y,z,wait,wait))
    file.write("DoCamera('Shutter');  # ??? \n"
               "RecenterCamera();  # recenters all three axes\n"
               "TextOut('End');  # eigentlich: TextOut( 'End !mit Umbruch!' );")
    file.close()


def printScript1(x,y,z,wait):
    file = open("script.mcs","w")
    file.write("UseMavlinkEmbedding( 57600, 82, 67, 71, 67 ); \n")
    file.write("SetAngle( {},{},{} );  # sets pitch, roll, yaw, in degrees \n"
               "Wait( {} );  # waits {} seconds \n".format(x,y,z,wait,wait))
    file.write("DoCamera('Shutter');  # ??? \n"
               "RecenterCamera();  # recenters all three axes\n"
               "TextOut('End');  # eigentlich: TextOut( 'End !mit Umbruch!' );")
    file.close()


def printScript2():
    x,y,z,wait = read_coordinates()
    file = open("script.mcs", "w")
    file.write("UseMavlinkEmbedding( 57600, 82, 67, 71, 67 ); \n")
    file.write("SetAngle( {},{},{} );  # sets pitch, roll, yaw, in degrees \n"
               "Wait( {} );  # waits {} seconds \n".format(x, y, z, wait,wait))
    file.write("DoCamera('Shutter');  # ??? \n"
               "RecenterCamera();  # recenters all three axes\n"
               "TextOut('End');  # eigentlich: TextOut( 'End !mit Umbruch!' );")
    file.close()


def saveCoordinates(x,y,z,wait):
    file = open("coordinates.txt", "w")
    file.write(str(x)+'\n')
    file.write(str(y)+'\n')
    file.write(str(z)+'\n')
    file.write(str(wait) + '\n')
    file.close()


def automatic():
    print("class automatic")

    printScript()
    saveCoordinates(x,y,z,wait)


def coordinate(x,y,z,wait):
    print('test')


def up():
    x,y,z,wait = read_coordinates()
    x = int(x)+1
    # printScript()
    saveCoordinates(x,y,z,wait)

def left():
    x, y, z, wait = read_coordinates()
    y = int(y) + 1
    # printScript()
    saveCoordinates(x, y, z, wait)


def right():
    x,y,z, wait = read_coordinates()
    z = int(z)+1
    # printScript()
    saveCoordinates(x,y,z,wait)


def down():
    x,y,z, wait = read_coordinates()
    x = int(x)+1
    y = int(y)+1
    # printScript()
    saveCoordinates(x,y,z,wait)


# werte muessen noch an globale Variablen uebergeben werden
def wait(sec):
    # global wait
    x, y, z, wait = read_coordinates()
    wait = sec
    saveCoordinates(x,y,z,wait)
