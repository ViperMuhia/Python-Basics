'''from tkinter import *

root = Tk()

root.title("Simple Calc")

e = Entry(root, width= 30,borderwidth=20)
e.pack()
e.insert(0,"please insert your name")



def clickme():
   
    mylabel =Label(root,text= "Hello"+e.get())
    mylabel.pack()

#mybutton = Button(root,text="Click me ",state= 'disabled')
#e.delete(0,END)
mybutton = Button(root,text="Enter your name",padx=10,pady=2,command= clickme,fg="red",bg= "Black")


mybutton.pack()
'''

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter IntVar Example")

# Create an IntVar for the Checkbutton
check_var = tk.IntVar()

# Function to display the current value of check_var
def show_check_value():
    print(f"Checkbutton value: {check_var.get()}")

# Create a Checkbutton
check_button = tk.Checkbutton(root, text="Check me", variable=check_var, command=show_check_value)
check_button.grid(row=0, column=0)

# Create an IntVar for the Radiobuttons
radio_var = tk.IntVar()

# Function to display the current value of radio_var
def show_radio_value():
    print(f"Selected Radiobutton value: {radio_var.get()}")

# Create Radiobuttons
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value=1, command=show_radio_value)
radio_button1.grid(row=1, column=0)

radio_button2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value=2, command=show_radio_value)
radio_button2.grid(row=2, column=0)

radio_button3 = tk.Radiobutton(root, text="Option 3", variable=radio_var, value=3, command=show_radio_value)
radio_button3.grid(row=3, column=0)

# Start the Tkinter event loop
root.mainloop()


























'''def clickme():
    mylabel =Label(root,text="You clicked me")
    mylabel.pack()

#mybutton = Button(root,text="Click me ",state= 'disabled')
mybutton = Button(root,text="Click me ",padx=10,pady=2,command= clickme,fg="red",bg= "Black")


mybutton.pack()'''























#defining labels
'''myLabel = Label(root,text="Hello World")
myLabe2 = Label(root,text="Hello You")
myLabe3 = Label(root,text="Hello Wewe")
myLabe4 = Label(root,text="Hello kenya")


myLabel.grid(row=0,column=0)
myLabe2.grid(row=1,column=0)
myLabe3.grid(row=2,column=0)
myLabe4.grid(row=3,column=0)'''

root.mainloop()