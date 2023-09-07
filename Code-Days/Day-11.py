# Day 11 Challenge - How many minutes seconds in a year? I'll spin this to how many seconds until Suga is back from the military.

name = input("Hello! Who is heading to the military?: ")
year = int(input("What year are they heading in?: "))
leap_year = input("Is it a leap year?: ")

calc_seconds = 60
calc_minutes = 60
calc_hours = 24
calc_month = 12
calc_year = 365
calc_leap = 366
mil_year = calc_year * 2 
mil_leap = calc_leap * 2

if leap_year == "yes" or "Yes":
  total_leap = calc_minutes * calc_seconds * calc_hours * calc_month * mil_leap
  print("Don't feel too sad.", name," will be back in ",total_leap, "seconds.")
else:
  total_year = calc_minutes * calc_seconds * calc_hours * calc_month * mil_year
  print("Don't feel too sad.", name," will be back in ",total_year, "seconds.")

