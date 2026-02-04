#booleans and boolean operations
print(bool("Hello"))
print(bool(15))

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#example of function definition with bools
def add(a,b):
    """
    add two numbers if a < b, subtract otherwise
    :param a: num 1
    :param b: num 2
    :return: sum or difference
    """
    if a < b:
        c = a + b
    else:
        c = a - b

    return c