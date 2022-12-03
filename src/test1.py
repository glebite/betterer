import tkinter
from tkinter import *
import sys
from PIL import ImageTk, Image

image1 = Image.open(sys.argv[1])
h, w = image1.size
image1 = image1.resize((h // 2, w // 2), Image.ANTIALIAS)

root = Tk()

test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test

label1.place(x=0, y = 0)
root.mainloop()

