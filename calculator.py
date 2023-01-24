from tkinter import*
root =Tk()
root.title("calculator")
e =Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
e.insert(0,"0")

def button_click(num):
    current=e.get()
    e.delete(0,END)

    e.insert(0,str(current)+str(num))

def button_clear(num):
    e.delete(0,END)

def button_add():
    f1=e.get()
    global f_num
    global math
    math="add"
    f_num =int(f1)
    e.delete(0,END)
    
def button_sub():
    f1=e.get()
    global f_num
    global math
    math="sub"
    f_num =int(f1)
    e.delete(0,END)

def button_mul():
    f1=e.get()
    global f_num
    global math
    math="mul"
    f_num =int(f1)
    e.delete(0,END)

def button_div():
    f1=e.get()
    global f_num
    global math
    math="div"
    f_num =int(f1)
    e.delete(0,END)

def button_equal():
    second_number =e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,f_num+int(second_number))
    if math=="mul":
        e.insert(0,f_num*int(second_number))
    if math=="sub":
        e.insert(0,f_num-int(second_number))
    if math=="div":
        e.insert(0,f_num/int(second_number))

b1=Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
b2=Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
b3=Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))

b4=Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
b5=Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
b6=Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))

b7=Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
b8=Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
b9=Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))

b0=Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))

badd=Button(root,text="+",padx=39.5,pady=20,command=button_add)
bsub=Button(root,text="-",padx=41,pady=20,command=button_sub)
bmul=Button(root,text="*",padx=40,pady=20,command=button_mul)
bdiv=Button(root,text="/",padx=40,pady=20,command=button_div)

beq=Button(root,text="   =  ",padx=78.5,pady=20,command=button_equal)
bclear=Button(root,text="clear",padx=78,pady=20,command=lambda: button_clear(0))

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)
bmul.grid(row=4,column=1)
bdiv.grid(row=4,column=2)
bclear.grid(row=5,column=1,columnspan=2) 

bsub.grid(row=5,column=0)
badd.grid(row=6,column=0)
beq.grid(row=6,column=1,columnspan=2)






root.mainloop()