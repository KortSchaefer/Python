from tkinter import *
from PIL import ImageTk, Image

root= Tk()

r = IntVar()
r2 = IntVar()

Radiobutton(root, text="Option 1", variable=r, value=1).pack()
Radiobutton(root, text="Option 1", variable=r, value=2).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

Radiobutton(root, text="Option 1", variable=r2, value=1).pack()
Radiobutton(root, text="Option 1", variable=r2, value=2).pack()

root.mainloop()