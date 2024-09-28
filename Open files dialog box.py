from tkinter import *
from PIL import ImageTk, Image
#have to import file system from tkinter
from tkinter import filedialog

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")

root.filename = filedialog.askopenfilename(initialdir="")

root.mainloop()