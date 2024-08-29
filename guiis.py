'''from tkinter import *
root = Tk()

button1=Button(root,text= "stop",width=25,command=root.destroy)
#button1.pack()

lable1=Label(root, text='First Name')
lable2=Label(root, text='Last Name')
e1 = Entry(root)
e2 = Entry(root)

lable1.grid(row=0)

lable1.grid(row=1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)






root.mainloop()'''
'''from tkinter import *

master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=E)
mainloop()'''

'''from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
    
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()'''
from tkinter import *

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()



 