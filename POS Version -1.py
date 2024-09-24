from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("POS System")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")

orderFrame = LabelFrame(root, text="Order Box", padx=50, pady=50)
orderFrame.grid(column=0, row=1, padx=10, pady=10)
orderBox= Label(orderFrame, text='Box').pack()

entryFrame = LabelFrame(root, text="Order Box", padx=50, pady=50)
entryFrame.grid(column=2, row=1, padx=10, pady=10)
orderBox= Label(entryFrame, text='Box').pack()

scrollFrame = LabelFrame(root, text="Order Box", padx=50, pady=50)
scrollFrame.grid(column=1, row=1, padx=10, pady=10)
orderBox= Label(scrollFrame, text='Box').pack()

bottomFrame = LabelFrame(root, text="Order Box", padx=50, pady=50)
bottomFrame.grid(column=1, row=3, padx=10, pady=10)
orderBox= Label(bottomFrame, text='Box').pack()

topFrame = LabelFrame(root, text="Order Box", padx=50, pady=50)
topFrame.grid(column=1, row=0, padx=10, pady=10)
orderBox= Label(topFrame, text='Box').pack()

root.mainloop()