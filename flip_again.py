import random

again = 'y'

while True:
    if again == "y":
        flip = random.randrange(2)  # 0-1

        if flip == 1:
            coin = "HEADS"
        else:
            coin = "TAILS"

        print("You flip a coin and it is... " + coin)

        again = input("Would you like to flip again (y/n)? ")
    else:
        break

#3 When removing the again = 'y' the code breaks becasue the variable "again" isn't defined