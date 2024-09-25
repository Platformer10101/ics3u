print("You're walking in a forest and you see two paths. Which one do you take? 'left' or 'right'")
choice1 = input("> ")
if choice1 == 'left':
    print("You see a cabin with smoke coming from it. Do you 'go' inside or 'keep walking'?")
    choice2 = input("> ")
    if choice2 == 'go':
        print("The door is locked. Do you 'pick the lock' or 'leave'?")
        choice3 = ("> ")
        if choice3 == 'pick the lock':
            print("Inside is nice warm meal and a bed. You stay here for the night ad return home the next day.")
        elif choice3 == 'leave':
            print("You get lost and die alone in the woods")
        else:
            print("Invalid Answer")
    elif choice2 =='keep walking':
        print("You eventually find the end of the path. Do you 'leave' or 'stay'")
        choice3 = input("> ")
        if choice3 == 'leave':
            print("You get in your car and go home.")
        elif choice3 == 'stay':
            print("Mr. Gallo appears and makes you write nested if statements until the end of time.")
        else:
            print("Invalid Answer")
    else:
        print("Invalid Answer")
elif choice1 == 'right':
    print("The trail eventually turns into a dirt path. Do you 'continue walking' or 'go back'?")
    choice2 = ("> ")
    if choice2 =='continue walking':
        print("A moonster apears in front of you. Do you 'run' or 'fight' it?")
        choice3 = input("> ")
        if choice3 == 'run':
            print("You try to run but the monster catches up and eats you.")
        elif choice3 == 'fight it':
            print("You try to fight it but you get eaten anyways.")
        else:
            print("Invalid Answer")
    elif choice2 == 'go back':
        print("You find yourself back at the begining. Do you 'take the other path' or 'leave'?")
        choice3 = input("> ")
        if choice3 == 'take the other path':
            print("By now it's dark and you trip on a stick and ball on a rock, breaking your neck causng you to die.")
        elif choice3 == 'leave':
            print("You realise you can't leave and you walk around endlessly until you die of dehydration.")
        else:
            print("Invalid Answer")
    else:
        print("Invalid Answer")
else:
    print("Invalid Answer")