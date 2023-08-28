# elif 

#practice
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password >")
if username == "mark" and password == "password":
  print("Welcome Mark!")
elif username == "sav" and password == "nope":
  print("Hello, Savannah")
elif username == "Bookie" and password == "irule":
  print("Hello, Bookie.")
else:
  print("Go away!")

#  Fix my code challenge:
#  season = input(what is your favorite season?)
# if season = "spring"
 #  print("Ah! The birds are chirping and flowers blooming.")
 # elif season == summer:
 # elif season == autumn
# print("The leaves are changing and the air is crisp. Enjoy!)
      # elif season = winter:
      # print("Stay warm by the fire and watch the snow fall.")
# else: 
  # print("I don't know that season. Please try again.")



#  Fixed the code!:
season = input("what is your favorite season?")
if season == "spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
  print("Stay warm by the fire and watch the snow fall.")
else: 
  print("I don't know that season. Please try again.")
