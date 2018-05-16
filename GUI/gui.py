from tkinter import *   # python 2.7 Tkinter
from PIL import Image, ImageTk
from random import randint
import sys
import os
import motion_control_scriptG
import functionsG
import edge_detectionG

fields = 'x-coordinate', 'y-coordinate', 'z-coordinate', 'time to wait'
text = "Ausgabe"

# event function
def buttonClick():
    hide_navigate_buttons()
    labelImg.place_forget()
    # buttonModeTest.place_forget()
    read_coordinates('')
    output()


def button1Click():
    hide_navigate_buttons()
    labelImg.place_forget()
    motion_control_scriptG.automatic()
    edge_detectionG.execute("../Bilder_BSP/filter1.jpg")


def button2Click():
    hide_navigate_buttons()
    labelImg.place_forget()
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
                motion_control_scriptG.printScript1(x,y,z,wait)
                motion_control_scriptG.saveCoordinates(x,y,z,wait)
                read_coordinates('')
                output()


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
        # tkFenster.title('Angabe der Werte')
        ents = makeform(root, fields)
        root.bind('<Return>', (lambda event, e=ents: fetch(e)))
        b1 = Button(root, text='print script',command=(lambda e=ents: fetch(e))) # command=motion_control_scriptG.printScript()
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(root, text='Quit', command=root.quit)
        b2.pack(side=LEFT, padx=5, pady=5)
        root.mainloop()


def button3Click():
    # motion_control_scriptG.coordinate()
    read_coordinates('old datas:')
    output()
    button1.place(x=500, y=130, width=100, height=20)
    button2.place(x=500, y=170, width=100, height=20)
    button3.place(x=500, y=210, width=100, height=20)
    button4.place(x=500, y=250, width=100, height=20)
    button5.place(x=505, y=290, width=40, height=20)
    button6.place(x=555, y=290, width=40, height=20)
    button7.place(x=500, y=330, width=100, height=20)
    output()
    labelImg.place_forget()


def output():
    output_label = Message(master=frameGui, text=text)
    output_label.config(bg='#E0ECF8', anchor=N, font=('times', 24, 'italic'))
    output_label.place(x=200, y=450, width=650, height=250)


def print(data):
    global text
    text = data


def hide_navigate_buttons():
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    button5.place_forget()
    button6.place_forget()
    button7.place_forget()


def read_coordinates(data):
    x,y,z,wait = motion_control_scriptG.read_coordinates()
    global text
    if(data == ''):
        text = "x-coordinate: "+x+"\n"  \
                                 "y-coordinate: "+y+"\n" \
                                                     "z-coordinate: "+z+"\n" \
                                                                       "time to wait: "+wait+""
    else:
        text = ""+data+"\n" \
               "x-coordinate: " + x + "\n"  \
                                          "y-coordinate: " + y + "\n" \
                                                             "z-coordinate: " + z + "\n" \
                                                                               "time to wait: " + wait+""


def test():
    motion_control_scriptG.printScript2(),
    print('print script')
    read_coordinates('new coordinates')
    output()


# create the window
tkFenster = Tk()
tkFenster.title('GUI')
tkFenster.geometry('1000x1000')


# background
frameGui = Frame(master=tkFenster, bg='#A9BCF5')
frameGui.place( width=1000, height=1000)    # x=5, y=5 border


# toolbar
toolbarY = Frame(tkFenster, bg='#084B8A')
# toolbar.pack(side=TOP, fill=X, padx=10)
toolbarY.place(x=0, y=0, width=150, height=1000)
toolbarYY = Frame(tkFenster, bg='#084B8A')
# toolbar.pack(side=TOP, fill=X, padx=10)
toolbarYY.place(x=900, y=0, width=100, height=1000)


# Images
image1 = ImageTk.PhotoImage(Image.open("../Bilder_BSP/filter1.jpg"))
# Label for images
labelImg = Label(master=frameGui, image=image1, bg='#BDBDBD')
labelImg.place(x=350, y=100, width=350, height=200)

# Button
buttonMode = Button(master=toolbarY, text='start', command=buttonClick)
buttonMode.place(x=25, y=100, width=100, height=20)
buttonMode1 = Button(master=toolbarY, text='automatic', command=button1Click)
buttonMode1.place(x=25, y=140, width=100, height=20)
buttonMode2 = Button(master=toolbarY, text='coordinate', command=button2Click)
buttonMode2.place(x=25, y=180, width=100, height=20)
buttonMode3 = Button(master=toolbarY, text='navigate', command=button3Click)
buttonMode3.place(x=25, y=220, width=100, height=20)
button1 = Button(master=frameGui, text='oben', command=motion_control_scriptG.up)
button2 = Button(master=frameGui, text='links', command=motion_control_scriptG.left)
button3 = Button(master=frameGui, text='rechts', command=motion_control_scriptG.right)
button4 = Button(master=frameGui, text='unten', command=motion_control_scriptG.down)
button5 = Button(master=frameGui, text='3sec', command=motion_control_scriptG.wait(3)) # funktioniert nicht
button6 = Button(master=frameGui, text='5sec', command=motion_control_scriptG.wait(5))
# button7 = Button(master=frameGui, text='print script', command=(motion_control_scriptG.printScript2(),
#                                                                     print('print script'))) # funktioniert nicht
button7 = Button(master=frameGui, text='print script', command=test)
# buttonModeTest = Button(master=frameGui, text='test', command=output)
# buttonModeTest.place(x=50, y=400, width=100, height=20)
exit_button = Button(tkFenster, text="Beenden", command=tkFenster.quit, bg='#BDBDBD')
exit_button.place(x=920, y=20, width=60, height=20)


# label
my_label = Label(master=frameGui, text="Automatische Werkzeug-Kontakt Detektion", bg='#BDBDBD')
my_label.place(x=325, y=20, width=350, height=30)

# coordinate
eingabefeld = Entry(tkFenster, bd=5, width=45)
text_label = Label(tkFenster)


# activation the window
tkFenster.mainloop()
