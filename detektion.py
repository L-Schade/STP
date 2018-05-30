import os
import keyboard
# import motion_control_script


fileList = os.listdir('Matlab/Bilder')
items = len(fileList)
print(items)
# key = input()


def read_coordinates():
    if (key == '1'):
        file = open("GUI/coordinates.txt")
    elif(key == '2'):
        file = open("coordinates.txt")

    index = 0
    for line in file:
        if (index == 0):
            x = line.rstrip()
        elif (index == 1):
            y = line.rstrip()
        elif(index == 2):
            z = line.rstrip()
        index += 1;
    return x, y, z


def save_coordinates(x, y, z, name):
    file = open(name+".txt", "w")
    file.write(str(x)+'\n')
    file.write(str(y)+'\n')
    file.write(str(z)+'\n')
    file.close()


print("1: Koordinaten aus der GUI")
print("2: Koordinaten aus der Konsole")

key = input("Wählen den Modus:")

while(True):
    fileList = os.listdir('Matlab/Bilder')
    length = len(fileList)

    if(length>items):
        print("speichern der aktuellen Position:")
        items+=1

        fileList.sort(reverse=True)
        name = fileList[0]
        print(name)

        x, y, z = read_coordinates()

        if (key == '1'):
            name = "GUI/Positionen/"+name
            print(name)
            save_coordinates(x, y, z, name)
        elif (key == '2'):
            name = "Positionen/" + name
            save_coordinates(x, y, z, name)

        print("aktuelle Position gespeichert")

        #continue               # noch wieder einkommentieren
        exit()                  # dann wieder entfernen

    elif(length == items):
        print("warten ...")
        continue

    elif(keyboard.is_pressed('q')):         # funktioniert noch nicht so richtig
        print("Programm wird beendet!")
        exit()

    else:
        print("Es idt ein Fehler aufgetreten")
        exit()
