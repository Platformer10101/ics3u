word1 = str.lower(input('Enter the first word: '))
word2 = str.lower(input('Enter the second word: '))
lastpos = len(word1) - len(word2)
inside = None

for i in range(lastpos, len(word1)):
    print(f"{word1[i]}", end = '')
    x = (word1[lastpos: len(word1)])
    
if x == word2:
    inside = True
elif x != word2:
    inside = False
while True:
    if inside == True:
        print('\nTrue')
        break
    if inside == False:
        print('\nFalse')
        break
    
#make it ignore numbers ig