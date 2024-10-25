# ask how many pizzas
# use this number in a for loop to ask the cost of each pizza 
# sum the total
# round(total * 0.2, 2) to find the sales tax
# add the sales tax to the total
# show the final amount

total = 0 
pizza_amount = int(input("how many pizzas? > "))
print()

for pizza in range(pizza_amount):
    total += float(input("Whats the price? £"))

total += round(total*0.2, 2)
total = "{:.2f}".format(total)

print(f"\nThe total including tax is: £{total}")

