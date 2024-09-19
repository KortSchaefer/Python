from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")

myimg1 = ImageTk.PhotoImage(Image.open("C:/Users/Kingc/Documents/Code/Python/Practice Images/stare1.png"))
myimg2 = ImageTk.PhotoImage(Image.open("C:/Users/Kingc/Documents/Code/Python/Practice Images/stare2.png"))
myimg3 = ImageTk.PhotoImage(Image.open("C:/Users/Kingc/Documents/Code/Python/Practice Images/stare3.png"))
myimg4 = ImageTk.PhotoImage(Image.open("C:/Users/Kingc/Documents/Code/Python/Practice Images/stare4.png"))
myimg5 = ImageTk.PhotoImage(Image.open("C:/Users/Kingc/Documents/Code/Python/Practice Images/stare5.png"))
myimg6 = ImageTk.PhotoImage(Image.open("C:/Users/Kingc/Documents/Code/Python/Practice Images/stare.png"))
statusb = 1
img_list = [myimg1, myimg2, myimg3, myimg4, myimg5, myimg6]



status = Label(root, text="Image "+str(statusb)+" of "+str(len(img_list)),bd=1, relief=SUNKEN, anchor=E)


mylabel = Label(image=myimg1)
mylabel.grid(row=0, column=0, columnspan=3)

def forward(num):
   global mylabel
   global button_forward
   global button_back
   global statusb
   global status

   mylabel.grid_forget()
   mylabel = Label(image=img_list[num-1])
   button_forward = Button(root, text=">>", command=lambda: forward(num+1))
   button_back = Button(root, text="<<", command=lambda: back(num-1))
   statusb += 1
   status.grid_forget()
   status = Label(root, text="Image "+str(statusb)+" of "+str(len(img_list)),bd=1, relief=SUNKEN, anchor=E)
   status.grid(row=2, column=0, columnspan=3,sticky=W+E)

   if num == 6:
      button_forward = Button(root, text=">>", state=DISABLED)

   button_back.grid(column=0, row=1)
   button_forward.grid(column=2, row=1)
   mylabel.grid(row=0, column=0, columnspan=3)
   
   return

def back(num):
   global mylabel
   global button_forward
   global button_back
   global statusb
   global status

   mylabel.grid_forget()
   mylabel = Label(image=img_list[num-1])
   button_forward = Button(root, text=">>", command=lambda: forward(num+1))
   button_back = Button(root, text="<<", command=lambda: back(num-1))

   if num == 1:
      button_back = Button(root, text="<<", state=DISABLED)

   button_back.grid(column=0, row=1)
   button_forward.grid(column=2, row=1)

   mylabel.grid(row=0, column=0, columnspan=3)
   statusb-=1
   status.grid_forget()
   status = Label(root, text="Image "+str(statusb)+" of "+str(len(img_list)),bd=1, relief=SUNKEN, anchor=E)
   status.grid(row=2, column=0, columnspan=3,sticky=W+E)
   return



button_back = Button(root, text="<<", command=back , state=DISABLED)
button_back.grid(column=0, row=1)


button_forward = Button(root, text=">>", command=lambda: forward(2))
button_forward.grid(column=2, row=1)

status.grid(row=2, column=0, columnspan=3,sticky=W+E)


bquit = Button(root, text="Quit", command=root.quit)
bquit.grid(column=1, row=1)


root.mainloop()