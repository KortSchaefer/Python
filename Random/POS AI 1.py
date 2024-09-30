from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("POS System")



root.configure(bg="lightblue")

# Scroll function definitions
def scroll1():
    print("Soft Drinks selected!")

def scroll2():
    print("Tea & Special selected!")

def scroll3():
    print("Apps selected!")

def scroll4():
    print("Apps as meal selected!")

def scroll5():
    print("Side salads selected!")


# Configure the root window to be resizable and responsive
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(1, weight=1)  # Adjust this for row 1 where the frames are located

# ---- Order Frame (Left) ----
orderFrame = LabelFrame(root, text="Order Box", width=100, height=300, relief='raised', bg='white')
orderFrame.grid_propagate(False)  # Prevent the frame from resizing based on content
orderFrame.grid(column=0, row=1, padx=(15, 2), pady=2, sticky='nsew')

# Add content to orderFrame
orderLabel = Label(orderFrame, text='Order Box')
orderLabel.pack(fill=BOTH, expand=True)

# ---- Entry Frame (Right) ----
entryFrame = LabelFrame(root, text="Entry Box", width=250, height=300, relief='raised', bg='white')
entryFrame.grid_propagate(False)
entryFrame.grid(column=2, row=1, padx=(2, 15), pady=2, sticky='nsew')

# Add content to entryFrame
entryLabel = Label(entryFrame, text='Entry Box')
entryLabel.pack(fill=BOTH, expand=True)

# ---- Scroll Frame (Middle) ----
scrollFrame = LabelFrame(root, text="Scroll Box", width=40, height=300, relief='raised', bg='white')
scrollFrame.grid_propagate(False)
scrollFrame.grid(column=1, row=1, padx=2, pady=2, sticky='nsew')

# Add a scrollbar to the scrollFrame
scrollbar = Scrollbar(scrollFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

# Add a canvas inside the scrollFrame to enable scrolling
scrollCanvas = Canvas(scrollFrame, yscrollcommand=scrollbar.set, width=40, height=300)
scrollCanvas.pack(side=LEFT, fill=BOTH, expand=True)

# Add the buttons to the canvas
buttonFrame = Frame(scrollCanvas)
scrollCanvas.create_window((0, 0), window=buttonFrame, anchor='nw')

# Configure the scrollbar
scrollbar.config(command=scrollCanvas.yview)

# Populate buttons in the scrollFrame
buttonData = [
    {"name": "Soft Drinks", "command": scroll1},
    {"name": "Tea & Special", "command": scroll2},
    {"name": "Apps", "command": scroll3},
    {"name": "Apps\nas meal", "command": scroll4},
    {"name": "Side\nsalads", "command": scroll5}
]

# Create buttons in scrollFrame
for i, button_info in enumerate(buttonData):
    button = Button(buttonFrame, text=button_info["name"], command=button_info["command"])
    button.grid(row=i, column=0, padx=5, pady=5)

# Make the canvas scrollable when the content exceeds its size
def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

buttonFrame.bind("<Configure>", lambda event, canvas=scrollCanvas: on_frame_configure(canvas))


# ---- Bottom Frame (Bottom) ----
bottomFrame = LabelFrame(root, text="Bottom Box", width=430, height=50, relief='raised', bg='white')
bottomFrame.grid_propagate(False)
bottomFrame.grid(column=0, row=3, padx=2, pady=2, columnspan=3, sticky='nsew')

# Add content to bottomFrame
bottomLabel = Label(bottomFrame, text='Bottom Box')
bottomLabel.pack(fill=BOTH, expand=True)

# ---- Top Frame (Top) ----
topFrame = LabelFrame(root, text="Top Box", width=430, height=50, relief='raised', bg='white')
topFrame.grid_propagate(False)
topFrame.grid(column=0, row=0, padx=2, pady=2, columnspan=3, sticky='nsew')

# Add content to topFrame
topLabel = Label(topFrame, text='Top Box')
topLabel.pack(fill=BOTH, expand=True)

# Set row and column configuration for each frame
for frame in [orderFrame, entryFrame, scrollFrame, topFrame, bottomFrame]:
    frame.grid(sticky='nsew')

# Make rows and columns within frames expand to fill available space
for i in range(3):
    root.columnconfigure(i, weight=1)

root.mainloop()
