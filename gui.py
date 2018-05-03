from tkinter import *   # python 2.7 Tkinter
from PIL import Image, ImageTk
from random import randint
import sys
import motion_control_script
# import edge_detection

# event function
def button1Click():
    motion_control_script.automatic()


def button2Click():
    motion_control_script.coordinate()


def button3Click():
    motion_control_script.navigate()

# create the window
tkFenster = Tk()
tkFenster.title('GUI')
tkFenster.geometry('1000x1000')

# background
frameGui = Frame(master=tkFenster, bg='#6699FF')
frameGui.place( width=1000, height=1000)    # x=5, y=5 border
# Images
image1 = ImageTk.PhotoImage(Image.open("Bilder_BSP/filter1.jpg"))

# Label for images
labelImg = Label(master=frameGui, image=image1)
labelImg.place(x=50, y=70, width=350, height=200)

# Button zum Würfeln
buttonMode1 = Button(master=frameGui, text='automatic', command=button1Click)
buttonMode1.place(x=50, y=30, width=100, height=20)
buttonMode2 = Button(master=frameGui, text='coordinate', command=button2Click)
buttonMode2.place(x=175, y=30, width=100, height=20)
buttonMode3 = Button(master=frameGui, text='navigate', command=button3Click)
buttonMode3.place(x=300, y=30, width=100, height=20)
# activation the window
tkFenster.mainloop()
