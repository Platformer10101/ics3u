#Create a while loop that will:

#calculate the sum of the numbers from 1 to 10.
#calculate the sum of the numbers from 100 to 200.
#calculate the difference between the sum of the numbers from 100 to 200 and the sum of the numbers from 200 to 300.
#calculate the sum of the multiples of 5 between the numbers 1000 and 10000.
#calculate the sum of the multiples of 5 between 1 and 100, but do not include numbers that are multiples of 3. Modulus (%) will come in handy here.

#1.
number = 0
sum = 0
while number < 10:  
    addition = number + 1
    sum += addition
    number += 1
    print(sum)
print()
    
#2. 
number2 = 99
sum2 = 0
while number2 < 200: 
    number2 += 1 
    addition2 = number2
    sum2 += addition2
    print(sum2)
print()

#3. 
number3 = 99
sum3 = 0
while number3 < 200: 
    number3 += 1 
    addition3 = number3
    sum3 += addition3
number32 = 199
sum32 = 0
while number32 < 300: 
    number32 += 1 
    addition32 = number32
    sum32 += addition32  
print(sum32 - sum3)
print()

#4.
number4 = 995
sum4 = 0
while sum4 < 10000:  
    number4 += 5
    sum4 += number4
    print(sum4)
print('Q4')

#5
number5 = 0
sum5 = 0
while sum5 < 100:  
    sum5 += 5
    remainder = sum5 % 3
    if remainder != 0:
        print(sum5)
    else:
        print()
print('Q5')
