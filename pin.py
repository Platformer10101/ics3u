PIN = "12345"

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

#1. While loops are similar to if statements in the sense that the code is not satisfied unless certain things are met.
#2. While loops, unlike if statments, repeat their code until it it satisfied. IF statements only use the cocde once before ending the program or continuing to the next part.
#3. Every time the user was asked for a pin the input code would have to be int(input("ENTER YOUR PIN: "))
#4. code asks you to enter the defenition/ value of the variable "entry" as a string or number
