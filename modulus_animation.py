print("1. Worm 2. Symbols")
animation = input("Pick one of the above animations: ")

if animation == 'Worm':
    import time
    import os
    for i in range(80):
    
        if i % 16 == 0:
            print(" ********                 ")
        elif i % 16 == 1:
            print("   ********               ")
        elif i % 16 == 2:
            print("     ********             ")
        elif i % 16 == 3:
            print("       ********           ")
        elif i % 16 == 4:
            print("         ********         ")
        elif i % 16 == 5:
            print("           ********       ")
        elif i % 16 == 6:
            print("             ********     ")
        elif i % 16 == 7:
            print("               ********   ")
        elif i % 16 == 8:
            print("                 ******** ")
        elif i % 16 == 9:
            print("               ********   ")
        elif i % 16 == 10:
            print("             ********     ")
        elif i % 16 == 11:
            print("           ********       ")
        elif i % 16 == 12:
            print("         ********         ")
        elif i % 16 == 13:
            print("       ********           ")
        elif i % 16 == 14:
            print("     ********             ")
        elif i % 16 == 15:
            print("   ********               ")
        time.sleep(0.1)

elif animation == 'Symbols':
    import time
    import os
    repeats = 5
    steps_per_second = 10
    
    for i in range(11 * repeats):
        
        if i % 11 == 0:
            print(" .oOo....... ")
        elif i % 11 == 1:
            print(" ..oOo...... ")
        elif i % 11 == 2:
            print(" ...oOo..... ")
        elif i % 11 == 3:
            print(" ....oOo.... ")
        elif i % 11 == 4:
            print(" .....oOo... ")
        elif i % 11 == 5:
            print(" ......oOo.. ")
        elif i % 11 == 6:
            print(" .......oOo. ")
        elif i % 11 == 7:
            print(" ........oOo ")
        elif i % 11 == 8:
            print(" o........oO ")
        elif i % 11 == 9:
            print(" Oo........o ")
        elif i % 11 == 10:
            print(" oOo........ ")
        time.sleep(1/steps_per_second)
else:
    print("Invalid Choice")

