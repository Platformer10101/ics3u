Score = 0

print("Are you ready for a quiz?")
print("Ok, here is comes!")
print(" ")

print("Q1) What is the capital of Alaska?")
print(" 1) Melbourne")
print(" 2) Anchorage")
print(" 3) Juneau")
print(" ")
q1 = int(input("> "))
if q1 == 2:
    Score += 1
    print("That's correct!")
else:
    print("Sorry, the capital of Alaska is Anchorage.")
print(" ")

print("Q2) In Python, the way you get keyboard input is the keyobard_input function.")
print(" True")
print(" False")
print(" ")
q2 = int(input("> "))
if q2 == 2:
    Score += 1
    print("That's correct!")
else:
    print("Sorry, in Python, you would use the 'input' function to get keyboard input.")
print(" ")

print("Q3) What is the result of 9 + 6 / 3?")
print(" 1) 5")
print(" 2) 11")
print(" 3) 15/3")
print(" ")
q3 = int(input("> "))
if q3 == 2:
    Score += 1
    print("That's correct!")
else:
    print("Sorry, the result is 11")
print(" ")
print(f"You got a score of {Score}/3!")
print("Thanks for playing!")