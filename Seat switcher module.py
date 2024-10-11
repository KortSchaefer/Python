from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
root.geometry('400x400')

orderFrame = LabelFrame(root, text="Order Box", relief='raised', bg='white')
orderFrame.grid_propagate(False)
orderFrame.grid(column=0, row=1, padx=(15, 2), pady=2, sticky='nsew')



testButton = Button(orderFrame, text="test").grid(row=0, column=0)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()