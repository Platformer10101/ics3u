print('Enetr three integers:')
side1 = input('Side 1: ')
side2 = input('Side 2: ')
while True:
    if side2 < side1:
        print("side 2 must be greater than side 1")
        while side2 < side1:
            side2 = input('Side 2: ')
    side3 = input('Side 3: ')        
    if side2 > side3:
        print("side 3 must be greater than side 2")
        while side3 > side2:
            side3 = input('Side 3: ')
    print(f'Your three sides are {side1}, {side2}, and {side3}')