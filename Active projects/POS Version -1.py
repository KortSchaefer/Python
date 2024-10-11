from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("POS System")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
root.configure(bg="lightblue")
#screen width and height variables
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#set fullscreen
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.attributes('-fullscreen', True)
# Bind the ESC key to exit fullscreen
root.bind("<Escape>", lambda event: root.attributes('-fullscreen', False))

###
###   Variables
###

#Screen size variables
fontSize = int(screen_width/160)
button_width = int(screen_width/180)
button_height = int(screen_height/300)
#order total variables
orderCostTotal = 0
currentOrder = []
#list of currently highlighted labels
highlighted_labels = []
seat_orders = {
    "table": [],
    "seat1": [],
    "seat2": [],
    "seat3": [],
    "seat4": [],
    "seat5": [],
    "seat6": [],
    "seat7": [],
    "seat8": [],
    "seat9": [],
    "seat10": [],
    "seat11": [],
    "seat12": [],
    "seat13": [],
    "seat14": [],
    "seat15": [],
    "seat16": [],
    "seat17": [],
    "seat18": [],
    "seat19": [],
    "seat20": [],
}
currentSeat = "table"
#global variable for row and column management
current_row = 0
current_column = 0
max_rows = 60
#PRICE CONFIGURATION
softDrinksPrice = 3.49

###
###   Definition space
###

#def to highlight clicked label
def ifClicked(event):
    global currentSeat
    label = event.widget
    
    if label in highlighted_labels:
        # If it is highlighted, reset its appearance and remove from the list
        label.config(bg="SystemButtonFace", highlightthickness=0)  # Reset color and highlight
        highlighted_labels.remove(label)  # Remove from highlighted list
    else:
        # If it is not highlighted, highlight it and add to the list
        label.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)  # Highlight clicked label
        label.config(bg="yellow")  # Change background color for visibility
        highlighted_labels.append(label)  # Add to highlighted list
        


#def to add current button item to order
def addToOrder(name, price):
    #global variables
    global orderCostTotal
    global fontSize
    global orderFrame
    global orderCostTotal
    global currentSeat
    global seat_orders
    
    if len(seat_orders[currentSeat]) == 0:
        seat_label = Label(orderFrame, text=f"{currentSeat}", font=("Arial", fontSize + 2, "bold"))
        seat_label.grid(row=len(orderFrame.winfo_children()), column=0, padx=10, pady=5, sticky="w")
    #Adding current button item to a list to be proccessed later
    seat_orders[currentSeat].append({"name": name, "price": price})
    #Creating label for current button item
    numSpaces = " " * (100 - (2*len(name)))
    order_label = Label(orderFrame, text=str(name+numSpaces+"$"+str(price)), cursor="hand2")
    order_label.grid(row=len(orderFrame.winfo_children()), column=0, padx=10, pady=5, sticky="w")
    # Bind the click event to the created label
    order_label.bind("<Button-1>", ifClicked)
    #Adding price to total
    orderCostTotal += price
    

def setCurrentSeat(seat_number):
    global currentSeat
    global seat_orders

    # Check if the seat_number exists in seat_orders
    if seat_number in seat_orders:
        currentSeat = seat_number
        print(f"Current seat set to {currentSeat}")
    else:
        print(f"Seat {seat_number} does not exist")
#First soft drink window def. WORKS!!!
def softDrinks():
    global orderCostTotal
    global fontSize
    global orderFrame
    global entryFrame
    global button_width
    global button_height
    #setting buttons to middle
    entryFrame.columnconfigure((0,5), weight=1)
    # row and column offset vars for positioning
    rOffest = 0
    cOffest = 0
    # blank function that does nothing
    def blank():
        pass
    # Updated buttons data with new drinks
    buttonDataSoftDrinks = [
    {"name": "Coke", "command": lambda: addToOrder('Coke', softDrinksPrice)},
    {"name": "Diet Coke", "command": lambda: addToOrder('Diet Coke', softDrinksPrice)},
    {"name": "Sprite", "command": lambda: addToOrder('Sprite', softDrinksPrice)},
    {"name": "Mr. Pib", "command": lambda: addToOrder('Mr. Pib', softDrinksPrice)},
    {"name": "Lemonade", "command": lambda: addToOrder('Lemonade', softDrinksPrice)},
    {"name": "Mellow\nYellow", "command": lambda: addToOrder('Mellow Yellow', softDrinksPrice)},
    {"name": "Coke\nZero", "command": lambda: addToOrder('Coke Zero', softDrinksPrice)},
    {"name": "Fruit\nPunch", "command": lambda: addToOrder('Fruit Punch', softDrinksPrice)},
    {"name": "Tonic Water", "command": lambda: addToOrder('Tonic Water', softDrinksPrice)},    
    {"name": "Root Beer", "command": lambda: addToOrder('Root Beer', softDrinksPrice)},        
    {"name": "Dr Pepper", "command": lambda: addToOrder('Dr Pepper', softDrinksPrice)},        
    {"name": "Rasp Tea Ftn", "command": lambda: addToOrder('Rasp Tea Ftn', softDrinksPrice)},
    {"name": " ", "command": blank}, 
    {"name": " ", "command": blank}, 
    {"name": " ", "command": blank}, 
    {"name": " ", "command": blank}, 
    {"name": "Sweet Tea", "command": lambda: addToOrder('Sweet Tea', softDrinksPrice)},
    {"name": "Hot Tea", "command": lambda: addToOrder('Hot Tea', softDrinksPrice)},  
    {"name": "Coffee", "command": lambda: addToOrder('Coffee', softDrinksPrice)},    
    {"name": "Iced Tea", "command": lambda: addToOrder('Iced Tea', softDrinksPrice)},
    {"name": " ", "command": blank},   
    {"name": "Hot Cocoa", "command": lambda: addToOrder('Hot Cocoa', softDrinksPrice)},    
    {"name": "Decaf Coffee", "command": lambda: addToOrder('Decaf Coffee', softDrinksPrice)},
    {"name": " ", "command": blank},  
    {"name": "No Bev", "command": lambda: addToOrder('No Bev', softDrinksPrice)},
    {"name": " ", "command": blank},  
    {"name": " ", "command": blank},  
    {"name": "Water", "command": lambda: addToOrder('Water', softDrinksPrice)}     
]

    #for loop adding the buttons onto the screen
    for i, button_info in enumerate(buttonDataSoftDrinks):
        if button_info["name"] == " ":
                cOffest += 1
                button = Button(entryFrame, text=button_info["name"], command=button_info["command"], font=("Arial", fontSize), padx=20, pady=5, width=button_width, height=button_height, state=DISABLED, highlightthickness=0, borderwidth=0)
                button.grid(row=rOffest, column=cOffest, padx=15, pady=15, sticky="W")
                if cOffest == 4:
                    cOffest = 0;rOffest += 1
        else:
            cOffest += 1
            button = Button(entryFrame, text=button_info["name"], command=button_info["command"], font=("Arial", fontSize), padx=20, pady=5, width=button_width, height=button_height)
            button.grid(row=rOffest, column=cOffest, padx=15, pady=15, sticky="W")
            if cOffest == 4:
                cOffest = 0;rOffest += 1
    
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
    global current_row, current_column  # Track row and column

    # Create duplicates of highlighted labels
    for label in highlighted_labels:
        duplicate_label = Label(orderFrame, text=label.cget('text'), fg="blue", cursor="hand2")
        duplicate_label.bind("<Button-1>", ifClicked)  # Bind the click event to duplicates too
        
        # Place in the grid, increment row, and manage column wrapping
        duplicate_label.grid(row=current_row, column=current_column, padx=10, pady=5)
        
        current_row += 1  # Move to the next row
        if current_row >= max_rows:  # When max rows is reached, move to the next column
            current_row = 0  # Reset to row 0
            current_column += 1  # Move to the next column

def modify():
    pass

def delete():
    for label in highlighted_labels.copy():
        label.destroy()  # Destroy the label
    highlighted_labels.clear()
    

def rapidFire():
    print('Get check')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def close():
    print('close')

def nextSeat():
    global currentSeat
    if currentSeat == 'table':
        currentSeat = 'seat1'
    elif currentSeat == 'seat20':
        pass
    else:
        currentSeat = 'seat' + str(int(currentSeat[-1]) + 1)


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