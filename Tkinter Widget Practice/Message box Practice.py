from tkinter import *
from PIL import ImageTk, Image
'''You need a module for this one'''
from tkinter import messagebox

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")

'''You can change the showinfo to many things depending on use case. ex. (askyesno, askokcancel, etc.)'''

def popup():
    responce=messagebox.askquestion("This is my popup", "hello World")
    Label(root, text=responce).pack()
    
    if responce == 'yes':
        Label(root, text="you clicked yes").pack()
    else:
        Label(root, text="you clicked no").pack() 

Button(root, text="Popup", command=popup).pack()

root.mainloop()