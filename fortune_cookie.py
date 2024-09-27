import random

message = random.randrange(7)

print("Fortune cookie says:")
if message == 0:
    print("The most important thing in communication is to hear what isn’t being said.")
elif message == 1:
    print("You will overcome difficult times.")
elif message == 2:
    print("You will find happiness with a new love.")
elif message == 3:
    print("Adjust finances, make budgets, to improve your standing.")
elif message == 4:
    print("Don't take yourself so seriously, no one else does.")
elif message == 5:
    print("Sometimes the object of the journey is not the end, but the journey itself.")
else:
    print("Happiness isn't something you remember, it's something you experience.")
print()

num1 = random.randrange(55)
num2 = random.randrange(55)
num3 = random.randrange(55)
num4 = random.randrange(55)
num5 = random.randrange(55)
num6 = random.randrange(55)

print(f"{num1} - {num2} - {num3} - {num4} - {num5} - {num6}")