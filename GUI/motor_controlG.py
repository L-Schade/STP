import datetime
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
        index += 1;
    return x, y, z, wait


def save_coordinates(x, y, z, wait):
    file = open("coordinates.txt", "w")
    file.write(str(x)+'\n')
    file.write(str(y)+'\n')
    file.write(str(z)+'\n')
    file.write(str(wait) + '\n')
    file.write(str(datetime.datetime.now()))
    file.close()


def automatic():
    print("class automatic")

    save_coordinates(x, y, z, wait)


def coordinate(x, y, z, wait):
    print('test')


def up():
    x, y, z, wait = read_coordinates()
    x = int(x)+1

    save_coordinates(x, y, z, wait)


def left():
    x, y, z, wait = read_coordinates()
    y = int(y) + 1

    save_coordinates(x, y, z, wait)


def right():
    x, y, z, wait = read_coordinates()
    z = int(z)+1

    save_coordinates(x, y, z, wait)


def down():
    x, y, z, wait = read_coordinates()
    x = int(x)+1
    y = int(y)+1

    save_coordinates(x, y, z, wait)


def wait3():
    x, y, z, wait = read_coordinates()
    wait = 3
    save_coordinates(x, y, z, wait)


def wait5():
    x, y, z, wait = read_coordinates()
    wait = 5
    save_coordinates(x, y, z, wait)