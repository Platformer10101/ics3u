print("Enter the following information about an item you wish to purchase..")
print()

print("The name of the item:")
#3 havign the instructions after the input is an issue because the code will not continue until the user input is completed but the input cannot be completed if the user is not given instructions to give an input.
name = input()
#1 the variable name ask for just an input
price = float(input("The price: $"))
#4 int and float funcitons determine the numerical value of a variable. int makes thr variable an integer while float makes the variable a decimal 
#1 the variable price askes for a float input or a decimal since it's in regards to money
print("How many do you want?")
quantity = int(input())

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")