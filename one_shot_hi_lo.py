import random 
number = random.randrange(1,101)

print("I'm thinking of a integer from 1 to 100. Try to guess it.")
guess = int(input("> "))
print()

if 1 <= guess < number:
    print(f"Too low, my number was {number}.")
elif 100 >= guess > number:
    print(f"Too high, my number was {number}.")
elif guess == number:
    print("Congrats, you guessed my number!")
else:
    print("Invalid Answer")