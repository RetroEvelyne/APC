print(f"\nThe total including tax is: £{'{:.2f}'.format(round(sum([float(input('Whats the price? £')) for _ in range(int(input('How many pizzas? > ')))])*1.2, 2))}")
