# Day 7!! Learned about nesting an if within an if!

# Practice Exercise (My own ideas!)

tvshow = input("What's your favorite tv show right now? ")
if tvshow == "Netflix Docs":
  print("Cool! I also love Netflix Documentaries!")
  ndoc = input("Which one are you watching? ")
  if ndoc == "Bikram Yogi":
    print("White people are always in a cult, right?")
  elif ndoc == "Shiny Happy People":
    print("Isn't that on Prime?")
  else:
    print("Ooh haven't seen that one yet. Tell me about it.")
elif tvshow == "K-dramas":
  print("I lOVE K-dramas!")
  kcurrent = input("What are you watching right now? ")
  if kcurrent == "100 Days My Prince":
    print("Love that one!")
  else:
    print("Ooh, tell me about it!")
else:
  print("Oh yeah! That's cool. Haven't heard of it though.")


# Broken Code
order = input(What would you like to order: pizza or hamburger? ")
if order = "hamburger":
print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
  print("You got it.")
else: 
    print("No cheese it is.")
elif order == pizza:
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings = "yes"
    print("We will add pepperoni.")
else:
  print"Your pizza will not have pepperoni.")


# Fixed Code
order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")
  else: 
    print("No cheese it is.")
elif order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")
  else:
    print("Your pizza will not have pepperoni.")

# Day 7 Challenge - Fake Fan Challenge BTS Edition

print("BTS FAN QUIZ")
print()
bts_know = input("✨ Hello! Do you know BTS? ")
if bts_know == "yes":
  print("Oh! Cool! Nice to meet you.")
  bts_fan = input("What is the fanbase name? ")
  if bts_fan == "ARMY":
    print("Wow, you might be a real fan!")
    bts_member = input("Who are the members? ")
    if bts_member == "RM, Jin, Suga, J-Hope, Jimin, V, JK":
      print("Well done!")
      bts_fav = input("Who is your favorite member? ")
      if bts_fav == "Suga":
        print("You're on the right track there.")
        suga_song = input("What's your favorite song of his? ")
        if suga_song == "So Far Away":
          print("We are a match made in heaven. Welcome in.")
      else:
        print("The're all pretty great honestly.")
  elif bts_fan == "AHMI":
    print("Ahh a true fan.")
  else:
    print("Yikes.. you call yourself a fan?")
else:
  print("Oh.. awkward.. Well it was nice chatting with you.")
