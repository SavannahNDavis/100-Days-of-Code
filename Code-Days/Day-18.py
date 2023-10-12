print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")
print()

correct_number = 10
attempt = 1

while True:
  user_guess = int(input("Pick a number between 1 and 100: "))
  if user_guess < 0:
    print("Wah wah wah..")
    exit()
  if user_guess < correct_number:
    print("A little too low. Try again: ")
    attempt +=1
  elif user_guess > correct_number:
    print("A bit too high there. Try again: ")
    attempt +=1
    continue
  elif user_guess == correct_number:
    print("You got it!")
else:
  print("Don't recognize that number, darling. Sorry.")

print()

print("It took you", attempt, "attempt(s) to get the correct answer.")
