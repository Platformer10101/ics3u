import random 

num = random.randrange(1,10)
guess = 0
tries = 0

print('I have chosen a number between 1 and 10.  Try to guess it.')
while num != guess:
    guess = int(input('Your guess: '))
    tries += 1
    if num != guess:
        print('That is incorret. Guess again.')
    elif num == guess:
        print(f"That's right You're a good guesser.\n It only took you {tries} tries.")
    else:
        print('INVALID ANSWER')