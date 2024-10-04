from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("POS System")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
root.configure(bg="lightblue")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.attributes('-fullscreen', True)

# Bind the ESC key to exit fullscreen
root.bind("<Escape>", lambda event: root.attributes('-fullscreen', False))


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


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def getCheck():
    print('Get check')

def getRecipe():
    print('Get check')

def getQuantity():
    print('Get check')

def repeat():
    print('Get check')

def modify():
    print('Get check')

def delete():
    print('Get check')

def rapidFire():
    print('Get check')

def close():
    print('close')

def nextSeat():
    print('next Seat')


### |  |  |  |
### |xx|  |  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### |  |  |  |
orderFrame = LabelFrame(root, text="Order Box", relief='raised', bg='white')
orderFrame.grid_propagate(False)
orderFrame.grid(column=0, row=1, padx=(15, 2), pady=2)
orderBox= Label(orderFrame, text='Box').pack()


### |  |  |  |
### |  |  |xx| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### |  |  |  |
entryFrame = LabelFrame(root, text="Entry Box", relief='raised',)
entryFrame.grid(column=2, row=1, padx=(2,15), pady=2)
orderBox= Label(entryFrame, text='Box').pack()


### |  |  |  |
### |  |xx|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### |  |  |  |
scrollFrame = LabelFrame(root, text="Scroll Box", relief='raised',)
scrollFrame.grid_propagate(False)
scrollFrame.grid(column=1, row=1, padx=2, pady=2,)



### |  |  |  |
### |  |  |  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### |xx|xx|xx|
bottomFrame = LabelFrame(root, text="Bottom Box", relief='raised',)
bottomFrame.grid(column=0, row=2, padx=2, pady=2, columnspan=3)
bottomBox= Label(bottomFrame, text='Box')
bottomBox.grid(column=0, row=0)

### Button Creation

buttonDataBottomLeft = [
    {"name": "Close", "command": close},
    {"name": "Next Seat", "command": nextSeat}
    
]

for i, button_info in enumerate(buttonDataBottomLeft):
    button = Button(bottomFrame, text=button_info["name"], command=button_info["command"])
    button.grid(row=0, column=i, padx=5, pady=5, sticky="W")


#divider
dividerLabel = Label(bottomBox, text="  s  ", padx=200)
dividerLabel.grid(column=2, row=0)


buttonDataBottomRight = [
    {"name": "Get Check", "command": getCheck},
    {"name": "Recipe", "command": getRecipe},
    {"name": "Quantity", "command": getQuantity},
    {"name": "Repeat", "command": repeat},
    {"name": "Modify", "command": modify},
    {"name": "Delete", "command": delete},
    {"name": "Rapid Fire", "command": rapidFire}
]

for i, button_info in enumerate(buttonDataBottomRight):
    button = Button(bottomFrame, text=button_info["name"], command=button_info["command"])
    button.grid(row=0, column=abs(i-12), padx=5, pady=5, sticky='WEN')


### |xx|xx|xx|
### |  |  |  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### |  |  |  |
topFrame = LabelFrame(root, text="Top Box", relief='raised',)
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
    button.grid(row=i, column=0, padx=5, pady=5, sticky='WEN')



### Frame anchoring -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
for frame in [entryFrame, scrollFrame, topFrame, bottomFrame, orderFrame]:
    # sticky='nswe' acts like fill='both'
    frame.grid(sticky='NSWE')
    frame.grid_propagate(0)
    

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=5)

root.rowconfigure(1, weight=12)
root.columnconfigure(1, weight=1)

root.rowconfigure(2, weight=1)
root.columnconfigure(2, weight=12)



root.mainloop()