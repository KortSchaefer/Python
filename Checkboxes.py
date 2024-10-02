from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
root.geometry('400x400')

def show():
    lbl = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text='Check this box', variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

btn = Button(root, text="Show Selecrion", command=show).pack()

root.mainloop()