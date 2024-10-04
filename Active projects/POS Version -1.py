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


fontSize = int(screen_width/160)
orderCostTotal = 0

###
###   Definition space
###

#def hide_all_buttons():
#    for widget in frame.winfo_children():  # Loop through all children in the frame
#        widget.grid_forget()  
            


def softDrinks():
    global orderCostTotal
    global fontSize
    global orderFrame
    global entryFrame
    
    # all of the soft drink buttons
    

    def coke():
        global orderCostTotal
        Label(orderFrame, text="Coke").grid(row=0, column=0)
        Label(orderFrame, text="3.49").grid(row=0, column=2)
        orderCostTotal += 3.49
    def dietCoke():
        global orderCostTotal
        Label(orderFrame, text="dietCoke").grid(row=0, column=0)
        Label(orderFrame, text="3.49").grid(row=0, column=2)
        orderCostTotal += 3.49
    def sprite():
        global orderCostTotal
        Label(orderFrame, text="sprite").grid(row=0, column=0)
        Label(orderFrame, text="3.49").grid(row=0, column=2)
        orderCostTotal += 3.49
    def mrPib():
        global orderCostTotal
        Label(orderFrame, text="mrPib").grid(row=0, column=0)
        Label(orderFrame, text="3.49").grid(row=0, column=2)
        orderCostTotal += 3.49
    #setting grid weight
    entryFrame.columnconfigure((0,5), weight=1)
    cokeButton = Button(entryFrame, text="Coke", command=coke, padx=fontSize*3, pady=fontSize, font=("Arial", fontSize)).grid(row=0, column=1, padx=fontSize, pady=fontSize)
    dietCokeButton = Button(entryFrame, text="Diet Coke", command=dietCoke, padx=fontSize*3, pady=fontSize, font=("Arial", fontSize)).grid(row=0, column=2, padx=fontSize, pady=fontSize)
    spriteButton = Button(entryFrame, text="Sprite", command=sprite, padx=fontSize*3, pady=fontSize, font=("Arial", fontSize)).grid(row=0, column=3, padx=fontSize, pady=fontSize)
    mrPibButton = Button(entryFrame, text="Mr. Pib", command=mrPib, padx=fontSize*3, pady=fontSize, font=("Arial", fontSize)).grid(row=0, column=4, padx=fontSize, pady=fontSize)
    
    #Seccond set of buttons
    def lemonade():
        global orderCostTotal
        Label(orderFrame, text="lemonaid").grid(row=0, column=0)
        Label(orderFrame, text="3.49").grid(row=0, column=2)
        orderCostTotal += 3.49
    def mellowYellow():
        global orderCostTotal
        Label(orderFrame, text="mellowYellow").grid(row=0, column=0)
        Label(orderFrame, text="3.49").grid(row=0, column=2)
        orderCostTotal += 3.49
    def cokeZero():
        global orderCostTotal
        Label(orderFrame, text="cokeZero").grid(row=0, column=0)
        Label(orderFrame, text="3.49").grid(row=0, column=2)
        orderCostTotal += 3.49
    def fruitPunch():
        global orderCostTotal
        Label(orderFrame, text="fruitPunch").grid(row=0, column=0)
        Label(orderFrame, text="3.49").grid(row=0, column=2)
        orderCostTotal += 3.49
    
    lemonadeButton = Button(entryFrame, text="Lemonade", command=lemonade, padx=fontSize*3, pady=fontSize, font=("Arial", fontSize)).grid(row=1, column=1, padx=fontSize, pady=fontSize)
    mellowYellowButton = Button(entryFrame, text="Mellow\nYellow", command=mellowYellow, padx=fontSize*3, pady=fontSize, font=("Arial", fontSize)).grid(row=1, column=2, padx=fontSize, pady=fontSize)
    cokeZeroButton = Button(entryFrame, text="Coke\nZero", command=cokeZero, padx=fontSize*3, pady=fontSize, font=("Arial", fontSize)).grid(row=1, column=3, padx=fontSize, pady=fontSize)
    fruitPunchButton = Button(entryFrame, text="Fruit\nPunch", command=fruitPunch, padx=fontSize*3, pady=fontSize, font=("Arial", fontSize)).grid(row=1, column=4, padx=fontSize, pady=fontSize)


def teaSpecial():
    print("Button 2 pressed!")

def apps():
    print("Button 3 pressed!")

def appsMeal():
    print("Button 4 pressed!")

def sideSalads():
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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
scrollFrame.grid_columnconfigure(0, weight=1)

### |xx|xx|xx|
### |  |  |  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### |  |  |  |
topFrame = LabelFrame(root, text="Top Box", relief='raised',)
topFrame.grid(column=0, row=0, padx=2, pady=2,columnspan=4)
orderBox= Label(topFrame, text='Box').pack()

### |  |  |  |
### |  |  |  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### |xx|xx|xx|
bottomLeftFrame = LabelFrame(root, text="Bottom Box", relief='raised',)
bottomLeftFrame.grid(column=0, row=2, padx=2, pady=2,)
bottomBox= Label(bottomLeftFrame, text='Box')
bottomBox.grid(column=0, row=0)

bottomFrame = LabelFrame(root, text="Bottom Box", relief='raised',)
bottomFrame.grid(column=1, row=2, padx=2, pady=2,)
bottomBox= Label(bottomFrame, text='Box')
bottomBox.grid(column=0, row=0)

bottomRightFrame = LabelFrame(root, text="Bottom Box", relief='raised',)
bottomRightFrame.grid(column=2, row=2, padx=2, pady=2,)
bottomBox= Label(bottomRightFrame, text='Box')
bottomBox.grid(column=0, row=0)



### Button Creation bottom left-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

buttonDataBottomLeft = [
    {"name": "Close", "command": close},
    {"name": "Next Seat", "command": nextSeat}
    
]

for i, button_info in enumerate(buttonDataBottomLeft):
    button = Button(bottomLeftFrame, text=button_info["name"], command=button_info["command"], font=("Arial", fontSize), padx=20, pady=5)
    button.grid(row=0, column=i, padx=5, pady=5, sticky="W")

### Button Creation bottom right -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



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
    button = Button(bottomRightFrame, text=button_info["name"], command=button_info["command"], font=("Arial", fontSize), padx=20, pady=5)
    button.grid(row=0, column=abs(i-12), padx=5, pady=5, sticky='EN')




### Buttons for scrollFrame -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
buttonData = [
    {"name": "Soft Drinks", "command": softDrinks},
    {"name": "Tea & Special", "command": teaSpecial},
    {"name": "Apps", "command": apps},
    {"name": "Apps\nas meal", "command": appsMeal},
    {"name": "Side\nsalads", "command": sideSalads},
]


for i, button_info in enumerate(buttonData):
    button = Button(scrollFrame, text=button_info["name"], command=button_info["command"], font=("Arial", fontSize))
    button.grid(row=i, column=0, padx=5, pady=5, sticky='WEN')



### Frame anchoring -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
for frame in [entryFrame, scrollFrame, topFrame, bottomFrame, orderFrame, bottomLeftFrame, bottomRightFrame]:
    # sticky='nswe' acts like fill='both'
    frame.grid(sticky='NSWE')
    frame.grid_propagate(0)
    


# Set row and column configuration for each frame ------------------------------------------------------------------------------------------------------------------------------------------------------------
root.rowconfigure(0, weight=2)
root.columnconfigure(0, weight=12)

root.rowconfigure(1, weight=24)
root.columnconfigure(1, weight=3)

root.rowconfigure(2, weight=2)
root.columnconfigure(2, weight=24)



root.mainloop()