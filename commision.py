print("\t************ELECTION DAY ****************\t\t")
print("***Welcome to the Soko mjinga electrol commission Please ensure you choose your department correctly. ***")
voting_times = 0
choice1=0
choice2 =0
choice3 =0
while voting_times<2:
    user_choice=int(input("\t1:Education\n\t2:Business\n\t3:Technology\n\t4:quit \n choice : "))
    if user_choice == 1:
        print("**********Welcome to the education department********"  )
        while choice1 < 1:
            contestants1 =int(input("\tThe following are applying for the position :\n\t 1:Sam korir\n\t2:Sandra Mohotia\n\t3:Eugene Were\n choice: "))
            if contestants1 == 1:
                print("You have successfully chosen Sam korir")
                break
            elif contestants1 == 2:
                print("You have successfully chosen Sandra Mohotia")
                break
            elif contestants1 == 3:
                print("You have successfully chosen Eugene Were")
                break
            else:
                print("Wrong choice please select again")
            choice1 = choice1 +1
    
        break       
            
    elif user_choice == 2:
        print("**********Welcome to the Business department********"  )
        while choice2 < 1:
            contestants2 =int(input("\tThe following are applying for the position :\n\t 1:Meshack Kiki\n\t2:Joy Nabiki\n\t3:Beatrice Mutindi\n choice: "))
            if contestants2 == 1:
                print("You have successfully chosen Meshack Kiki")
                break
            elif contestants2 == 2:
                print("You have successfully chosen Joy Nabiki")
                break
            elif contestants2 == 3:
                print("You have successfully chosen Beatrice Mutindi")
                break
            else:
                print("Wrong choice please select again")
            choice2 = choice2 +1
        
    elif user_choice == 3:
        print("**********Welcome to the Technology department********"  )
        while choice3 < 1:
            contestants3 =int(input("\tThe following are applying for the position : \n\t 1:Alex Ntutu\n\t2:Isiah Keki\n\t3:Eshter Nzuki\n choice: "))
            if contestants3 == 1:
                print("You have successfully chosen Alex Ntutu")
                break
            elif contestants3 == 2:
                print("You have successfully chosen Isiah Keki")
                break
            elif contestants3 == 3:
                print("You have successfully chosen Eshter Nzuki")
                break
            else:
                print("Wrong choice please select again")
            choice3 = choice3 +1
    elif user_choice==4:
        print("You have successfully Quit") 
        break  
    else:
        print("invalid choice!!!!!!!!!! please choose from above list")
    voting_times = voting_times + 1