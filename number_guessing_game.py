import random
number = random.randrange(11)

print("I'm thinking of a number from 1 to 10.")
guess = int(input("Your guess: "))

if guess == number:
    print(f"Congrats. You guessed my number!")
elif guess != number:
    print(f"You did not guess my number. My number was {number}.")
else:
    print("Invalid Answer")