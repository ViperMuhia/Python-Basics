unconfirmed_user = ["Brian","Suzzy","David","Trisha","Suzzy","Alex","Antony","Suzzy" ]
'''confirmed_user =[]

while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    print("Verifying user: " + current_user)

    confirmed_user.append(current_user)

print("The following users are confirmed")
for user in confirmed_user:
    print(user)'''

while "Suzzy" in unconfirmed_user:
    unconfirmed_user.remove("Suzzy")

print(unconfirmed_user)