from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
### Create a new window
top = Toplevel()
top.title("Image Practice")
top.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")


myimg = ImageTk.PhotoImage(Image.open("C:/Users/Kingc/Documents/Code/Python/Practice Images/stare1.png"))
lbl = Label(top, image=myimg).pack()
root.mainloop()