start = int(input('Count from: '))
end = int(input('Count to: ')) + 1
difference = int(input('Count by: '))
print()

for n in range(start,end,difference):
    print(n ,end=' ')