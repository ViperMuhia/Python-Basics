responses={}

polling_active = True

while polling_active:
    name = input("What is your name: \n")
    response = input("Where do you want to visit this world? :\n")

    responses[name]= response
    reapeat = input("Would you like anyone else to continue? (y/n)\n" )

    if reapeat.lower() == "n":
        break
    elif reapeat.lower() == "y":
        continue
    else:
        print("Invalid entry")

#for name, response in responses.items():
 #   print(name + " Is having a dream to visit "+ response)

print(responses)