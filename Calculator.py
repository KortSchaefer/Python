from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)
##All opperation buttons
def button_plus():
    first = e.get()
    global f_num
    f_num = int(first)
    global opp
    opp=str("+")
    e.delete(0,END)
def button_sub():
    first = e.get()
    global f_num
    f_num = int(first)
    global opp
    opp=str("-")
    e.delete(0,END)
def button_mul():
    first = e.get()
    global f_num
    f_num = int(first)
    global opp
    opp=str("x")
    e.delete(0,END)
def button_div():
    first = e.get()
    global f_num
    f_num = int(first)
    global opp
    opp=str("/")
    e.delete(0,END)
#equal  func
def button_eq():
    if str(opp) == "+":
        seccond=e.get()
        e.delete(0,END)
        sum=int(f_num)+int(seccond)
        e.insert(0,str(sum))
    elif str(opp) == "-":
        seccond=e.get()
        e.delete(0,END)
        sum=int(f_num)-int(seccond)
        e.insert(0,str(sum))
    elif str(opp) == "x":
        seccond=e.get()
        e.delete(0,END)
        sum=int(f_num)*int(seccond)
        e.insert(0,str(sum))
    elif str(opp) == "/":
        seccond=e.get()
        e.delete(0,END)
        sum=int(f_num)/int(seccond)
        safesum=int(sum)
        e.insert(0,str(safesum))
    else:
        return

    



button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0))
buttonAdd = Button(root, text="+", padx=39, pady=20, command=button_plus)
buttonSub = Button(root, text="-", padx=39, pady=20, command=button_sub)
buttonMul = Button(root, text="x", padx=39, pady=20, command=button_mul)
buttonDiv = Button(root, text="/", padx=39, pady=20, command=button_div)
buttonEq = Button(root, text="=", padx=91, pady=20, command=button_eq)
buttonClear = Button(root, text="Clear", padx=71, pady=20, command=button_clear)

#buttons on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonAdd.grid(row=5, column=0)
buttonEq.grid(row=5, column=1, columnspan=2)

buttonClear.grid(row=4, column=1, columnspan=2)

buttonSub.grid(row=6, column=0)
buttonMul.grid(row=6, column=1)
buttonDiv.grid(row=6, column=2)

    
root.mainloop()