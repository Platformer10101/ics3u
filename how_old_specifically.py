name = input("What is you name?: ")
age = int(input(f"How old are you, {name}: "))

if age < 16:
    print(f"You can't drive, vote, or rent a car, {name}.")    
elif age < 18:
    print(f"You can drive but you can't vote or rent a car, {name}.")   
elif age < 21:
    print(f"You can drive and vote but you can't rent a car, {name}.")    
else: 
    print(f"You can do anything that's legal, {name}.")
    