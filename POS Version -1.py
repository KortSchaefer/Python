from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("POS System")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")


### |  |  |  |
### |xx|  |  |
### |  |  |  |
orderFrame = LabelFrame(root, text="Order Box", padx=100, pady=300)
orderFrame.grid(column=0, row=1, padx=(15, 2), pady=2)
orderBox= Label(orderFrame, text='Box').pack()


### |  |  |  |
### |  |  |xx|
### |  |  |  |
entryFrame = LabelFrame(root, text="Entry Box", padx=250, pady=300)
entryFrame.grid(column=2, row=1, padx=(2,15), pady=2)
orderBox= Label(entryFrame, text='Box').pack()


### |  |  |  |
### |  |xx|  |
### |  |  |  |
scrollFrame = LabelFrame(root, text="Scroll Box", padx=30, pady=300)
scrollFrame.grid(column=1, row=1, padx=2, pady=2)
orderBox= Label(scrollFrame, text='Box').pack()


### |  |  |  |
### |  |  |  |
### |xx|xx|xx|
bottomFrame = LabelFrame(root, text="Bottom Box", padx=430, pady=50)
bottomFrame.grid(column=0, row=3, padx=2, pady=2, columnspan=3)
orderBox= Label(bottomFrame, text='Box').pack()


### |xx|xx|xx|
### |  |  |  |
### |  |  |  |
topFrame = LabelFrame(root, text="Top Box", padx=430, pady=50)
topFrame.grid(column=0, row=0, padx=2, pady=2,columnspan=4)
orderBox= Label(topFrame, text='Box').pack()

root.mainloop()