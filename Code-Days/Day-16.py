# Day 16 - While True

print("Let's play Shooter, Roller, Brush. Please read the rules below:")
print()
print("Rules: Sellect S for Shooter, R for Roller, or B for Brush. One person at a time. Then it will be decided who wins!")


while True:
  print()
  player1 = input("Player 1: Your move. S,R, or B?: ")
  player2 = input("Player2: Let's go! Pick S,R, or B?: ")
  print()
  if player1 == "r" or player1 == "R":
    if player2 == "b" or player2 == "B":
      print("Player 2's Brush covers the roller with a load of ink!")
    elif player2 == "S" or player2 == "s":
      print("Player 2's shooter is crushed by the roller!")
    elif player2 == "r" or player2 == "R":
      print("You're both rollers. Duke it out!")
    else:
      print("Invalid move, Player 2!!")
  if player1 == "b" or player1 == "B":
    if player2 == "r" or player2 == "R":
      print("Player 1's brush covers the roller!")
    elif player2 == "S" or player2 == "s":
      print("Player 1's brush takes out the shooter!")
    elif player2 == "b" or player2 == "B":
      print("Both brushes huh? Duke it out! Who is a better brush?")
    else:
      print("Invalid move, Player 2!!")
  if player1 == "s" or player1 == "s":
    if player2 == "b" or player2 == "B":
      print("Player 2's brush covers the shooter!")
    elif player2 == "R" or player2 == "r":
      print("Player 2's roller crushses the shooter!")
    elif player2 == "s" or player2 == "S":
      print("Two shooters.. Rather boring I think.")
    else:
      print("Hmm.. try to select one of the three weapon categories listed. ")
  
  exit = input("Exit?: ")
  if exit == "yes" or exit == "Yes":
    break
print("Thanks for playing!")
