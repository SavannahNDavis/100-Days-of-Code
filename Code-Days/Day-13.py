# Day 13 - Grade Calculator/Output Challenge. (First BIG project!)

print("~ Exam Grade Calculator ~")
print()
name = input("What's your name?: ")
print("Hello! Let's calculate your grade,", name,"!")
print()
exam_high_score = int(input("What's the highest you could have scored?: " ))
exam_score = float(input("What did you end up scoring?: "))
answer_total = exam_score/exam_high_score *100
answer = round (float(answer_total),2)
print("Your final grade was ", answer)

if answer <=40:
  print("Wow.. you failed. Your score is", answer, "and you have a U in the class.")
elif answer >=50 and answer <= 59:
  print("Okay.. So you made a", answer,". Not much to say honestly.")
elif answer >= 60 and answer <= 69:
  print("You have a D. The 60's look great on anyone, really.")
elif answer >=70 and answer <=79:
  print("Let me just say this.. C's DO get degrees. I'm sure it's no surpirse you have a C.")
elif answer >=80 and answer <=89:
  print("Great job! You worked hard for that B! 🌟 ")
elif answer >=90:
  print("No one likes overachivers. Please take your A and exit left.")
else:
  print("I don't want to hurt your feelings.. Bye..")

