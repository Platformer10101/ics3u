import math

print("SQUARE ROOT!")
number = int(input('Enter a number: '))
if number < 0:
    print("you can't root a negative!")
    while number < 0:
        number = int(input('Try Again: '))
root = math.sqrt(number) 
print(root)