from tkinter import *
from PIL import ImageTk, Image
'''You need a module for this one'''
from tkinter import messagebox

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")

def popup():
    messagebox.showinfo("This is my popup", "hello World")


Button(root, text="Popup", command=popup).pack()

root.mainloop()