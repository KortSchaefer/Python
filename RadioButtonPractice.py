from tkinter import *
from PIL import ImageTk, Image

root= Tk()

r = IntVar()
r.set('1')
r2 = IntVar()

MODES = [
    ('Pepperoni', 'a'),
    ('Cheese', 'b'),
    ('Mushroom', 'c'),
    ('Onion', 'd')
]

pizza = StringVar()
pizza.set("Pepperoni")

frame = LabelFrame(root, text="Old Code", padx=50, pady=50)
frame.pack(padx=10, pady=10)

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value,)
    myLabel.pack()

Radiobutton(frame, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(frame, text="Option 1", variable=r, value=2, command=lambda: clicked(r.get())).pack()

b1 = Button(root, text="click Me", command=lambda: clicked(pizza.get()))
b1.pack()

Radiobutton(frame, text="Option 1", variable=r2, value=1).pack()
Radiobutton(frame, text="Option 1", variable=r2, value=2).pack()

root.mainloop()