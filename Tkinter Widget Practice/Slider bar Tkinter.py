from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
root.geometry('400x400')


vertical = Scale(root, from_=0, to=200)
#make sure you add to screen on its own line
vertical.pack()

def slide(var):
    lbl = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()*2)+"x400")

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=slide)
horizontal.pack()

my_btn = Button(root, text="click ME", command=slide,).pack()

root.mainloop()