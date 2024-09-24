from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("POS System")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
root.configure(bg="lightblue")





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
scrollFrame = LabelFrame(root, text="Scroll Box", width=40, height=300, relief='raised',)
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
some_label = Label(orderFrame, text='Simple Text')
some_button = Button(topFrame, text='Quit', command=root.destroy)


### Frame anchoring
for frame in [entryFrame, scrollFrame, topFrame, bottomFrame, orderFrame]:
    # sticky='nswe' acts like fill='both'
    frame.grid(sticky='nswe')
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.grid_propagate(0)

for widget in [some_label, some_button]:
    # sticky='wse' acts like fill='x' + anchor='s'
    widget.grid(sticky='wse')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()