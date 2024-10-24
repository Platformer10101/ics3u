import random

number = random.randrange(1,100)
guess = 0
tries = 10
guessnum = 0

print("I'm thinking of a number between 1-100.  You have 7 guesses.")

while guess != number:
    tries -= 1
    guessnum += 1    
    guess = int(input(f'Guess #{guessnum} '))
    if guess == number:
        print("You guessed it!  What are the odds?!?")
        break
    elif guess != number and guess > number:
        print("Sorry, that guess is too high.")
    elif guess != number and guess < number:
        print("Sorry, that guess is too low.")
    else:
        print("Invalid")