from tkinter import *
from PIL import ImageTk, Image

root= Tk()

r = IntVar()
r.set('1')
r2 = IntVar()



def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 1", variable=r, value=2, command=lambda: clicked(r.get())).pack()

b1 = Button(root, text="click Me", command=lambda: clicked(r.get()))
b1.pack()

Radiobutton(root, text="Option 1", variable=r2, value=1).pack()
Radiobutton(root, text="Option 1", variable=r2, value=2).pack()

root.mainloop()