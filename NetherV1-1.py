from tkinter import *

root = Tk()
root.title("Nether Portal Cords V 1.0")
root.geometry("500x300")


###Functions
###Overworld to nether def
def button1():
    x1 = xover.get()
    y1 = yover.get()
    nam = name.get()
    x2=float(x1)/8
    y2=float(y1)/8
    document= Label(root, text=str(nam+"   Overworld  X: "+str(x1)+" Z: "+str(y1)+"     Nether  X: "+str(x2)+" Z: "+str(y2)))
    document.grid(row=4,column=0,columnspan=6, padx=10, pady=10)
    

###Frames
entryFrame = LabelFrame(root, text="test", padx=5, pady=5)
entryFrame.pack(padx=10, pady=10)
###Labels
label1= Label(root, text="Only enter 1 set of coords")
label1.grid(row=0,column=0,columnspan=3)

label2= Label(root, text="Click if you entered:")
label2.grid(row=0,column=6,columnspan=3,)

label3= Label(root, text="X coord:")
label3.grid(row=1,column=1)

label4= Label(root, text="Z coord:")
label4.grid(row=1,column=2)

label5= Label(root, text="X coord:")
label5.grid(row=1,column=4)

label6= Label(root, text="Z coord:")
label6.grid(row=1,column=5)
###Overword Buttons
label2= Label(root, text="Overworld: ")
label2.grid(row=2,column=0)

xover = Entry(root, width=8)
xover.grid(row=2,column=1,padx=3)


yover = Entry(root, width=8)
yover.grid(row=2,column=2,padx=3)

###Nether buttons

label3= Label(root, text="Nether: ")
label3.grid(row=2,column=3)

xnet = Entry(root, width=8)
xnet.grid(row=2,column=4,padx=3)


ynet = Entry(root, width=8)
ynet.grid(row=2,column=5,padx=3)


###Name

label4= Label(root, text="Name: ")
label4.grid(row=3,column=0)

name = Entry(root, width=18)
name.grid(row=3,column=1,padx=3,columnspan=2)

###Buttons

button1 = Button(root, text="Overworld Coords", width=14, command=button1)
button1.grid(row=2,column=6, padx=5, pady=5)

button2 = Button(root, text="Nether Coords", width=14, command=button1)
button2.grid(row=3,column=6, padx=5, pady=5)









root.mainloop()