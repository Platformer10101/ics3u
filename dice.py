import random 

print("HERE COMES THE DICE!")

roll1 = random.randrange(1,7)
roll2 = random.randrange(1,7)

print(f"Roll #1: {roll1}")
print(f"Roll #2: {roll2}")

sum = roll1 + roll2

print(f"The total is {sum}!")