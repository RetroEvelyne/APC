CYCLE_CALS_PER_HOUR = 200
RUNNING_CALS_PER_HOUR = 475
SWIMMING_CALS_PER_HOUR = 275

cycle_hours = float(input("Please enter hours spend cycling: "))
running_hours = float(input("Please enter hours spend running: "))
swimming_hours = float(input("Please enter hours spend swimming: "))

total_cycle_cals = cycle_hours * CYCLE_CALS_PER_HOUR
total_running_cals = running_hours * RUNNING_CALS_PER_HOUR
total_swimming_cals = swimming_hours * SWIMMING_CALS_PER_HOUR

total_cals_burnt = total_cycle_cals + total_running_cals + total_swimming_cals

total_pounds_lost = total_cals_burnt / 3500

print("You have burnt {:.2f} calories and lost {:.2f} pounds"
      .format(total_cals_burnt, total_pounds_lost))
