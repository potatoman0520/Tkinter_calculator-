from tkinter import *

win = Tk()
win.geometry("300x400")

#Entry box
e = Entry(win, width=40, borderwidth=5)
e.place(x=0, y=0)

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))
    

#BUTTONS
b = Button(win, text= "0", width= 5, command=lambda:click(0))
b.place(x=30,y=60)

b = Button(win, text= "1", width= 5, command=lambda:click(1))
b.place(x=80,y=60)

b = Button(win, text= "2", width= 5, command=lambda:click(2))
b.place(x=130,y=60)

b = Button(win, text= "3", width= 5, command=lambda:click(3))
b.place(x=30,y=100)

b = Button(win, text= "4", width= 5, command=lambda:click(4))
b.place(x=80,y=100)

b = Button(win, text= "5", width= 5, command=lambda:click(5))
b.place(x=130,y=100)

b = Button(win, text= "6", width= 5, command=lambda:click(6))
b.place(x=30,y=140)

b = Button(win, text= "7", width= 5, command=lambda:click(7))
b.place(x=80,y=140)

b = Button(win, text= "8", width= 5, command=lambda:click(8))
b.place(x=130,y=140)

b = Button(win, text= "9", width= 5, command=lambda:click(9))
b.place(x=30,y=180)

def clear():
    e.delete(0, END)

b = Button(win, text= "CLEAR", width= 12, command= clear)
b.place(x=80,y=180)

def equal():
    n2 = e.get()
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0, i + int (n2))
    elif math == "substraction":
        e.insert(0, i - int (n2))
    elif math == "multiplaction":
        e.insert(0, i * int (n2))
    else:
        e.insert(0, i / int (n2))
    
    
b = Button(win, text= "=", width= 5 ,command= equal)
b.place(x=30,y=180)

def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int (n1)
    e.delete(0, END)

b = Button(win, text= "+", width= 5, command= add)
b.place(x=180,y=60)

def sub():
    n1 = e.get()
    global math
    math = "substraction"
    global i
    i = int (n1)
    e.delete(0, END)

b = Button(win, text= "-", width= 5, command= sub)
b.place(x=180,y=100)

def multi():
    n1 = e.get()
    global math
    math = "multiplation"
    global i
    i = int (n1)
    e.delete(0, END)

b = Button(win, text= "*", width= 5,command= multi)
b.place(x=180,y=140)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int (n1)
    e.delete(0, END)

b = Button(win, text= "/", width= 5, command= div)
b.place(x=180,y=180)




mainloop()