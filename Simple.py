from tkinter import *

root = Tk()
root.geometry("350x400")

e = Entry(root, width= 50,borderwidth=20)
e.grid(row=0, column=0,columnspan = 4,padx=10,pady=10)
#e.insert(0,"please insert your name")


def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)
def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0,END)
def button_equal():
    second_num = e.get()
    e.delete(0,END)

    if math == "addition" :
        e.insert(0, f_num + (int(second_num)))

 
mybutton1 = Button(root,text="1",padx=40,pady=20,command= lambda:button_click(1))
mybutton2 = Button(root,text="2",padx=40,pady=20,command= lambda:button_click(2))
mybutton3 = Button(root,text="3",padx=40,pady=20,command= lambda:button_click(3))
mybutton4 = Button(root,text="4",padx=40,pady=20,command= lambda:button_click(4))
mybutton5 = Button(root,text="5",padx=40,pady=20,command= lambda:button_click(5))
mybutton6 = Button(root,text="6",padx=40,pady=20,command= lambda:button_click(6))
mybutton7 = Button(root,text="7",padx=40,pady=20,command= lambda:button_click(7))
mybutton8 = Button(root,text="8",padx=40,pady=20,command= lambda:button_click(8))
mybutton9 = Button(root,text="9",padx=40,pady=20,command= lambda:button_click(9))
mybutton0 = Button(root,text="0",padx=40,pady=20,command= lambda:button_click(0))
mybuttonadd= Button(root,text="+",padx=39,pady=20,command= lambda:button_add())
mybuttonequal = Button(root,text="=",padx=91,pady=20,command= lambda:button_equal())
mybuttonClear = Button(root,text="Clear",padx=79,pady=20,command= lambda:button_click())



mybutton1.grid(row=3,column=0)
mybutton2.grid(row=3,column=1)
mybutton3.grid(row=3,column=2)

mybutton4.grid(row=2,column=0)
mybutton5.grid(row=2,column=1)
mybutton6.grid(row=2,column=2)

mybutton7.grid(row=1,column=0)
mybutton8.grid(row=1,column=1)
mybutton9.grid(row=1,column=2)

mybutton0.grid(row=4,column=0)
mybuttonadd.grid(row=5,column=0)
mybuttonequal.grid(row=5,column=1,columnspan = 2)
mybuttonClear.grid(row=4,column=1,columnspan = 2)




root.mainloop()