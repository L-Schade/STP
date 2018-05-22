from tkinter import *   # python 2.7 Tkinter
from PIL import Image, ImageTk
from random import randint
import sys
import os
# import "/home/lisa/Dokumente/Uni/5_Semester/Automatische_Werkzeug-Kontakt_Detektion/STP/GUI/motion_control_scriptG""
import motion_control_scriptG
# import functionsG
import edge_detectionG
import distance_calculator



fields = 'x-coordinate', 'y-coordinate', 'z-coordinate', 'time to wait'
fields_angle = 'pitch', 'roll', 'yaw', 'time to wait'
text = "Ausgabe"
x = None
y = None
center = None


# click_event
def click(event):
    global x, y, text, center

    print("left")
    print("clicked at", event.x, event.y)

    x = event.x
    y = event.y
    point = [x, y]
    # text = "Punkt: ({},{})".format(x,y)
    # output_label()

    # motion_control_scriptG.automatic()

    distance = distance_calculator.distance(center, point)
    dist = distance_calculator.dist(center, point)
    # text = "Abstand von {} zum Mittelpunkt: {}".format(point, distance)
    text = "Abstand von {} zum Mittelpunkt: x-Abstand: {} y-Abstand: {}".format(point, dist[0], dist[1])
    output_label()


# event function
def buttonClick():
    hide_navigate_buttons()
    hide_automatic_windows()
    hide_coordinate_buttons()
    labelImg.place_forget()
    # buttonModeTest.place_forget()
    read_coordinates('old position:')
    output_label()


def button1Click():
    hide_navigate_buttons()
    hide_coordinate_buttons()
    labelImg.place_forget()

    # click_event
    frame.place(x=200, y=75, width=600, height=350)
    # frame.bind("<Button-1>", click)

    labelImg1.place(x=50, y=50, width=500, height=250)
    labelImg1.bind("<Button-1>", click)

    global center
    center = distance_calculator.center(500,250)
    print(center)

    # motion_control_scriptG.automatic()
    # point, dist = edge_detectionG.execute("../Bilder_BSP/filter1.jpg")

    # global text
    # text = "Abstand von {} zum Mittelpunkt: {}".format(point,dist)
    # output_label()


def button2Click():
    hide_navigate_buttons()
    hide_automatic_windows()
    labelImg.place_forget()
    # output_lab.place_forget()
    # toolbar_yy.place(x=150, y=0, width=150, height=1000)
    buttonMode21.place(x=175, y=100, width=125, height=20)
    buttonMode22.place(x=175, y=140, width=125, height=20)


def button21click():
    hide_coordinate_buttons()
    # panel
    # buttonAction = Button(master=frameGui, text='ENTER', command=button_action)
    # buttonAction.place(x=625, y=200, width=100, height=20)
    # # dialog box
    # eingabefeld.place(x=500, y=150 ,width=350, height=30)
    # text_label.place(x=500, y=250,width=350,height=25)
    # # motion_control_scriptG.navigate()

    # def button_action():
    #     entry_text = eingabefeld.get()
    #     if (entry_text == ""):
    #         text_label.config(text="undefined key")
    #     else:
    #         text = functionsG.input(entry_text)
    #         text_label.config(text=text)


    # coordinates, extra window
    def fetch(entries):
        index = 0
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            print('%s: "%s"' % (field, text))
            if(index == 0):
                x = entry[1].get()
                index = index+1
            elif (index == 1):
                y = entry[1].get()
                index = index + 1
            elif(index == 2):
                z = entry[1].get()
                index = index+1
            elif(index == 3):
                wait = entry[1].get()
                index = 0
                # noch Funktion zum "Umrechnen" einbauen
                motion_control_scriptG.printScript1(x,y,z,wait)
                motion_control_scriptG.saveCoordinates(x,y,z,wait)
                read_coordinates('new coordinates:')
                output_label()


    def makeform(root, fields):
        entries = []
        for field in fields:
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((field, ent))
        return entries


    if __name__ == '__main__':
        root = Tk()
        root.title('Eingabe der Werte')
        ents = makeform(root, fields)
        root.bind('<Return>', (lambda event, e=ents: fetch(e)))
        b1 = Button(root, text='print script',command=(lambda e=ents: fetch(e))) # command=motion_control_scriptG.printScript()
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(root, text='quit', command=root.destroy)
        b2.pack(side=LEFT, padx=5, pady=5)
        root.mainloop()


def button22click():
    hide_coordinate_buttons()

    def fetch(entries):
        index = 0
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            print('%s: "%s"' % (field, text))
            if(index == 0):
                x = entry[1].get()
                index = index+1
            elif (index == 1):
                y = entry[1].get()
                index = index + 1
            elif (index == 2):
                z = entry[1].get()
                index = index + 1
            elif(index == 3):
                wait = entry[1].get()
                index = 0
                motion_control_scriptG.printScript1(x,y,z,wait)
                motion_control_scriptG.saveCoordinates(x,y,z,wait)
                read_coordinates('new angle position:')
                output_label()


    def makeform(root, fields):
        entries = []
        for field in fields_angle:
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((field, ent))
        return entries


    if __name__ == '__main__':
        root_angle = Tk()
        root_angle.title('Eingabe der Werte')
        ents = makeform(root_angle, fields)
        root_angle.bind('<Return>', (lambda event, e=ents: fetch(e)))
        b1 = Button(root_angle, text='print script',command=(lambda e=ents: fetch(e))) # command=motion_control_scriptG.printScript()
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(root_angle, text='quit', command=root_angle.destroy)
        b2.pack(side=LEFT, padx=5, pady=5)
        root_angle.mainloop()


def button3Click():
    hide_automatic_windows()
    hide_coordinate_buttons()
    # motion_control_scriptG.coordinate()
    read_coordinates('old datas:')
    output_label()
    button1.place(x=500, y=130, width=100, height=20)
    button2.place(x=500, y=170, width=100, height=20)
    button3.place(x=500, y=210, width=100, height=20)
    button4.place(x=500, y=250, width=100, height=20)
    button5.place(x=505, y=290, width=40, height=20)
    button6.place(x=555, y=290, width=40, height=20)
    button7.place(x=500, y=330, width=100, height=20)
    output_label()
    labelImg.place_forget()


def output_label():
    output_lab = Message(master=frameGui, text=text)
    output_lab.config(bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
    output_lab.place(x=200, y=450, width=650, height=250)


# def print(data):
    # global text
    # text = data


def hide_navigate_buttons():
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    button5.place_forget()
    button6.place_forget()
    button7.place_forget()


def hide_automatic_windows():
    frame.place_forget()
    labelImg1.place_forget()


def hide_coordinate_buttons():
    buttonMode21.place_forget()
    buttonMode22.place_forget()


def read_coordinates(data):
    x,y,z,wait = motion_control_scriptG.read_coordinates()
    global text
    if(data == ''):
        text = "x-coordinate: "+x+"\n"  \
                                 "y-coordinate: "+y+"\n" \
                                                     "z-coordinate: "+z+"\n" \
                                                                       "time to wait: "+wait+""
    elif (data == 'new angle position:'):
        text = "pitch: " + x + "\n" \
                                      "roll: " + y + "\n" \
                                                             "yaw: " + z + "\n" \
                                                                                    "time to wait: " + wait + ""
    else:
        text = ""+data+"\n" \
               "x-coordinate: " + x + "\n"  \
                                          "y-coordinate: " + y + "\n" \
                                                             "z-coordinate: " + z + "\n" \
                                                                               "time to wait: " + wait+""


def automatic_output(data):
    global text
    text = data


def test():
    motion_control_scriptG.printScript2(),
    print('print script')
    read_coordinates('new coordinates')
    output_label()


def load_image():
    img = edge_detectionG.edges(edge_detectionG.loadImage("../Bilder_BSP/filter1.jpg"))
    return img


# create the window
tkFenster = Tk()
tkFenster.title('GUI')
tkFenster.geometry('1000x1000')


# background
frameGui = Frame(master=tkFenster, bg='#A9BCF5')
frameGui.place( width=1000, height=1000)    # x=5, y=5 border


# toolbar
toolbar_y = Frame(tkFenster, bg='#084B8A')
# toolbar.pack(side=TOP, fill=X, padx=10)
toolbar_y.place(x=0, y=0, width=150, height=1000)
toolbar_yy = Frame(master=tkFenster, bg='#045FB4')
# toolbar.pack(side=TOP, fill=X, padx=10)
toolbar_yyy = Frame(tkFenster, bg='#084B8A')
# toolbar.pack(side=TOP, fill=X, padx=10)
toolbar_yyy.place(x=900, y=0, width=100, height=1000)

# label
my_label = Label(master=frameGui, text="Automatische Werkzeug-Kontakt Detektion", bg='white') # bg='#BDBDBD'
my_label.place(x=325, y=20, width=350, height=30)

# click_event
frame = Frame(master=frameGui, bg='white')

# Images
image1 = ImageTk.PhotoImage(Image.open("../Bilder_BSP/filter1.jpg"))
image2 = ImageTk.PhotoImage(Image.open("../Matlab/bild3.png"))
# Label for images
labelImg = Label(master=frameGui, image=image1, bg='white')
labelImg.place(x=325, y=100, width=350, height=200)
# labelImg1 = Label(master=frameGui, image=edge_detectionG.edges(edge_detectionG.loadImage("../Bilder_BSP/filter1.jpg")
#                                                                  , bg='white')
labelImg1 = Label(master=frame, image=image2, bg='white')

# Button
buttonMode = Button(master=toolbar_y, text='start', command=buttonClick)
buttonMode.place(x=25, y=100, width=100, height=20)
buttonMode1 = Button(master=toolbar_y, text='automatisch', command=button1Click)
buttonMode1.place(x=25, y=140, width=100, height=20)
buttonMode2 = Button(master=toolbar_y, text='Koordinaten', command=button2Click)
buttonMode2.place(x=25, y=180, width=100, height=20)
buttonMode21 = Button(master=frameGui, text='Koordinaten: x,y,z', command=button21click)
buttonMode22 = Button(master=frameGui, text='Winkel', command=button22click)
buttonMode3 = Button(master=toolbar_y, text='Navigation', command=button3Click)
buttonMode3.place(x=25, y=220, width=100, height=20)
button1 = Button(master=frameGui, text='oben', command=motion_control_scriptG.up)
button2 = Button(master=frameGui, text='links', command=motion_control_scriptG.left)
button3 = Button(master=frameGui, text='rechts', command=motion_control_scriptG.right)
button4 = Button(master=frameGui, text='unten', command=motion_control_scriptG.down)
button5 = Button(master=frameGui, text='3sec', command=motion_control_scriptG.wait3)
button6 = Button(master=frameGui, text='5sec', command=motion_control_scriptG.wait5)
# button7 = Button(master=frameGui, text='print script', command=(motion_control_scriptG.printScript2(),
#                                                                     print('print script'))) # funktioniert nicht
button7 = Button(master=frameGui, text='print script', command=test)
# buttonModeTest = Button(master=frameGui, text='test', command=output_label)
# buttonModeTest.place(x=50, y=400, width=100, height=20)
exit_button = Button(tkFenster, text="Beenden", command=tkFenster.destroy, bg='#BDBDBD')
exit_button.place(x=920, y=20, width=60, height=20)

# coordinate
eingabefeld = Entry(tkFenster, bd=5, width=45)
text_label = Label(tkFenster)

# output
# output_lab = Message(master=frameGui, text=text)

# activation the window
tkFenster.mainloop()
