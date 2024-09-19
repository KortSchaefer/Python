from tkinter import *
from PIL import ImageTk, Image
'''Lol it didnt work'''
root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
###Edit padx and y for larger/smaller frames
frame = LabelFrame(root, text="This is my frame.... ", padx=50, pady=50)
frame.grid(column=0, row=0, padx=10, pady=10)

frame2 = LabelFrame(root, text="This is my frame.... ", padx=50, pady=50)
frame2.grid(column=1, row=0, padx=10, pady=10)

frame3 = LabelFrame(root, text="This is my frame.... ", padx=50, pady=50)
frame3.grid(column=2, row=0, padx=10, pady=10)

b = Button(frame,text="Dont Click Here!")
b.pack()
b2 = Button(frame2,text="Dont Click Here!")
b2.pack()
b3 = Button(frame3,text="Dont Click Here!")
b3.pack()
root.mainloop()