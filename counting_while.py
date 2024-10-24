print("Type in a message, and I'll display it thowever many times you want.")

message = input("Message: ")
print()

repetitions = int(input('How many times do you want it to repeat\n'))
print()

n = 0
while n < repetitions:
    print(f"{n * 10 + 10}. {message}")
    n += 1
    
#1 n += 1 adds 1 to the variable n each time the code is executed so that the loop will eventualy stop
#2  see line 7
#3 seel ine 8
