from name import call_name

name_1=''
name_2 = ''
name_3 = ''
call_name(name_1,name_2,name_3)


toppings = []
max_of_toppings = 0
print("**********Welcome to our pizza in company************\nYou are only allowed to enter a maximum of 6 toppings at a time")
print("Please select from the list below : \n ")

while max_of_toppings < 7:
    user_choice=int(input("\t1:chicken\n\t2:beef\n\t3:Fruit\n\t4:mashrooms\n\t5:pork\n\t6:yams\n\t7:quit \n choice : "))
    if user_choice == 1:
        print("Adding chiicken to the topping") 
        toppings.append("chicken")
    elif user_choice == 2:
        print("Adding beef to the topping") 
        toppings.append("beef")
    elif user_choice == 3:
        print("Adding fruit to the topping") 
        toppings.append("fruit")
    elif user_choice == 4:
        print("Adding mashroom to the topping") 
        toppings.append("mashroom")
    elif user_choice == 5:
        print("Adding pork to the topping") 
        toppings.append("pork")
    elif user_choice == 6:
        print("Adding yam to the topping") 
        toppings.append("chicken")
    elif user_choice == 7:
        print("Thanks for visiting our page ...............Exiting") 
        break
    else:
        print("invalid choice!!!!!!!!!! please choose from above list")


    max_of_toppings =max_of_toppings + 1



if max_of_toppings == 0:
    print("Your pizza  is empty ")
else:
    print("Your toppings are" + str(toppings))