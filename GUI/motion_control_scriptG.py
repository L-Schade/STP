import datetime
x = None
y = None
z = None
wait = None


def read_coordinates_wait():
    filename = open("coordinates.txt")
    index = 0
    for line in filename:
        if (index == 0):
            x = line.rstrip()
        elif (index == 1):
            y = line.rstrip()
        elif(index == 2):
            z = line.rstrip()
        elif (index == 3):
            wait = line.rstrip()
        index = index+1;
    return x, y, z, wait


def read_coordinates():
    filename = open("coordinates.txt")
    index = 0
    for line in filename:
        if (index == 0):
            x = line.rstrip()
        elif (index == 1):
            y = line.rstrip()
        elif(index == 2):
            z = line.rstrip()
        index += 1;     # = index+1
    return x, y, z


def read_old_coordinates(file_name):
    print(file_name)
    filename = open('Positionen/'+file_name+'.txt','r')
    index = 0
    for line in filename:
        if (index == 0):
            x = line.rstrip()
        elif (index == 1):
            y = line.rstrip()
        elif(index == 2):
            z = line.rstrip()
        index += 1;
    save_coordinates(x, y, z)
    return x, y, z


def printScript():
    file = open("script.mcs","w")
    file.write("UseMavlinkEmbedding( 57600, 82, 67, 71, 67 ); \n")
    file.write("SetAngle( {},{},{} );  # sets pitch, roll, yaw, in degrees \n"
               "Wait( {} );  # waits {} seconds \n".format(x, y, z, wait, wait))
    file.write("DoCamera('Shutter');  # ??? \n"
               "RecenterCamera();  # recenters all three axes\n"
               "TextOut('End');  # eigentlich: TextOut( 'End !mit Umbruch!' );")
    file.close()


def printScript1(x, y, z, wait):
    file = open("script.mcs","w")
    file.write("UseMavlinkEmbedding( 57600, 82, 67, 71, 67 ); \n")
    file.write("SetAngle( {},{},{} );  # sets pitch, roll, yaw, in degrees \n"
               "Wait( {} );  # waits {} seconds \n".format(x, y, z, wait, wait))
    file.write("DoCamera('Shutter');  # ??? \n"
               "RecenterCamera();  # recenters all three axes\n"
               "TextOut('End');  # eigentlich: TextOut( 'End !mit Umbruch!' );")
    file.close()


def printScript2():
    x, y, z, wait = read_coordinates_wait()
    file = open("script.mcs", "w")
    file.write("UseMavlinkEmbedding( 57600, 82, 67, 71, 67 ); \n")
    file.write("SetAngle( {},{},{} );  # sets pitch, roll, yaw, in degrees \n"
               "Wait( {} );  # waits {} seconds \n".format(x, y, z, wait, wait))
    file.write("DoCamera('Shutter');  # ??? \n"
               "RecenterCamera();  # recenters all three axes\n"
               "TextOut('End');  # eigentlich: TextOut( 'End !mit Umbruch!' );")
    file.close()


def save_coordinates_wait(x, y, z, wait):
    filename= open("coordinates.txt", "w")
    filename.write(str(x)+'\n')
    filename.write(str(y)+'\n')
    filename.write(str(z)+'\n')
    filename.write(str(wait) + '\n')
    filename.write(str(datetime.datetime.now()))
    filename.close()


def save_coordinates(x, y, z,):
    filename = open("coordinates.txt", "w")
    filename.write(str(x)+'\n')
    filename.write(str(y)+'\n')
    filename.write(str(z)+'\n')
    filename.write(str(datetime.datetime.now()))
    filename.close()
    print("save to file")


def automatic():
    print("class automatic")

    printScript()
    # save_coordinates_wait(x,y,z,wait)
    save_coordinates(x, y, z)


def coordinate(x, y, z, wait):
    print('test')


def up(blocked):
    if (blocked == False):
        x, y, z = read_coordinates()
        x = int(x)+1
        # printScript()
        save_coordinates(x, y, z)
    else:
        print("Motoren sind gesperrt!")


def left(blocked):
    if (blocked == False):
        x, y, z = read_coordinates()
        y = int(y) + 1
        # printScript()
        save_coordinates(x, y, z)
    else:
        print("Motoren sind gesperrt!")


def right(blocked):
    if(blocked == False):
        x, y, z = read_coordinates()
        z = int(z)+1
        # printScript()
        save_coordinates(x, y, z)
    else:
        print("Motoren sind gesperrt!")


def down(blocked):
    if (blocked == False):
        x, y, z = read_coordinates()
        x = int(x)+1
        y = int(y)+1
        # printScript()
        save_coordinates(x, y, z)
    else:
        print("Motoren sind gesperrt!")


def wait(time):
    x, y, z = read_coordinates()
    wait = int(time)
    save_coordinates(x, y, z)


def wait5():
    x, y, z = read_coordinates()
    wait = 5
    save_coordinates(x, y, z)


def opposite(image_name):
    print(image_name)
    print("Positionen/"+image_name)
    x, y, z = read_coordinates()
    new_position = -1 * int(x)
    print(new_position)
    # print("illegal type")


