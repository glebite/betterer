import tkinter
from tkinter import *
import sys
import time
import glob
import os
from PIL import ImageTk, Image

list_of_files = glob.glob(sys.argv[1]+'/*.jpg')
list_of_files.sort(key=os.path.getmtime)



root = Tk()
for file_name in list_of_files:
    image1 = Image.open(file_name)
    h, w = image1.size
    image1 = image1.resize((h // 2, w // 2), Image.ANTIALIAS)
    
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test

    label1.place(x=0, y = 0)
    label1.pack()
    root.update()
    
root.mainloop()

