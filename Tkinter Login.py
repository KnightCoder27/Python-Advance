from tkinter import *
window = Tk()
window.title("Login Page")

L1 = Label(window,text="Enter your Login ID: ",fg="black")
L1.pack()
E1 = Entry(window,text = "Login ID",width=50,borderwidth=5)
E1.pack()

L2 = Label(window,text="Enter your Password: ",fg="black")
L2.pack()
E2 = Entry(window,text = "Password",width=50,borderwidth=5)
E2.pack()

CB = Checkbutton(window,text = "Registered?",onvalue=1,offvalue=0)
CB.pack()

def click():
    L3 = Label(window,text=f"Email-Id: {E1.get()}",fg="Red")
    L4 = Label(window,text=f"Email-Id: {E2.get()}",fg="Red")
    L3.pack()
    L4.pack()

B = Button(window,text="Sign In",command=click,background="black",fg="white")
B.pack()

window.mainloop()
