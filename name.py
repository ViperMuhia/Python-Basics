name_1=''
name_2 = ''
name_3 = ''
def call_name(name_1, name_2, name_3):
    name_1 =input("Enter your firstr name: \n")
    name_2 = input("Enter your secondr name: \n")
    name_3 = input("Enter your secondr name: \n")

    if name_2 == '':
        full_name = print("Your name is " +name_1 +" "+ name_3 )
        return full_name
    else:
        full_name = print(f"Your name is {name_1}  {name_2} {name_3}")
        return full_name
    

