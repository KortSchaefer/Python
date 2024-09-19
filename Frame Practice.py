from tkinter import *
from PIL import ImageTk, Image
'''Lol it didnt work'''
root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")

frame = LabelFrame(root, text="This is my frame.... ", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame,text="Dont Click Here!")
b.pack
root.mainloop()