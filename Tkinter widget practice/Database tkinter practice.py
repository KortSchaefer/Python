from tkinter import *
from PIL import ImageTk, Image
#first import !!!!
import sqlite3

root = Tk()
root.title("Image Practice")
root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
root.geometry('400x400')

#create a database or connect to one
conn = sqlite3.connect('address_book.db')  

#create cursor
c = conn.cursor()

#create table
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")



conn.commit()
conn.close()

root.mainloop()