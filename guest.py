#user= input("Please enter your name\n")

user_data = 'User_data.txt'
'''with open(user_data,'a') as f:
    f.write(user + '\n')'''

with open(user_data) as y:
    lin=y.readlines()
po=""
for line in lin:
    po =po +str( line.rsplit())
name = "faith"
if name in po:
    print("Found")
else:
    print("No name")