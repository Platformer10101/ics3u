print('#1')
sum = 0
while sum <= 10:
    sum += 1    
    if sum != 7 and sum <= 10:
        print(sum)
print()

print('#2')
sum2 = 0
num2 = 4
while num2 <= 19:
    num2 += 1
    sum2 += num2
    remainder = sum2 % 3
    if remainder != 0:
        print(sum2)
    else:
        print()
print()

print('#3')
startnum = int(input("First number: "))
endnum = int(input("Last number: "))
sum3 = 0
num3 = startnum - 1
while num3 != endnum:
    num3 += 1
    sum3 += num3
    print(sum3)
    if num3 ==  13 or num3 == 31:
        break
print()

print('#4')
while True:
    word = str(input("Enter a word: "))
    if word == 'stop':
        print('Goodbye!')
        break
    print(f"Your word: {word}")
print()