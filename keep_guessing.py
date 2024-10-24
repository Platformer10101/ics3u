
import random

number = random.randrange(1,10)
guess = 0

print('I have chosen a number between 1 and 10. Try to guess it.')
while guess != number:
    guess = int(input('Your guess: '))
    if guess != number:
        print('That is incorrect. Guess again.')
    if guess == number:
        print("That's right! You're a good guesser.")
        