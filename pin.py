number_of__entries=0
pin = 1234
trial = 3

while number_of__entries > trial:
    user_input=int(input("Please enter your pin \n"))
    if user_input == pin:
        print("Correct pin number")
        break
    else:
        print("Invalid pin number please try again")
    number_of__entries=+1