def greetings(firstname, lastname,age):
    person = {'firstname':firstname, 'lastname':lastname,  'age':age}
    return person

musician = greetings("Alex","Muhia",21)
print(musician)

for firstname,lastname,age in musician.items():
    print ("f{firstname} {lastname} who is {age}is a great artist")