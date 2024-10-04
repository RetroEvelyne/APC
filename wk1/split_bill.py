import math as maths
# total / 3
# round up then take away the original to find the tip for each
# times this by 3 to find the total tip

def main(bill_total: float, num_of_friends: int):
    bill_for_each = round(bill_total / num_of_friends, 2)

    each_friend_pay = maths.ceil(bill_for_each)

    tip_for_each = round(each_friend_pay - bill_for_each, 2)

    total_payed = each_friend_pay * num_of_friends

    total_tip = tip_for_each * num_of_friends


    print(f"Each friend owes: £{bill_for_each}")
    print(f"Each friend needs to tip £{tip_for_each} to bring it to a round number")
    print(f"Which means each friend needs to pay: £{each_friend_pay}")
    print(f"The total payed is: £{total_payed}")
    print(f"Which includes the tip of: £{total_tip}")


if __name__ == "__main__":
    bill_total = 84.87
    num_of_friends = 3
    main(bill_total, num_of_friends)