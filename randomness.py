import random
random.seed(4000)
#2 caused all the numbers to be the same
#3 new set of numbers but they stay the same

x = random.randrange(10)  # 0-9
print(f"My random number is {x}.")

print()
print("Here are some random numbers from 1 to 5...")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5))
#1 range changes from 1 to 5 to 1 to 4

print()
print("Here are some random numbers from 1 to 100...")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101))

print()
print("Will these next two random number be the same?")
a = random.randrange(10)  # 0-9
b = random.randrange(10)

if a == b:
    print(f"Wow! Both numbers were {a}!")
else:
    print("The two random numbers were different. Not too surprising.")
    
#4 Some popular game that use seeds are Minecraft and Muck. The seed is often used for world generation in open world sandbox games where procedural generation is used to create worlds. It is useful for creating new and original worlds compared to the same world each time.