from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("POS System")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
root.configure(bg="lightblue")

###
###   Definition space
###

def scroll1():
    print("Button 1 pressed!")

def scroll2():
    print("Button 2 pressed!")

def scroll3():
    print("Button 3 pressed!")

def scroll4():
    print("Button 4 pressed!")

def scroll5():
    print("Button 5 pressed!")


### |  |  |  |
### |xx|  |  |
### |  |  |  |
orderFrame = LabelFrame(root, text="Order Box", width=100, height=300, relief='raised', bg='white')
orderFrame.grid_propagate(False)
orderFrame.grid(column=0, row=1, padx=(15, 2), pady=2)
orderBox= Label(orderFrame, text='Box').pack()


### |  |  |  |
### |  |  |xx|
### |  |  |  |
entryFrame = LabelFrame(root, text="Entry Box", width=250, height=300, relief='raised',)
entryFrame.grid(column=2, row=1, padx=(2,15), pady=2)
orderBox= Label(entryFrame, text='Box').pack()


### |  |  |  |
### |  |xx|  |
### |  |  |  |
scrollFrame = LabelFrame(root, text="Scroll Box", width=40, pady=300, relief='raised',)
scrollFrame.grid_propagate(False)
scrollFrame.grid(column=1, row=1, padx=2, pady=2,)
orderBox= Label(scrollFrame, text='Box').pack()


### |  |  |  |
### |  |  |  |
### |xx|xx|xx|
bottomFrame = LabelFrame(root, text="Bottom Box", width=430, height=20, relief='raised',)
bottomFrame.grid(column=0, row=3, padx=2, pady=2, columnspan=3)
orderBox= Label(bottomFrame, text='Box').pack()


### |xx|xx|xx|
### |  |  |  |
### |  |  |  |
topFrame = LabelFrame(root, text="Top Box", width=430, height=20, relief='raised',)
topFrame.grid(column=0, row=0, padx=2, pady=2,columnspan=4)
orderBox= Label(topFrame, text='Box').pack()

### Button Creation
buttonData = [
    {"name": "Soft Drinks", "command": scroll1},
    {"name": "Tea & Special", "command": scroll2},
    {"name": "Apps", "command": scroll3},
    {"name": "Apps\nas meal", "command": scroll4},
    {"name": "Side\nsalads", "command": scroll5}
]

for i, button_info in enumerate(buttonData):
    button = Button(scrollFrame, text=button_info["name"], command=button_info["command"])
    button.grid(row=i, column=0, padx=5, pady=5)



### Frame anchoring
for frame in [entryFrame, scrollFrame, topFrame, bottomFrame, orderFrame]:
    # sticky='nswe' acts like fill='both'
    frame.grid(sticky='NSWE')
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.grid_propagate(0)



root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()