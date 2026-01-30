'''trying lists
bed = 12
bath = 23
liv = 56
rooms_list = [bed, bath, liv]
print(rooms_list)
'''

#try if condition inside for loop

duration = 40
countdown = 30

for second in range (duration):
    if countdown>0:
        Status= "active"
        
        countdown -=1
        print (Status,'downcounting',countdown)
    else:
        Status = "expired"
        break
print (Status, "stop")


'''I am confused how to start from 30 ,
 as I was thinking about adding one the start counting but then it will end at 1 '''


# I will try to have many if condition
'''
Duration = 40
countdown = 30
countdown_1 = countdown +1
for second in range (Duration):
    if countdown_1>0:
        Status="active"
    else:Status = "expired"
    if countdown_1>0:
        countdown_1 -=1
        print (Status,'downcounting',countdown_1)
    else:
        print(Status)
        break
'''
''' 1. you should put break at the end of the condition not before
 2. I tried to make if condition for status , and one for the counting , , it worked , 
  3. I was confused about why it didn't continue counting  the whole duration , then i removed the break , it worked '''


#The len function gives the number of elements in the list. Tell the user how many times they've logged in, and when they last logged in.
'''
user= "bodi"
times= [12,13,14,15,16]
print ("you logged ", len(times))


#Logins between 2am and 4am are unusual. Notify the user of any unusual logins.
unser = "bodi"
times = [12,13,14,15,16]
for time in times :
    print (len(times))
    if time >12 and time <14:
        print ("it's weird")
        
I have no idea why it does't execute , is there anything wrong I have done ?
        

#There's a login from a new MacBook. Append it to the list of past devices, and notify the user.
users= "bodi"
old_devices = ["iphpne", "samsung"]
device = "mac"
old_devices.append(device)
print ("there is a new device tying to log in", device , "is it yours?")
print ("devices logged in", len(old_devices))
print (old_devices)
'''
#Run through the list of login devices, printing a message for each.
'''I am confused about print the list sometimes you call the values , some times you call the variable itself 




'''