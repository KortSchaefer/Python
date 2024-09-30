from tkinter import *
from PIL import ImageTk, Image
#have to import file system from tkinter
from tkinter import filedialog

# Esentialy allows user to select image/any file to use in the program

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir=r"\Users\Kingc\Documents\Code\Python", title='select a file', filetypes=(("png files","*.png"),("all files", "*.*")) )
    myLabel = Label(root,text =root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(root, image=my_image).pack()

mybtn = Button(root, text='open file', command = open).pack()



root.mainloop()