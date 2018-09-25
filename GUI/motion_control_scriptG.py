import datetime
# import motor_controlG

x = None
y = None
z = None
wait = None

# TODO
# methoden & variabeln umbennen sinnvoller


def read_position_delay():
    filename = open("position.txt")
    index = 0
    for line in filename:
        if index == 0:
            x = line.rstrip()
        elif index == 1:
            y = line.rstrip()
        elif index == 2:
            z = line.rstrip()
        elif index == 3:
            delay = line.rstrip()
        index += 1;
    return int(x), int(y), int(z), float(delay)


def read_position():
    filename = open("position.txt")
    index = 0
    for line in filename:
        if index == 0:
            x = line.rstrip()
        elif index == 1:
            y = line.rstrip()
        elif index == 2:
            z = line.rstrip()
        index += 1     # = index+1
    return int(x), int(y), int(z)


# position fits to image
def read_old_position(file_name):
    print(file_name)
    filename = open('Positionen/'+file_name+'.txt','r')
    index = 0
    for line in filename:
        if index == 0:
            x = line.rstrip()
        elif index == 1:
            y = line.rstrip()
        elif index == 2:
            z = line.rstrip()
        index += 1
    # save_position(x, y, z)
    return x, y, z


# save position in steps
def save_position(x, y, z,):
    print(y)
    filename = open("position.txt", "w")
    filename.write(str(x)+'\n')
    filename.write(str(y)+'\n')
    filename.write(str(z)+'\n')
    filename.write(str(1) + '\n')           # auto delay
    filename.write(str(datetime.datetime.now()))
    filename.close()
    print("save to file")


def save_position_delay(x, y, z, delay):
    print(y)
    filename = open("position.txt", "w")
    filename.write(str(x)+'\n')
    filename.write(str(y)+'\n')
    filename.write(str(z)+'\n')
    filename.write(str(delay) + '\n')
    filename.write(str(datetime.datetime.now()))
    filename.close()
    print("save to file")


def automatic():
    print("class automatic")
    # TODO
    # printScript()

    save_position(x, y, z)


def coordinate(x, y, wait):
    print('test')
    # neue Koordinatwen berechnen und speichern
    save_position(x, y, z)


# TODO
# Motoren ansteuern
# Berechnen wie viel Pixel ein step sind und anpassen!
def up():
    x, y, z = read_position()
    y -= 1
    save_position(x, y, z)



def left():
    x, y, z = read_position()
    new_y = int(y) + 1
    print(new_y)
    # printScript()
    save_position(x, new_y, z)


def right():
    x, y, z = read_position()
    z = int(z)+1
    # printScript()
    save_position(x, y, z)


def down():
    x, y, z = read_position()
    x = int(x)+1
    y = int(y)+1
    # printScript()
    save_position(x, y, z)


def delay(time):
    x, y, z = read_position()
    delay = float(time)
    save_position_delay(x, y, z, delay)


# def wait5():
#     x, y, z = read_position()
#     wait = 5
#     save_position(x, y, z)


def opposite(image_name):
    print(image_name)
    print("Positionen/"+image_name)
    x, y, z = read_position()
    new_position = -1 * int(x)
    print(new_position)
    # print("illegal type")

    # TODO
    # Motoren ansteuern
