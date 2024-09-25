print("Here are the available planets")
print(" 1. Venus   2. Mars    3. Jupiter 4. Saturn  5. Uranus  6. Neptune")

planet = input("Please choose a planet: ")
eweight = int(input("what is your weight (to the nearest pound)"))
vweight = eweight * 0.78
mweight = eweight * 0.39
jweight = eweight * 2.65
sweight = eweight * 1.17
uweight = eweight * 1.05
nweight = eweight * 1.23

if planet == 'Venus':
     print(f"Your weight on Venus is {vweight} lbs)")
elif planet == 'Mars':
    print(f"Your weight on Mars is {mweight} lbs")
elif planet == 'Jupiter':
    print(f"Your weight on Jupiter is {jweight} lbs")
elif planet == 'Saturn':
    print(f"Your weight on Saturn is {sweight} lbs")
elif planet == 'Uranus':
    print(f"Your weight on Uranus is {uweight} lbs")
else:
    print(f"Your weight on Uranus is {uweight} lbs")