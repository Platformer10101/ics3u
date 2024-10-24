print("Type in a message, and I'll display it ten times.")

message = input("Message: ")

for n in range(2,21,2):
    print(f"{n}. {message}")
    
#1 if the name of the variable is changed nothing will happen. n represents the number of times the message is printed. n is just short for number. 
#2 the 0 in teh range fuction represents the start of the range. The 5 is the number after the end of the range.
#3 the last nubmer represents the distance skipped by the range. When changed to two the message is printed on every multiple of 2 within the range
#4 if there is only one number in the range function the code repeats that many times starting from 0
#5 starts at teh first number ends before the last number
#6 Look at the code
#7 ^^^