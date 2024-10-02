from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
root.geometry('400x400')

var = IntVar()

c = Checkbutton(root, text='Check this box', variable=var)
c.pack()

root.mainloop()