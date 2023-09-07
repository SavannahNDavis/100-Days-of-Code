# Day 10 Challenge! 

total_bill = float(input("Whats the bill total?: "))
tip = int(input("What would you like to tip?: "))
total_people = int(input("How many people are there?: "))
tip_calc = tip /100
bill_tip = total_bill * tip_calc
total = bill_tip + total_bill
answer = total/total_people
answer = round(answer,2)
print("You all owe,",answer)
