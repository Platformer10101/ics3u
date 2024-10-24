num = int(input('Input a number: ')) + 1
sum = 0
for n in range(1,num):
    print(n, end=' ')
    sum = sum + n
    
print(f"\nthe sum is {sum}.")