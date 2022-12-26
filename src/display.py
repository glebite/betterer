"""display.py

Eseentially display an image - typically the "get" image
so it's displaying correctly.  It should pre-cache the
"""


from PIL import ImageTk, Image
from tkinter import Tk, PhotoImage, Button, W, E, RIDGE, Label, Canvas
import glob
import os
import sys
from carouselle import Carouselle


class Display(Carouselle):
    def __init__(self, parent, file_path, file_ptr=None):
        """__init__

        Parameters:
        file_path (str): path to the list of images
        file_ptr (str): match for glob (*.jpg)

        Returns:
        n/a
        """
        super().__init__()
        self.file_ptr = file_ptr
        if not os.path.exists(file_path):
            raise FileExistsError
        self.file_path = file_path

        self.counter = 0

        self.parent = parent
        self.master_list()
        self.photo = ImageTk.PhotoImage(Image.open(
            self.file_list[self.counter]).resize((640, 480)))

        self.display = Label(parent, text="", image=self.photo, bg="white")
        self.display.image = self.photo
        self.display.grid(row=0, column=0)

        back = Button(parent, width=2, anchor=W, text="<", relief=RIDGE,
                      command=self.previous_image)
        back.grid(row=1, column=0)

        forward = Button(parent, width=2, anchor=E, text=">", relief=RIDGE,
                         command=self.next_image)
        forward.grid(row=1, column=1)

    def master_list(self):
        """master_list
        """
        self.file_list = sorted(glob.glob(self.file_path + self.file_ptr),
                                key=os.path.getmtime)

    def next_image(self):
        """
        """
        self.counter += 1
        img = ImageTk.PhotoImage(Image.open(
            self.file_list[self.counter]).resize((640, 480)))
        print(self.counter)
        self.photo = img
        self.display.configure(image=self.photo)

    def previous_image(self):
        """
        """
        self.counter -= 1
        img = ImageTk.PhotoImage(Image.open(
            self.file_list[self.counter]).resize((640, 480)))
        print(self.counter)
        self.photo = img
        self.display.configure(image=self.photo)


if __name__ == "__main__":
    root = Tk()
    root.title("hello")
    x = Display(root, sys.argv[1], sys.argv[2])
    root.mainloop()
