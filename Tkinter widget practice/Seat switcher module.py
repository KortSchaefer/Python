from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
root.geometry('400x400')
seatItter = 0
def leftButton():
     pass
def addScrollButtons():
    global orderScrollFrame
    left = Button(orderScrollFrame, text="Left", command=leftButton).grid(row=1, column=0, sticky="ew")
def addSeatButton():
    global seatItter
    global orderScrollFrame
    if seatItter < 5:
        seatIndexButton = Button(orderScrollFrame, text=str('seat ' + str(seatItter+1))).grid(row=1, column=(seatItter+1), sticky="ews",pady=30 )
        seatItter += 1
    else:
        addScrollButtons()

orderScrollFrame = LabelFrame(root, text="Order Box", relief='raised', bg='white')
orderScrollFrame.grid_propagate(False)
orderScrollFrame.grid(column=0, row=0, padx=(15, 2), pady=2, sticky='nsew')
#invisable labels to set up the orderFrame
for i in range(7):  # Create 7 columns
        # Create a label with a specific text, you can modify the text as needed
        label = Label(orderScrollFrame, text='', borderwidth=2, relief="groove")
        # Place the label in the first row and the i-th column
        label.grid(row=1, column=i, sticky="ew")  # 'ew' makes the label expand horizontally
        # Configure column weight to allow the labels to expand equally
        orderScrollFrame.grid_columnconfigure(i, weight=1)




testButton = Button(orderScrollFrame, text="test", command=addSeatButton).grid(row=0, column=0)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()