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
