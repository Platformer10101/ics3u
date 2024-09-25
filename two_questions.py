print("TWO QUESTIONS!")
print("Think of an object and I'll try to guess it.")
print(" ")
print("Question 1) Is it animal, vegetable of mineral?")
clue1 = input("> ")
print("Question 2) Is it bigger than a breadbox?")
clue2 = input("> ")
if clue1 == 'animal':
    if clue2 == 'yes':
        print("My guess is that you are thinking of a moose.")
    elif clue2 =='no':
        print("My guess is that you are thinking of a squirrel")
    else:
        print("invalid answer")
elif clue1 == 'vegetable':
    if clue2 == 'yes':
         print("My guess is that you are thinking of a watermelon.")
    elif clue2 =='no':
        print("My guess is that you are thinking of a carrot")
    else:
        print("invalid answer")
elif clue1 == 'mineral':
    if clue2 == 'yes':
         print("My guess is that you are thinking of a car.")
    elif clue2 =='no':
        print("My guess is that you are thinking of a paperclip")
    else:
        print("invalid answer")
else:
    print("Invalid answer")