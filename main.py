#  Copyright (c) 2024. William E. Kitson

from image_writer import ImageWriter
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
img = ImageTk.PhotoImage(ImageWriter("4kitsw10_COM519_database").load("Ice Cream"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()

from presentation import Presentation
Presentation("4kitsw10_COM519_database").render()