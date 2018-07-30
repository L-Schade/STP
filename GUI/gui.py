from Tkinter import *   # python 2.7
# from  tkinter import *  # 3.5
import tkMessageBox
from PIL import Image, ImageTk
import motion_control_scriptG
import distance_calculator
# import functionsG
import imagesG

fields = 'x-coordinate', 'y-coordinate', 'z-coordinate', 'time to wait'
fields_angle = 'pitch', 'roll', 'yaw', 'time to wait'
images = []
image = None            # aktuelles Bild
image_na = None       # name aktuelles Bild (ohne Dateiformat)
imageStart = None
imageAutomatic = None
imageNavigate = None
index = None         # index des ausgewaehlten Bildes
text = "Ausgabe"
x = None
y = None
center = None

bu1_blocked = False       # Motoren sind frei
bu2_blocked = False       # Motoren koennen bewegt werden


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

    # distance = distance_calculator.distance(center, point)
    # text = "Abstand von {} zum Mittelpunkt: {}".format(point, distance)
    dist = distance_calculator.dist(center, point)
    text = "Abstand von {} zum Mittelpunkt: x-Abstand: {} y-Abstand: {}".format(point, dist[0], dist[1])
    output_label()


# event function
def button_click():
    hide_automatic_windows()
    hide_coordinate_buttons()
    hide_navigate_buttons()
    hide_images_buttons()
    labelImg.place_forget()

    # buttonModeTest.place_forget()
    read_coordinates('alte Position:')
    output_label()

    x, y, z = motion_control_scriptG.read_old_coordinates(image_na)
    print(x, y, z)
    if(bu2_blocked == False):
        print("test")
        # nur noch an diese Position fahren

    else:
        print("Motoren sind gesperrt")


def button1_click():
    hide_coordinate_buttons()
    hide_navigate_buttons()
    hide_images_buttons()
    output_lab.place_forget()
    labelImg.place_forget()

    # click_event
    frame.place(x=200, y=75, width=600, height=350)
    # frame.bind("<Button-1>", click)

    labelImg1.config(image=imageAutomatic)
    labelImg1.place(x=50, y=50, width=500, height=250)
    labelImg1.Image = imageNavigate
    labelImg1.bind("<Button-1>", click)

    global center
    center = distance_calculator.center(500, 250)
    print(center)

    # global text
    # text = "Abstand von {} zum Mittelpunkt: {}".format(point,dist)
    # output_label()

    # Funktion zum Umrechnen noch ein bauen


def button2_click():
    hide_automatic_windows()
    hide_navigate_buttons()
    hide_images_buttons()
    output_lab.place_forget()
    labelImg.place_forget()
    # output_lab.place_forget()
    # toolbar_yy.place(x=150, y=0, width=150, height=1000)
    buttonMode21.place(x=175, y=100, width=125, height=20)
    buttonMode22.place(x=175, y=140, width=125, height=20)


def button21_click():
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
        global bu2_blocked
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

                if(bu2_blocked == False):
                    # noch Funktion zum "Umrechnen" einbauen
                    motion_control_scriptG.printScript1(x, y, z, wait)
                    motion_control_scriptG.save_coordinates_wait(x, y, z, wait)

                    read_coordinates('neue Koordinaten:')
                    output_label()

                else:
                    print("Motoren sind gesperrt")
                    output("Motoren sind gesperrt!")
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
        b1 = Button(root, text='Daten verschicken',command=(lambda e=ents: fetch(e))) # command=motion_control_scriptG.printScript()
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(root, text='quit', command=root.destroy)
        b2.pack(side=LEFT, padx=5, pady=5)
        root.mainloop()


def button22_click():
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

                if (bu2_blocked == False):
                    # noch Funktion zum "Umrechnen" einbauen
                    motion_control_scriptG.printScript1(x, y, z, wait)
                    motion_control_scriptG.save_coordinates_wait(x, y, z, wait)

                    read_coordinates('neue Koordinaten:')
                    output_label()

                else:
                    print("Motoren sind gesperrt")
                    output("Motoren sind gesperrt!")
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
        b1 = Button(root_angle, text='Daten verschicken',command=(lambda e=ents: fetch(e))) # command=motion_control_scriptG.printScript()
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(root_angle, text='quit', command=root_angle.destroy)
        b2.pack(side=LEFT, padx=5, pady=5)
        root_angle.mainloop()


def button3_click():
    hide_automatic_windows()
    hide_coordinate_buttons()
    hide_images_buttons()
    labelImg.place_forget()
    # motion_control_scriptG.coordinate()

    read_coordinates('alte Daten:')
    output_label()

    button1.place(x=250, y=100, width=100, height=20)
    button2.place(x=175, y=140, width=100, height=20)
    button3.place(x=325, y=140, width=100, height=20)
    button4.place(x=250, y=180, width=100, height=20)
    button5.place(x=235, y=230, width=40, height=20)
    button6.place(x=325, y=230, width=40, height=20)
    button7.place(x=235, y=290, width=130, height=20)
    button8.place(x=585, y=325, width=180, height=20)
    labelImg2.config(image=imageNavigate)
    labelImg2.place(x=500, y=110, width=350, height= 190)

    # read_coordinates('')
    # output_label()


def button4_click():
    labelImg.place_forget()
    hide_automatic_windows()
    hide_navigate_buttons()
    hide_coordinate_buttons()
    output_lab.place_forget()

    print("lade Bilder")
    output('lade Bilder...')
    output_label_img()

    # scrollbar.pack(side=RIGHT, fill=Y)
    # buttonBox.place(x=150, y=275, width=750, height=6800)
    # scrollbar.config(command=buttonBox.yview)

    buttonImg1.place(x=200, y=300, width=175, height=100)
    buttonImg2.place(x=437.5, y=300, width=175, height=100)
    buttonImg3.place(x=675, y=300, width=175, height=100)
    buttonImg4.place(x=200, y=425, width=175, height=100)
    buttonImg5.place(x=437.5, y=425, width=175, height=100)
    buttonImg6.place(x=675, y=425, width=175, height=100)
    buttonImg7.place(x=200, y=550, width=175, height=100)
    buttonImg8.place(x=437.5, y=550, width=175, height=100)
    buttonImg9.place(x=675, y=550, width=175, height=100)


# load another image
def button_click_image(index):
    global image, image_na
    image_names = imagesG.list_images(12)
    image = load_image(image_names[index])
    reload_images()

    print("lade passende Position...")
    image_name = image_names[index]
    image_name = image_name.split(".")
    image_na = image_name[0]
    print(image_na)
    load_position(image_na)
    output("Daten zu Bild: " + image_na + " geladen")
    output_label_img()


# output for navigate, coordinate, automatic & letzte Position
def output_label():
    # output_lab = Message(master=frameGui)
    output_lab.config(text=text, bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
    output_lab.place(x=200, y=450, width=650, height=250)


# output for the side image
def output_label_img():
    # output_lab = Message(master=frameGui)
    output_lab.config(text=text, bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
    output_lab.place(x=200, y=100, width=650, height=150)


# set new output text
def output(data):
    global text
    text = data


# load position addicted to image
def read_coordinates(data):
    global image_na
    print(image_na)
    # x, y, z, wait = motion_control_scriptG.read_coordinates()
    x, y, z = load_position(image_na)
    wait = str(3)
    global text
    if(data == ''):
        text = "x-Koordinate: " + x + "\n"  \
                                 "y-Koordinate: " + y + "\n" \
                                                     "z-Koordinate " + z + "\n" \
                                                                       "time to wait: " + wait + ""
    elif (data == 'new angle position:'):
        text = "pitch: " + x + "\n" \
                                      "roll: " + y + "\n" \
                                                             "yaw: " + z + "\n" \
                                                                                    "time to wait: " + wait + ""
    else:
        text = ""+data+"\n" \
               "x-Koordinate: " + x + "\n"  \
                                          "y-Koordinate: " + y + "\n" \
                                                             "z-Koordinate: " + z + "\n" \
                                                                               "time to wait: " + wait +""


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
    button8.place_forget()
    labelImg2.place_forget()


def hide_automatic_windows():
    frame.place_forget()
    labelImg1.place_forget()


def hide_coordinate_buttons():
    buttonMode21.place_forget()
    buttonMode22.place_forget()


def hide_images_buttons():
    buttonImg1.place_forget()
    buttonImg2.place_forget()
    buttonImg3.place_forget()
    buttonImg4.place_forget()
    buttonImg5.place_forget()
    buttonImg6.place_forget()
    buttonImg7.place_forget()
    buttonImg8.place_forget()
    buttonImg9.place_forget()


# fuer board wichtig gewesen
def print_script():
    global bu2_blocked
    if(bu2_blocked == False):
        motion_control_scriptG.printScript2()
        print('print script')
        read_coordinates('new coordinates')
        output_label()
    else:
        output("Motoren sind gesperrt!")
        output_label()


# reload position
def update_coordinates():
    read_coordinates('new coordinates')
    output_label()


# load image from file
def load_image(name):
    # img = ImageTk.PhotoImage(Image.open(name))
    img = Image.open("../Matlab/Bilder/" + name)
    return img


# load image from file and add to list
def load_images(name):          # buttons
    # img = ImageTk.PhotoImage(Image.open(name))
    img = Image.open("../Matlab/Bilder/"+name)
    img = resized_image(img, 175, 100)
    images.append(img)
    return img


# adapt imgae size
def resized_image(img, h, w):
    resized = img.resize((h, w), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(resized)
    return image


#
def get_latest_images():
    global image
    list_images(6)
    image = load_image(imagesG.latest_image())


# load the latest images, the number depend on maxi
def list_images(maxi):
    image_names = imagesG.list_images(maxi)
    print(image_names)
    for image in image_names:
        load_images(image)


# load new image for gui
def reload_images():
    global image, imageStart, imageAutomatic, imageNavigate
    imageStart = resized_image(image, 300, 150)  # latest image
    imageAutomatic = resized_image(image, 500, 250)
    imageNavigate = resized_image(image, 350, 190)


# load position for ...
def load_position(name):
    # file_name = 'Positionen/'+name+'.txt'
    # print(file_name)
    x, y, z = motion_control_scriptG.read_old_coordinates(name)
    # motion_control_scriptG.save_coordinates_without_wait(x, y, z)        Bildposition auf aktuelle Koordinaten setzen
    print(x, y, z)
    return x, y, z

    # motion_control_scriptG.printScript1(x, y, z, 3)
    # motion_control_scriptG.save_coordinates(x, y, z, 3)


#
def warning():
    if __name__ == '__main__':
        root_angle = Tk()
        root_angle.title('Eingabe der Werte')

        i = Image.open("warning1.jpg")
        photo = ImageTk.PhotoImage(i)
        img = Label(master=frameGui, image=photo)     # funktioniert nur mit master=frameGui
        img.place(x=150, y=325, width=750, height=100)
        # img.pack(fill=X, pady=5)

        # tkMessageBox.showwarning("Warning", "Sind sie sich sicher das nichts im Weg ist und sie in die gewuenschte Richting verfahren koennen?")
        text = Label(root_angle, text="Sind sie sich sicher das nichts im Weg ist \n & sie in die gewuenschte Richting verfahren koennen?", bg="red", fg="white")
        text.pack(fill=X, pady=5)
        b1 = Button(root_angle, text='auf die andere Seite fahren',command=lambda: opposite(root_angle, img)) # command=motion_control_scriptG.printScript()
        # b1 = Button(tkMessageBox, text='auf die andere Seite fahren', command=motion_control_scriptG.opposite())
        # b1.place(x=10, y=30, width=20, heigth=20)
        b1.pack(fill=X, pady=5)
        # b2 = Button(root_angle, text='Abbrechen', command=root_angle.destroy)
        b2 = Button(root_angle, text='Abbrechen', command=lambda: close_warning(root_angle, img))
        # b2.place(x=40, y=30, width=20, heigth=20)
        b2.pack(fill=X, pady=5)
        root_angle.mainloop()


#
def opposite(root_angle, img):
    motion_control_scriptG.opposite(image_na + '.txt')
    root_angle.destroy()
    img.place_forget()


#
def close_warning(root_angle, img):
    root_angle.destroy()
    img.place_forget()


# hold position
def bu1_onclick():
    global bu1_blocked
    if(bu1_blocked == False):
        bu1['bg'] = '#B40431'
        bu1['fg'] = 'white'
        bu1['text'] = 'Position \nwird gehalten'
        bu1_blocked = True
        print(bu1_blocked)
    elif(bu1_blocked == True):
        bu1['bg'] = '#BDBDBD'
        bu1['fg'] = 'black'
        bu1['text'] = 'Motoren \nhalten'
        bu1_blocked = False
        print(bu1_blocked)


# blocked motor
def bu2_onclick():
    global bu2_blocked
    if(bu2_blocked == False):
        bu2['bg'] = '#B40431'
        bu2_blocked = True
        bu2['fg'] = 'white'
        bu2['text'] = 'Motoren \ngesperrt'
        print(bu2_blocked)
    elif(bu2_blocked == True):
        bu2['bg'] = '#BDBDBD'
        bu2['fg'] = 'black'
        bu2['text'] = 'Motoren \nsperren'
        bu2_blocked = False
        print(bu2_blocked)

        # TODO
        output("Motoren sind wieder freigegeben!")
        output_label()
        # geht so nur bei navigate, coordinate, automatic & letzte Position


def get_blocked(ind):
    global bu2_blocked
    if(bu2_blocked == False):
        if(ind == 0):
            motion_control_scriptG.up(bu2_blocked)
        elif(ind == 1):
            motion_control_scriptG.left(bu2_blocked)
        elif (ind == 2):
            motion_control_scriptG.right(bu2_blocked)
        elif (ind == 3):
            motion_control_scriptG.down(bu2_blocked)
        # print(bu2_blocked)
    else:
        print(index)
        output("Motoren sind gesperrt!")
        output_label()


# create the window
tk_fenster = Tk()
tk_fenster.title('GUI')
tk_fenster.geometry('1000x1000')

# background
frameGui = Frame(master=tk_fenster, bg='#A9BCF5')
frameGui.place(width=1000, height=950)    # x=5, y=5 border

# toolbar
toolbar_y = Frame(tk_fenster, bg='#084B8A')
# toolbar.pack(side=TOP, fill=X, padx=10)
toolbar_y.place(x=0, y=0, width=150, height=1000)
toolbar_yy = Frame(master=tk_fenster, bg='#045FB4')
# toolbar.pack(side=TOP, fill=X, padx=10)
toolbar_yyy = Frame(tk_fenster, bg='#084B8A')
# toolbar.pack(side=TOP, fill=X, padx=10)
toolbar_yyy.place(x=900, y=0, width=100, height=1000)

# scrollbar
# scrollbar = Scrollbar(tk_fenster)
# buttonBox = Listbox(tk_fenster, yscrollcommand = scrollbar.set )

# label
my_label = Label(master=frameGui, text="Automatische Werkzeug-Kontakt Detektion", bg='white')    # bg='#BDBDBD'
my_label.place(x=325, y=20, width=350, height=30)

# click_event
frame = Frame(master=frameGui, bg='white')

# Images
list_images(9)
image_na = imagesG.latest_image()
image = load_image(image_na)
image_na = image_na.split('.')
image_na = image_na[0]
reload_images()
im = load_image(imagesG.latest_image())

# Label for images
labelImg = Label(master=frameGui, image=imageStart, bg='white', state=NORMAL)
labelImg.place(x=325, y=100, width=350, height=200)
labelImg1 = Label(master=frame, bg='white')           # automatic
labelImg2 = Label(master=frameGui, bg='white')        # navigate

# Button
buttonMode = Button(master=toolbar_y, text='letzte Position', command=button_click)
buttonMode.place(x=25, y=100, width=100, height=20)
buttonMode1 = Button(master=toolbar_y, text='automatisch', command=button1_click)
buttonMode1.place(x=25, y=140, width=100, height=20)
buttonMode2 = Button(master=toolbar_y, text='Koordinaten', command=button2_click)
buttonMode2.place(x=25, y=180, width=100, height=20)
buttonMode21 = Button(master=frameGui, text='Koordinaten: x,y,z', command=button21_click)
buttonMode22 = Button(master=frameGui, text='Winkel', command=button22_click)
buttonMode3 = Button(master=toolbar_y, text='Navigation', command=button3_click)
buttonMode3.place(x=25, y=220, width=100, height=20)
buttonMode4 = Button(master=toolbar_y, text='Bilder', command=button4_click)
buttonMode4.place(x=25, y=260, width=100, height=20)
# button1 = Button(master=frameGui, text='oben', command=lambda: motion_control_scriptG.up(bu2_blocked))
button1 = Button(master=frameGui, text='links', command=lambda: get_blocked(0))
# button2 = Button(master=frameGui, text='links', command=lambda: motion_control_scriptG.left(bu2_blocked))
button2 = Button(master=frameGui, text='links', command=lambda: get_blocked(1))
# button3 = Button(master=frameGui, text='rechts', command=lambda: motion_control_scriptG.right(bu2_blocked))
button3 = Button(master=frameGui, text='links', command=lambda: get_blocked(2))
#button4 = Button(master=frameGui, text='unten', command=lambda: motion_control_scriptG.down(bu2_blocked))
button4 = Button(master=frameGui, text='links', command=lambda: get_blocked(3))
button5 = Button(master=frameGui, text='3sec', command=lambda: motion_control_scriptG.wait(3))
button6 = Button(master=frameGui, text='5sec', command=lambda: motion_control_scriptG.wait(5))
button7 = Button(master=frameGui, text='Daten verschicken', command=print_script)
button8 = Button(master=frameGui, text='zur anderen Seite fahren', command= warning)
# vlt die Anzahl noch variierbar machen?
buttonImg1 = Button(master=frameGui, image=images[0], command=lambda: button_click_image(0))
buttonImg2 = Button(master=frameGui, image=images[1], command=lambda: button_click_image(1))
buttonImg3 = Button(master=frameGui, image=images[2], command=lambda: button_click_image(2))
buttonImg4 = Button(master=frameGui, image=images[3], command=lambda: button_click_image(3))
buttonImg5 = Button(master=frameGui, image=images[4], command=lambda: button_click_image(4))
buttonImg6 = Button(master=frameGui, image=images[5], command=lambda: button_click_image(5))
buttonImg7 = Button(master=frameGui, image=images[6], command=lambda: button_click_image(6))
buttonImg8 = Button(master=frameGui, image=images[7], command=lambda: button_click_image(7))
buttonImg9 = Button(master=frameGui, image=images[8], command=lambda: button_click_image(8))
# buttonModeTest = Button(master=frameGui, text='test', command=output_label)
# buttonModeTest.place(x=50, y=400, width=100, height=20)
exit_button = Button(tk_fenster, text="Beenden", command=tk_fenster.destroy, bg='#BDBDBD')
exit_button.place(x=910, y=20, width=80, height=20)
refresh_button = Button(tk_fenster, text=" Bilder \n neu laden", command=lambda: get_latest_images(), bg='#BDBDBD')
refresh_button.place(x=910, y=60, width=80, height=40)
bu1 = Button(tk_fenster, text="Motoren \n halten", command=lambda: bu1_onclick(), bg='#BDBDBD')
bu1.place(x=905, y=600, width=90, height=40)
bu2 = Button(tk_fenster, text="Motoren \n sperren", command=lambda: bu2_onclick(), bg='#BDBDBD')
bu2.place(x=905, y=660, width=90, height=40)

# coordinate
eingabefeld = Entry(tk_fenster, bd=5, width=45)
text_label = Label(tk_fenster)

# output
output_lab = Message(master=frameGui)

# activation the window
tk_fenster.mainloop()
