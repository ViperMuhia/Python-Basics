f = 'cow.txt'
with open(f) as t:
    
    lines = t.readlines()

pi = ''
for line in lines:
    pi+=line.rstrip()


inpo=input("Enter your birth date in the format mmddyy")
if inpo in pi:
    print ("Got")
else:
    print ("Invalid")



#print(pi)
#print(len(pi))
    
    
    
    
    
    
    
    
    
    
    
    #lines = t.readlines()
    #print(lines)

#for line in lines:
 #   print(line.strip())
    
    
    
    
    
    
    
    
'''con = t.read()
    print(con.strip())'''