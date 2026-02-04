#variables and different variable types
age = 25 #int
height = 10.1 #float
boolean = True # binary; true/false value
name = "Sam" #string

arr = [1,2,3] # arrays

#python DOES NOT explicit variable types so you need to be careful when doing operations
print(type(age))
print(type(height))
print(type(boolean))

#variable operations -> addition/subtraction/division/multiplication
a = 3
b = 10
c = 0
print(f"{c} original value")
c = a + b
print(f"{c} value after addition")
c = b/a
print(f"{c} value after division")
c = a * b
print(f"{c} value after multiplication")

#data type conversions
ageStr = str(age) # now age is a string
print(ageStr)
ageFloat = float(age) # now age is a float
print(ageFloat)
heightStr = int(height) # now height is an int
print(heightStr)

