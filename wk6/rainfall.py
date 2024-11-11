def display_histogram(rainfall_data):
    print(" "*21 + "------------------")
    print(" "*21 + "Rainfall Histogram")
    print(" "*21 + "------------------")

    max_rainfall = max(rainfall_data.values())

    # print out the bars
    # max_rainfall//10 is used to scale the histogram down by 10 
    # level is representing each line of the histogram starting from the top
    for level in reversed(range(1, max_rainfall//10)):
        # this goes through each month sequentially and decides whether the months 
        # amount of rain meets the threshhold value set by level
        for months_rain in rainfall_data.values():
            if months_rain // 10 >= level:
                print(f"  *  ", end="")
            else:
                print(f"     ", end="")
        print()

    # print the months in order on the bottom
    for month in rainfall_data.keys():
        print(f" {month} ", end="")
    print()

def main():
    rainfall_data = { 'Jan': 23, 'Feb': 45, 'Mar': 12, 'Apr': 10, 'May': 33,
                      'Jun': 90, 'Jul': 94, 'Aug': 76, 'Sep': 10, 'Oct': 15,
                      'Nov': 120, 'Dec': 22 }

    display_histogram(rainfall_data)

main()
