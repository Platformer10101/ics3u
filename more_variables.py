store = "No Frills"
item = "Apples"
price = 0.5
quantity = 7
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal

#fstring
print(f"At {store} I bought some {item}.")
#concatenation
print("They sold for $" + str(price) + " each.")
#dot format
print("I wanted to purchase {} of them.".format(quantity))
# f is missing before the quotation
#fstring
print(f"The total price, with tax included, was ${total}.")
print(f"The subtotal is %{tax}.")
print(f"The tax is ${subtotal}.")