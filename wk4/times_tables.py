chosen_num = int(input("Which times tables would you like? > "))

for multiplier in range(1, 13):
    print(f"{chosen_num} x {multiplier} = {chosen_num*multiplier}")
