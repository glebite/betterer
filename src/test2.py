import tkinter as tk
from PIL import ImageTk, Image
import os
import glob
import sys

win = tk.Tk()
win.geometry('800x500')  # set window size
win.resizable(0, 0)  # fix window

panel = tk.Label(win)
panel.pack()

list_of_files = glob.glob(sys.argv[1]+'/*.jpg')
list_of_files.sort(key=os.path.getmtime)

images = iter(list_of_files)  # make an iterator

def next_img():
    try:
        img = next(images)  # get the next image from the iterator
    except StopIteration:
        return  # if there are no more images, do nothing

    # load the image and display it
    img = Image.open(img)
    h, w = img.size
    img = img.resize((h // 4, w // 4), Image.ANTIALIAS)
    
    img = ImageTk.PhotoImage(img)
    panel.img = img  # keep a reference so it's not garbage collected
    panel['image'] = img

btn = tk.Button(text='Next image', command=next_img)
btn.pack()

# show the first image
next_img()

win.mainloop()
