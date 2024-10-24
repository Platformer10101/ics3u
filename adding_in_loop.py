print('I will add up the numbers you give me')

sum = 0
number = ''

while number != 0:
    number = int(input('Number: '))
    sum += number
    if number != 0:
        print(f'The total so far is {sum}')
    elif number == 0:
        print(f'The total is {sum}')
        break