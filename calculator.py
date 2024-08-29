from tkinter import *

root = Tk()

root.title("Muhia calculation")
#root.iconbitmap()

e = Entry(root,width=50,borderwidth=30)
e.grid(row=0,column=0,padx=10,pady=10,columnspan=3)

def click(num):
    cur = e.get()
    e.delete(0,END)
    e.insert(0,  str(cur)+ str(num) )
    
    
def click_add():
    first_num=e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0,END)
def click_clear():
    e.delete(0,END)





def click_sub():
    first_num=e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0,END)


def click_equals():
    if math == "addition":
        second_num = e.get()
        e.delete(0,END)
        e.insert(0,f_num + int(second_num))
    else:
        second_num = e.get()
        e.delete(0,END)
        e.insert(0,f_num - int(second_num))





mybutton1=Button(root,text="1",padx=40,pady=20,command= lambda :click(1))
mybutton2=Button(root,text="2",padx=40,pady=20,command= lambda :click(2))
mybutton3=Button(root,text="3",padx=40,pady=20,command= lambda :click(3))
mybutton4=Button(root,text="4",padx=40,pady=20,command= lambda :click(4))
mybutton5=Button(root,text="5",padx=40,pady=20,command= lambda :click(5))
mybutton6=Button(root,text="6",padx=40,pady=20,command= lambda :click(6))
mybutton7=Button(root,text="7",padx=40,pady=20,command= lambda :click(7))
mybutton8=Button(root,text="8",padx=40,pady=20,command= lambda :click(8))
mybutton9=Button(root,text="9",padx=40,pady=20,command= lambda :click(9))
mybutton0=Button(root,text="0",padx=40,pady=20,command= lambda :click(0))
mybuttonadd=Button(root,text="+",padx=40,pady=20,command= lambda :click_add())
mybuttonsub=Button(root,text="-",padx=40,pady=20,command= lambda :click_sub())
mybuttonequals=Button(root,text="=",padx=110,pady=20,command= lambda :click_equals())
mybuttonclear=Button(root,text="clear",padx=40,pady=20,command= lambda :click_clear())

mybutton9.grid(row=1,column=2)
mybutton8.grid(row=1,column=1)
mybutton7.grid(row=1,column=0)

mybutton6.grid(row=2,column=2)
mybutton5.grid(row=2,column=1)
mybutton4.grid(row=2,column=0)

mybutton3.grid(row=3,column=2)
mybutton2.grid(row=3,column=1)
mybutton1.grid(row=3,column=0)

mybutton0.grid(row=4,column=0)
mybuttonequals.grid(row=4,column=1,columnspan=2)

mybuttonadd.grid(row=5,column=0)
mybuttonsub.grid(row=5,column=1)
mybuttonclear.grid(row=5,column=2)





root.mainloop()