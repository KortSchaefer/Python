from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
root.geometry('400x400')

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

clicked = StringVar()
clicked.set('Monday')
# Create a Combobox for days of the week
day_combobox = OptionMenu(root, clicked, *days_of_the_week)
day_combobox.pack(pady=10)

'''Code Goes Here'''

root.mainloop()