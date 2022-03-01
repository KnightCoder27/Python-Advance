from tkinter import*

window = Tk()
window.title("Simple Calculator")

e = Entry(window, width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#e.pack()
#e.insert(0, "Enter Your Name")

def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))
    
def button_clear():
    e.delete(0,END)

def button_add():
    f_num = e.get()
    global num1
    num1 = int(f_num)
    e.delete(0, END)

def button_equal():
    s_number = e.get()
    e.delete(0, END)
    e.insert(0, num1 + int(s_number))



button_1 = Button(window,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2 = Button(window,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3 = Button(window,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4 = Button(window,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5 = Button(window,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6 = Button(window,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7 = Button(window,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8 = Button(window,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9 = Button(window,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0 = Button(window,text="0",padx=40,pady=20,command=lambda: button_click(0))
button_add = Button(window,text="+",padx=39,pady=20,command=button_add)
button_equal = Button(window,text="=",padx=91,pady=20,command=button_equal)
button_clear = Button(window,text="Clear",padx=79,pady=20,command=button_clear)

button_1.grid(row=3 ,column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)

button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column=2)

button_7.grid(row=1 ,column=0)
button_8.grid(row=1 ,column=1)
button_9.grid(row=1 ,column=2)

button_0.grid(row=4 ,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
    

#spam = Label(window, text="Hey People",padx=50,bg="white",fg = "BLUE")
#B = Button(window , text = "Click Here",padx=50, bg = "black", fg="White")
#spam.pack()
#B.pack()

window.mainloop()
