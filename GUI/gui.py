from Tkinter import *   # python 2.7
# from  tkinter import *  # 3.5
import tkMessageBox
from PIL import Image, ImageTk
import time
import motion_control_scriptG
import distance_calculator
# import functionsG
import imagesG
import detection
import cv2


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
def click1(event):
    global x, y, text, center, bu2_blocked
    if not bu2_blocked:         # False
        # print("left")
        print("clicked at", event.x, event.y)

        x = event.x
        y = event.y
        point = [x, y]
        # text = "Punkt: ({},{})".format(x,y)

        # motion_control_scriptG.automatic()

        # distance = distance_calculator.distance(center, point)
        # text = "Abstand von {} zum Mittelpunkt: {}".format(point, distance)
        dist = distance_calculator.dist(center, point)
        text = "Abstand von {} zum Mittelpunkt:\n" \
               "x-Abstand: {} \n" \
               "y-Abstand: {}".format(point, dist[0], dist[1])

        output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'), aspect=800)    #
        output_lab.place(x=225, y=475, width=600)

        # TODO
        # gewuenschte Position berechnen
        # Motoren ansteuern
        # Bildgroesse beachten

    else:
        output("Motoren sind gesperrt!")
        output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
        output_lab.place(x=225, y=450, width=600)
        stop()


def click2(event):
    global x, y, text, center, bu2_blocked
    if not bu2_blocked:  # False
        print("clicked at", event.x, event.y)
        x = event.x
        y = event.y

        img = cv2.imread("../Matlab/Bilder/" + image_na + ".png")
        dim = (500, 250)
        # resize image
        resized = cv2.resize(img, dim)
        print(resized[y, x])

        # TODO
        # pixel Farbe bestimmen
        color = resized[y,x]
        # color = [33, 33, 33]

        img_name = "../Matlab/Bilder/" + image_na + ".png"
        x_dist, y_dist = detection.algorithm_(img_name, color, x, y)
        # x_dist, y_dist = detection.algorithm_('schwarz_weiss.jpeg', color, x, y)  # zum Testen
        # print(x_dist, y_dist)

        # TODO
        # gewuenschte Position berechnen
        # Motoren ansteuern
        # Bildgroesse beachten

    else:
        output("Motoren sind gesperrt!")
        output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
        output_lab.place(x=600, y=460, width=170, height=150)
        stop()


# event function
# latest position
def button_click():
    hide_focus_windows()
    hide_tracking_buttons()
    hide_coordinate_buttons()
    hide_navigate_buttons()
    hide_images_buttons()
    labelImg.place_forget()
    label_img_coord1.place_forget()
    label_img_coord2.place_forget()

    # buttonModeTest.place_forget()

    # Image appropriate to the latest Position
    frame.place(x=225, y=75, width=600, height=350)
    labelImg1.config(image=imageAutomatic)
    labelImg1.place(x=50, y=50, width=500, height=250)
    labelImg1.Image = imageNavigate

    # output("Motoren fahren an die zuletzt aufgenommene Position")
    # output_lab = output_label_img()

    read_coordinates('alte Position:')
    output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
    output_lab.place(x=225, y=450, width=600, height=200)

    # x, y, z = motion_control_scriptG.read_old_coordinates(image_na)
    old_coord = motion_control_scriptG.read_old_coordinates(image_na)
    x_coord = old_coord[0]
    y_coord = old_coord[1]
    z_coord = old_coord[2]
    print(x_coord, y_coord, z_coord)
    if not bu2_blocked:     # False
        print("test")
        # TODO
        # nur noch an diese Position fahren
        # Motoren ansteuern

    else:
        print("Motoren sind gesperrt")
        output("Motoren sind gesperrt")
        output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
        output_lab.place(x=225, y=450, width=600, height=200)
        stop()


# automatic modes
# new focus
def button11_click():
    hide_tracking_buttons()
    hide_coordinate_buttons()
    hide_navigate_buttons()
    hide_images_buttons()
    output_lab.place_forget()
    labelImg.place_forget()
    label_img_coord1.place_forget()
    label_img_coord2.place_forget()

    # click_event
    frame.place(x=225, y=75, width=600, height=350)
    # frame.bind("<Button-1>", click)

    labelImg1.config(image=imageAutomatic)
    labelImg1.place(x=50, y=50, width=500, height=250)
    labelImg1.Image = imageNavigate
    labelImg1.bind("<Button-1>", click1)

    global center
    center = distance_calculator.center(500, 250)
    print(center)

    # global text
    # text = "Abstand von {} zum Mittelpunkt: {}".format(point,dist)


# tracking
def button12_click():
    hide_coordinate_buttons()
    hide_navigate_buttons()
    hide_images_buttons()
    output_lab.place_forget()
    labelImg.place_forget()
    label_img_coord1.place_forget()
    label_img_coord2.place_forget()

    frame.place(x=225, y=75, width=600, height=350)

    # TODO
    # koennte man noch verbessern
    labelImg1.config(image=imageAutomatic)
    labelImg1.place(x=50, y=50, width=500, height=250)
    labelImg1.Image = imageNavigate
    labelImg1.bind("<Button-1>", click2)

    buttonColor1.place(x=175, y=460, width=140, height=30)
    buttonColor2.place(x=175, y=520, width=140, height=30)
    buttonColor3.place(x=175, y=580, width=140, height=30)

    text_box_label1.place(x=370, y=460, width=30, height=30)
    text_box_label2.place(x=370, y=520, width=30, height=30)
    text_box_label3.place(x=370, y=580, width=30, height=30)
    text_box1.place(x=400, y=460, width=140, height=30)
    text_box2.place(x=400, y=520, width=140, height=30)
    text_box3.place(x=400, y=580, width=140, height=30)
    text_box_button.place(x=370, y=640, width=170, height=30)

    # global bu2_blocked
    # if not bu2_blocked:  # False
    #     print("kd")
    #     # comment("Tracking-\nModus")
    #     # output('Tracking-Modus ...')
    #     # output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'), aspect=800)
    #     # output_lab.place(x=225, y=475, width=600)
    #
    #     # TODO
    #     # WZ-Detektion
    #     # Motoren ansteuern
    #
    # else:
    #     output("Motoren sind gesperrt!")
    #     output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
    #     output_lab.place(x=600, y=460, width=170, height=150)
    #     stop()


# coordinate
def button2_click():
    hide_focus_windows()
    hide_tracking_buttons()
    hide_navigate_buttons()
    hide_images_buttons()
    output_lab.place_forget()
    labelImg.place_forget()
    label_img_coord1.place_forget()
    label_img_coord2.place_forget()
    # output_lab.place_forget()
    # toolbar_yy.place(x=150, y=0, width=150, height=1000)
    buttonMode21.place(x=175, y=100, width=140, height=30)
    buttonMode22.place(x=175, y=180, width=140, height=30)

    # TODO
    # Seite noch etwas fuellen, noch zu leer


def button21_click():
    hide_coordinate_buttons()
    # TODO
    # Textfeld anpassen an moegliche Werte
    output('Geben Sie die gewuenschten Koordinaten ein, '
           'der Wert darf zwischen ??? liegen')
    output_label_coor()

    ind = Image.open("angle.jpeg")
    pht = ImageTk.PhotoImage(ind)     # photo
    # img = Label(master=frameGui, image=photo)  # funktioniert nur mit master=frameGui
    # img.place(x=150, y=325, width=750, height=100)
    label_img_coord1.config(image=pht)
    label_img_coord1.place(x=250, y=350, width=550, height=260)

    # panel
    # buttonAction = Button(master=frameGui, text='ENTER', command=button_action)
    # buttonAction.place(x=625, y=200, width=100, height=20)
    # # dialog box
    # eingabefeld.place(x=500, y=150 ,width=350, height=30)
    # text_label.place(x=500, y=250,width=350,height=25)
    # # motion_control_scriptG.navigate()

    # def button_action():
    #     entry_text = eingabefeld.get()
    #     if  entry_text == "":
    #         text_label.config(text="undefined key")
    #     else:
    #         text = functionsG.input(entry_text)
    #         text_label.config(text=text)

    # coordinates, extra window
    def fetch(entries):
        global bu2_blocked, text
        ind = 0
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            print('%s: "%s"' % (field, text))
            if ind == 0:
                x = entry[1].get()
                ind = ind + 1
            elif ind == 1 :
                y = entry[1].get()
                ind = ind + 1
            elif ind == 2:
                z = entry[1].get()
                ind = ind+1
            elif ind == 3:
                wait = entry[1].get()
                ind = 0
                # TODO
                # wait wird falsch uebertragen

                if not bu2_blocked:         # False
                    motion_control_scriptG.save_coordinates_wait(x, y, z, wait)
                    # TODO
                    # Motoren ansteuern
                    # noch Funktion zum "Umrechnen" einbauen

                    # read_coordinates('neue Koordinaten:')
                    read('')
                    output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
                    # output_lab.place(x=225, y=450, width=600, height=200)
                    label_img_coord1.place_forget()

                else:
                    label_img_coord1.place_forget()

                    print("Motoren sind gesperrt")
                    output("Motoren sind gesperrt!")
                    output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
                    output_lab.place(x=225, y=450, width=600, height=200)
                    stop()


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
    output('Geben Sie die gewuenschte Winkel Position der einzelnen Motoren ein, '
           'der Wert darf zwischen 0 - 180 Grad liegen')
    output_label_coor()

    ind = Image.open("angle.jpeg")
    pht = ImageTk.PhotoImage(ind)
    # img = Label(master=frameGui, image=photo)  # funktioniert nur mit master=frameGui
    # img.place(x=150, y=325, width=750, height=100)
    label_img_coord2.config(image=pht)
    label_img_coord2.place(x=250, y=350, width=550, height=260)     # x=350, y=350, width=350, height=190

    def fetch(entries):
        global bu2_blocked, text
        ind = 0
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            print('%s: "%s"' % (field, text))
            if ind == 0:
                x = entry[1].get()
                ind = ind+1
            elif ind == 1:
                y = entry[1].get()
                ind = ind + 1
            elif ind == 2:
                z = entry[1].get()
                ind = ind + 1
            elif ind == 3:
                wait = entry[1].get()
                print(wait)
                ind = 0
                # TODO
                # wait wird falsch uebertragen

                if not bu2_blocked:         # False
                    # TODO
                    # Winkel der Motoren noch in Koordinaten umrechnen um einheitliches Format der "coordinaten.txt" zu haben
                    motion_control_scriptG.save_coordinates_wait(x, y, z, wait)
                    # TODO
                    # Motoren ansteuern
                    # noch Funktion zum "Umrechnen" einbauen

                    # read_coordinates('neue Koordinaten:')
                    read('new angle position:')
                    output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
                    label_img_coord2.place_forget()


                else:
                    label_img_coord2.place_forget()

                    print("Motoren sind gesperrt")
                    output("Motoren sind gesperrt!")
                    output_lab.config(text=text, bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
                    print(text)
                    output_lab.place(x=225, y=450, width=600, height=200)
                    stop()


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


# navigate
def button3_click():
    hide_focus_windows()
    hide_tracking_buttons()
    hide_coordinate_buttons()
    hide_images_buttons()
    labelImg.place_forget()
    label_img_coord1.place_forget()
    label_img_coord2.place_forget()
    # motion_control_scriptG.coordinate()

    read_coordinates('alte Daten:')
    output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
    output_lab.place(x=225, y=425, width=600, height=200)

    button1.place(x=250, y=100, width=100, height=20)
    button2.place(x=175, y=140, width=100, height=20)
    button3.place(x=325, y=140, width=100, height=20)
    button4.place(x=250, y=180, width=100, height=20)
    button5.place(x=235, y=230, width=40, height=20)
    button6.place(x=325, y=230, width=40, height=20)
    button7.place(x=235, y=290, width=130, height=20)
    button8.place(x=585, y=325, width=180, height=20)
    labelImg2.config(image=imageNavigate)
    labelImg2.place(x=500, y=110, width=350, height=190)

    # read_coordinates('')
    # output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))


# images
def button4_click():
    labelImg.place_forget()
    label_img_coord1.place_forget()
    label_img_coord2.place_forget()
    hide_focus_windows()
    hide_tracking_buttons()
    hide_navigate_buttons()
    hide_coordinate_buttons()
    output_lab.place_forget()
    close_stop()

    print("lade Bilder")

    output('Die letzten/ aktuellsten neun Bilder wurden geladen, Stand: ' + time.strftime("%d.%m.%Y %H:%M:%S"))
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
def button_click_image(ind):
    global image, image_na
    img_names = imagesG.list_images(9)     # 12, image_names
    image = load_image(img_names[ind])      # image_names[ind]
    reload_images()

    print("lade passende Position...")
    # print(img_names[ind])

    image_name = img_names[ind]

    txt = 'aktuelles Bild:\n' + image_name
    image_label.config(text=txt)

    image_name = image_name.split(".")
    image_na = image_name[0]
    print(image_na)
    load_position(image_na)
    output("Daten zum Bild: " + image_na + " wurden geladen")
    output_label_img()


# set color for WZ-detection and get x-, y-distance
def button_click_color(color):
    global image, bu2_blocked
    # print(color)
    if not bu2_blocked:
        img_name = "../Matlab/Bilder/" + image_na + ".png"
        # x_dist, y_dist = detection.algorithm(img_name, color, mode)
        x_dist, y_dist = detection.algorithm('schwarz_weiss.jpeg', color)   # zum Testen
        # print(x_dist, y_dist)

        # TODO
        # gewuenschte Position berechnen
        # Motoren ansteuern
        # Bildgrosse beachten
    else:
        output("Motoren sind gesperrt!")
        output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 18, 'italic'))
        output_lab.place(x=600, y=460, width=170, height=150)
        stop()


# output for the side coordinates
def output_label_coor():
    # output_lab = Message(master=frameGui)
    output_lab.config(text=str(text), bg='#E0ECF8', anchor=N, font=('times', 20, 'italic'), aspect=300)
    output_lab.place(x=300, y=120, width=450)       # y=100,   , height=200


# output for the side image
def output_label_img():
    # output_lab = Message(master=frameGui)
    output_lab.config(text=str(text), bg='#E0ECF8', anchor=N, font=('times', 20, 'italic'), aspect=200)
    output_lab.place(x=300, y=100, width=450)      # x= 200,


# set new output text
def output(data):
    global text
    text = data


def comment(data):
    if data == 'Motoren sind gesperrt!':
        comment_label['fg'] = 'red'
        if bu1_blocked:          # True
            data = "Motoren Posi-\n" \
                   "tionen werden gehalten\n" + data
    elif data == 'Motoren Positionen werden gehalten':
        comment_label['fg'] = 'red'
        if bu2_blocked:          # True
            data = 'Motoren sind\n' \
                   'gesperrt\nMotoren Posi-\n' \
                   'tionen werden gehalten'
    elif data == 'Motoren sind wieder frei/ halten nicht mehr':
        if bu2_blocked:         # True
            comment_label['fg'] = 'orange'
            data = 'Motoren sind\n' \
                   'gesperrt\nMotoren sind\n' \
                   'wieder frei/ \n' \
                   'halten nicht\n' \
                   'mehr'
    elif data == 'Motoren sind freigegeben!':
        if bu1_blocked:     # True
            comment_label['fg'] = 'orange'
            data = 'Motoren Posi-\n' \
                    'tionen werden gehalten\n' + data
    elif data =='Bilder wurden neu geladen':
        # if bu1_blocked == True:
        #     data = 'Motoren Positionen werden gehalten ' + data
        # elif bu2_blocked == True:
        #     data = "Motoren sind gesperrt\n" + data
        # elif bu2_blocked == True & bu1_blocked == True:
        #     data = 'Motoren Posi-\n' \
        #            'tionen werden gehalten  ' \
        #            'Motoren sind gesperrt' + data

        # data = 'Bilder wurden neu geladen'
        comment_label['fg'] = 'black'
        # TODO
        # 2. String wird verschluckt, Messagebox zu klein?
    # else:
    #     comment_label['fg'] = 'white
    comment_label.config(text=str(data),anchor=NW ,font=('times', 14, 'italic'))

    comment_label.place(x=10, y=360, width=130)     # , height=360


# load position addicted to image
def read_coordinates(data):
    global image_na
    print(image_na)
    # x, y, z, wait = motion_control_scriptG.read_coordinates()
    coord = load_position(image_na)
    x_coord = coord[0]
    y_coord = coord[1]
    z_coord = coord[2]
    wait = str(3)
    global text
    if data == '':
        text = "x-Koordinate: " + x_coord + "\n"  \
                                 "y-Koordinate: " + y_coord + "\n" \
                                                              "z-Koordinate " + z_coord + "\n" \
                                                                       "time to wait: " + wait + ""
    # TODO
    # wird daas wirklich benoetigt ???
    elif data == 'new angle position:':
        text = "pitch: " + x_coord + "\n" \
                                      "roll: " + y_coord + "\n" \
                                                             "yaw: " + z_coord + "\n" \
                                                                                    "time to wait: " + wait + ""
    else:
        text = ""+data+"\n" \
               "x-Koordinate: " + x_coord + "\n"  \
                                          "y-Koordinate: " + y_coord + "\n" \
                                                             "z-Koordinate: " + z_coord + "\n" \
                                                                               "time to wait: " + wait +""


# read old coordinates, independent of the image
def read(data):
    coord = motion_control_scriptG.read_coordinates()
    x_coord = coord[0]
    y_coord = coord[1]
    z_coord = coord[2]
    wait = str(3)
    global text
    if data == '':
        text = "x-Koordinate: " + x_coord + "\n" \
                                      "y-Koordinate: " + y_coord + "\n" \
                                                             "z-Koordinate " + z_coord + "\n" \
                                                                                   "time to wait: " + wait + ""
    elif data == 'new angle position:':
        text = "pitch: " + x_coord + "\n" \
                               "roll: " + y_coord + "\n" \
                                              "yaw: " + z_coord + "\n" \
                                                            "time to wait: " + wait + ""
    else:
        text = "" + data + "\n" \
                           "x-Koordinate: " + x_coord + "\n" \
                                                  "y-Koordinate: " + y_coord + "\n" \
                                                                         "z-Koordinate: " + z_coord + "\n" \
                                                                                                "time to wait: " + wait + ""


# def print(data):
    # global text
    # text = data


def hide_tracking_buttons():
    buttonColor1.place_forget()
    buttonColor2.place_forget()
    buttonColor3.place_forget()
    text_box_label1.place_forget()
    text_box_label2.place_forget()
    text_box_label3.place_forget()
    text_box1.place_forget()
    text_box2.place_forget()
    text_box3.place_forget()
    text_box_button.place_forget()


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


def hide_focus_windows():
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


# print script, navigate
def print_script():
    global bu2_blocked
    if not bu2_blocked:     # False
        # TODO
        # Motoren ansteuern

        # motion_control_scriptG.printScript2()
        # print('print script')

        read('neue Koordinaten:')
        output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
    else:
        output("Motoren sind gesperrt!")
        output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
        stop()


# reload position
def update_coordinates():
    read_coordinates('new coordinates')
    output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))


# load image from file
def load_image(name):
    # img = ImageTk.PhotoImage(Image.open(name))
    img = Image.open("../Matlab/Bilder/" + name)
    return img


# load image from file and add to list
def load_images(name):          # buttons
    # img = ImageTk.PhotoImage(Image.open(name))
    img = Image.open("../Matlab/Bilder/"+name)
    img = resize_image(img, 175, 100)
    images.append(img)
    return img


# adapt imgae size
def resize_image(img, h, w):
    resize = img.resize((h, w), Image.ANTIALIAS)
    img_re = ImageTk.PhotoImage(resize)        # image
    return img_re                               # image


#
def get_latest_images():
    global image
    list_images(6)
    image = load_image(imagesG.latest_image())
    comment('Bilder wurden neu geladen')


# load the latest images, the number depend on maxi
def list_images(maxi):
    img_names = imagesG.list_images(maxi)           # image_names
    print(img_names)
    for img in img_names:                         # image
        load_images(img)


# load new image for gui
def reload_images():
    global image, imageStart, imageAutomatic, imageNavigate
    imageStart = resize_image(image, 300, 150)  # latest image
    imageAutomatic = resize_image(image, 500, 250)
    imageNavigate = resize_image(image, 350, 190)


# load position for ...
def load_position(name):
    # file_name = 'Positionen/'+name+'.txt'
    # print(file_name)
    x_coord, y_coord, z_coord = motion_control_scriptG.read_old_coordinates(name)

    # motion_control_scriptG.save_coordinates_without_wait(x, y, z)        Bildposition auf aktuelle Koordinaten setzen
    print(x_coord, y_coord, z_coord)
    return x_coord, y_coord, z_coord

    # motion_control_scriptG.printScript1(x, y, z, 3)
    # motion_control_scriptG.save_coordinates(x, y, z, 3)


# place warning-label
def warning():
    if __name__ == '__main__':
        root_angle = Tk()
        root_angle.title('Eingabe der Werte')

        ind = Image.open("warning1.jpg")
        pht = ImageTk.PhotoImage(ind)
        img = Label(master=frameGui, image=pht)     # funktioniert nur mit master=frameGui
        img.place(x=150, y=325, width=750, height=100)
        # img.pack(fill=X, pady=5)

        # tkMessageBox.showwarning("Warning", "Sind sie sich sicher das nichts im Weg ist und sie in die gewuenschte
        # Richting verfahren koennen?")
        txt = Label(root_angle, text="Sind Sie sich sicher das nichts im Weg ist \n "
                                      "& Sie in die gewuenschte Richting verfahren koennen?", bg="red", fg="white")
        txt.pack(fill=X, pady=5)
        b1 = Button(root_angle, text='auf die andere Seite fahren', command=lambda: opposite(root_angle, img))
        # command=motion_control_scriptG.printScript()
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
    if not bu2_blocked:
        motion_control_scriptG.opposite(image_na + '.txt')
        root_angle.destroy()
        img.place_forget()
    else:
        # TODO
        # keine extra Feld oeffnen
        output("Motoren sind gesperrt!")
        output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
        stop()


# close warning-label
def close_warning(root_angle, img):
    root_angle.destroy()
    img.place_forget()


# place stop-label
def stop():
    print("stop")
    img_stop.place(x=150, y=100, width=750, height=250)
    img_stop.lift()


# close stop-label
def close_stop():
    img_stop.place_forget()


# hold position
def bu1_onclick():
    global bu1_blocked
    if not bu1_blocked:
        bu1['bg'] = '#FE9A2E'
        bu1['fg'] = 'white'
        bu1['text'] = 'Positionen \nwerden gehalten'
        bu1_blocked = True
        print(bu1_blocked)
        comment('Motoren Positionen werden gehalten')
    elif bu1_blocked:
        bu1['bg'] = '#BDBDBD'
        bu1['fg'] = 'black'
        bu1['text'] = 'Motoren \nPosition halten'
        bu1_blocked = False
        print(bu1_blocked)
        comment('Motoren sind wieder frei/ halten nicht mehr')


# TODO
# Funktion zum Position halten einbauen


# blocked motor
def bu2_onclick():
    global bu2_blocked
    if not bu2_blocked:
        bu2['bg'] = '#B40431'
        bu2_blocked = True
        bu2['fg'] = 'white'
        bu2['text'] = 'Motoren \ngesperrt'
        print(bu2_blocked)
        comment('Motoren sind gesperrt!')
    elif bu2_blocked:
        bu2['bg'] = '#BDBDBD'
        bu2['fg'] = 'black'
        bu2['text'] = 'Motoren \nsperren'
        bu2_blocked = False
        print(bu2_blocked)
        comment('Motoren sind freigegeben!')

        img_stop.place_forget()

        # TODO
        output("Motoren sind wieder freigegeben!")
        output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
        # geht so nur bei navigate, coordinate, focus & letzte Position


def get_blocked(ind):
    global bu2_blocked
    if not bu2_blocked:     # == False
        if ind == 0:
            motion_control_scriptG.up()
        elif ind == 1:
            motion_control_scriptG.left()
        elif ind == 2:
            motion_control_scriptG.right()
        elif ind == 3:
            motion_control_scriptG.down()
    else:
        print(ind)  # index
        output("Motoren sind gesperrt!")
        output_lab.config(text=str(text), bg='#E0ECF8', anchor=NW, font=('times', 20, 'italic'))
        # comment("Motoren sind gesperrt!")
        stop()


# create the window
tk_fenster = Tk()
tk_fenster.title('GUI')
tk_fenster.geometry('1000x720')

# background
frameGui = Frame(master=tk_fenster, bg='#A9BCF5')
frameGui.place(width=1000, height=720)    # x=5, y=5 border

# toolbar
toolbar_y = Frame(tk_fenster, bg='#084B8A')
# toolbar.pack(side=TOP, fill=X, padx=10)
toolbar_y.place(x=0, y=0, width=150, height=720)
toolbar_yy = Frame(master=tk_fenster, bg='#045FB4')
# toolbar.pack(side=TOP, fill=X, padx=10)
toolbar_yyy = Frame(tk_fenster, bg='#084B8A')
# toolbar.pack(side=TOP, fill=X, padx=10)
toolbar_yyy.place(x=900, y=0, width=100, height=720)

# comment
comment_label = Message(master=toolbar_y, bg='#E6E6E6', anchor=N, text="Infos", font=('times', 10, 'italic'))
comment_label.place(x=10, y=360, width=130)         # , height=380

# scrollbar
# scrollbar = Scrollbar(tk_fenster)
# buttonBox = Listbox(tk_fenster, yscrollcommand = scrollbar.set )

# label
my_label = Label(master=frameGui, text="Automatische Werkzeug-Kontakt Detektion", bg='white')    # bg='#BDBDBD'
my_label.place(x=350, y=20, width=350, height=30)

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
labelImg.place(x=350, y=100, width=350, height=200)
labelImg1 = Label(master=frame, bg='white')           # focus
labelImg2 = Label(master=frameGui, bg='white')        # navigate

label_img_coord1 = Label(master=frameGui, bg='white')
label_img_coord2 = Label(master=frameGui, bg='white')


# image informations
image_infos = 'aktuelles Bild: ' + image_na
image_label = Message(master=tk_fenster, bg='#E6E6E6', anchor=N, text=image_infos, font=('times', 9, 'italic'),
                      aspect=100)
image_label.place(x=910, y=120, width=80)

# stop image
i = Image.open("stop.png")
photo = ImageTk.PhotoImage(i)
img_stop = Label(master=frameGui, image=photo)  # funktioniert nur mit master=frameGui

# Button
buttonMode = Button(master=toolbar_y, text='letzte Position', command=button_click)
buttonMode.place(x=25, y=100, width=100, height=20)
buttonMode11 = Button(master=toolbar_y, text='automatisch', command=button11_click)
buttonMode11.place(x=25, y=140, width=100, height=20)
buttonMode12 = Button(master=toolbar_y, text='Tracking', command=button12_click)
buttonMode12.place(x=25, y=180, width=100, height=20)
buttonMode2 = Button(master=toolbar_y, text='Koordinaten', command=button2_click)
buttonMode2.place(x=25, y=220, width=100, height=20)
buttonMode21 = Button(master=frameGui, text='Koordinaten: x, y, z', command=button21_click)
buttonMode22 = Button(master=frameGui, text='Winkel', command=button22_click)
buttonMode3 = Button(master=toolbar_y, text='Navigation', command=button3_click)
buttonMode3.place(x=25, y=260, width=100, height=20)
buttonMode4 = Button(master=toolbar_y, text='Bilder', command=button4_click)
buttonMode4.place(x=25, y=300, width=100, height=20)
# button1 = Button(master=frameGui, text='oben', command=lambda: motion_control_scriptG.up(bu2_blocked))
button1 = Button(master=frameGui, text='oben', command=lambda: get_blocked(0))
# button2 = Button(master=frameGui, text='links', command=lambda: motion_control_scriptG.left(bu2_blocked))
button2 = Button(master=frameGui, text='links', command=lambda: get_blocked(1))
# button3 = Button(master=frameGui, text='rechts', command=lambda: motion_control_scriptG.right(bu2_blocked))
button3 = Button(master=frameGui, text='rechts', command=lambda: get_blocked(2))
# button4 = Button(master=frameGui, text='unten', command=lambda: motion_control_scriptG.down(bu2_blocked))
button4 = Button(master=frameGui, text='unten', command=lambda: get_blocked(3))
button5 = Button(master=frameGui, text='3sec', command=lambda: motion_control_scriptG.wait(3))
button6 = Button(master=frameGui, text='5sec', command=lambda: motion_control_scriptG.wait(5))
button7 = Button(master=frameGui, text='Daten verschicken', command=print_script)
button8 = Button(master=frameGui, text='zur anderen Seite fahren', command=warning)
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
buttonColor1 = Button(master=frameGui, text='[33, 33, 33]', command=lambda: button_click_color([33, 33, 33]))
buttonColor2 = Button(master=frameGui, text='[0, 0, 0]', command=lambda: button_click_color([0, 0, 0]))
buttonColor3 = Button(master=frameGui, text='[255, 255, 255]', command=lambda: button_click_color([255, 255, 255]))

#
exit_button = Button(tk_fenster, text="Beenden", command=tk_fenster.destroy, bg='#BDBDBD')
exit_button.place(x=910, y=20, width=80, height=20)
refresh_button = Button(tk_fenster, text=" Bilder \n neu laden", command=lambda: get_latest_images(), bg='#BDBDBD')
refresh_button.place(x=910, y=60, width=80, height=40)
#
bu1 = Button(tk_fenster, text="Motoren \n halten", command=lambda: bu1_onclick(), bg='#BDBDBD')
bu1.place(x=905, y=600, width=90, height=40)
bu2 = Button(tk_fenster, text="Motoren \n sperren", command=lambda: bu2_onclick(), bg='#BDBDBD')
bu2.place(x=905, y=660, width=90, height=40)

# tracking-text box
text_box_label1 = Label(tk_fenster, text='R:')
text_box_label2 = Label(tk_fenster, text='G:')
text_box_label3 = Label(tk_fenster, text='B:')
text_box1 = Entry(tk_fenster, bd=5, width=45)
text_box2 = Entry(tk_fenster, bd=5, width=45)
text_box3 = Entry(tk_fenster, bd=5, width=45)
# text_box_button = Button(tk_fenster, text='ENTER', command=lambda: button_click_color([55, 55, 55]))
text_box_button = Button(tk_fenster, text='ENTER', command=lambda:
                         button_click_color([int(text_box1.get()), int(text_box2.get()), int(text_box3.get())]))


# coordinate
eingabefeld = Entry(tk_fenster, bd=5, width=45)
text_label = Label(tk_fenster)

# output
output_lab = Message(master=frameGui)       # vorgeschriebene Breite
# output_lab = Text(master=frameGui)          # hat kein Attribut text (bei config)
# output_lab = Label(master=frameGui)       # text laeuft aus dem Label hinaus

# activation the window
tk_fenster.mainloop()
