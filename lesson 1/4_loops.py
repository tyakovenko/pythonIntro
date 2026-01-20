#different loops are used to run the same action over and over again
for i in range(1, 6): #range means the numbers that we are iterating over; note that 6 is NOT included in the iteration
    print(f"The values of i from the first for loop {i}")

#for loops for arrays
'''
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(0, len(fruits)):
    print(fruits[i])

'''

#while loop
count = 1 # counter variable
while count <= 5:
    if count == 2:
        print("I got to 2!")
    print(f"count prints from while loop {count}")
    count = count + 1

#break is to stop a loop after a particular condition
for number in range(1, 10):
    if number == 5:
        break
    print(number)

#continue is to skip a certain part of the loop with a new condition
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

#nested for loops; the easiest application is matrix operations
for row in range(1,3):
    for col in range(1, 3):
        print(row, col)

#TODO: homework
'''
Homework: use a nested for loop to create a matrix multiplication calculator
Print out the two matrices added and the result onto the screen
'''










