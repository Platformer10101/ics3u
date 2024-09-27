import random
ace = random.randrange(1,4)

print("You slide up to Fast Eddie's card table and plop down your cash.")
print()
print("He glances at you out of the corner of his eye and starts shuffling.")
print()
print("He lays down three cards.")
print()
print("WHch one is the ace?")
print()
print("	##  ##  ##")
print("	##  ##  ##")
print("	1   2   3")
print()

answer = int(input("> "))

if answer != ace:
    print(f"Ha! Fast Eddie wins again! The ace was card number {ace}.")
    print()
    if ace == 1:
        print("AA  ##  ##")
        print("AA  ##  ##")
        print("1   2   3")
    if ace == 2:
        print("##  AA  ##")
        print("##  AA  ##")
        print("1   2   3")
    if ace == 3:
        print("##  ##  AA")
        print("#  ##  AA")
        print("1   2   3")
elif answer == ace:
    print("You nailed it! Fast Eddie reluctantly hands over your winnings, scowling.")
    print()
    if ace == 1:
        print("AA  ##  ##")
        print("AA  ##  ##")
        print("1   2   3")
    if ace == 2:
        print("##  AA  ##")
        print("##  AA  ##")
        print("1   2   3")
    if ace == 3:
        print("##  ##  AA")
        print("##  ##  AA")
        print("1   2   3")
    


