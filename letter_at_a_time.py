message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")

a_count = 0
for i in range(len(message)):
    letter = message[i].lower()
    if letter == 'a':
        a_count += 1
    if letter == 'e':
        a_count += 1
    if letter == 'i':
        a_count += 1
    if letter == 'o':
        a_count += 1
    if letter == 'u':
        a_count += 1
        
print(f"\nYour message contains the letter 'a' {a_count} times.")

#1 the code only prints out 7 characters of the message. puting it in a list made everything for spaces ahead
#2 if te message was hello the numbers sent would be 4,3,2,1 and 0
#3 2
#4 See code