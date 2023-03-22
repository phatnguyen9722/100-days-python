# Fix code 
# tvShow = input("What is your favourite tv show? ")
# if tvShow == "peppa pig":
#   print("Ugh, why?")
#   faveCharacter = input("Who is your favourite character? ")
#   if faveCharacter == "daddy pig":
#     print("Right answer")
#   else:
#     print("Nah, Daddy Pig's the greatest")
# elif tvShow == "paw patrol":
#   print("Aww, sad times")
# else:
#   print("Yeah, that's cool and all…")

# Fix code 2
# order = input("What would you like to order: pizza or hamburger? ")
# if order == "hamburger":
#   print("Thank you.")
#   cheese = input("Do you want cheese?")
#   if cheese == "yes":
#     print("You got it.")
#   else: 
#     print("No cheese it is.")
# elif order == "pizza":
#   print("Pizza coming up.")
#   toppings = input("Do you want pepperoni on that?")
#   if toppings == "yes":
#     print("We will add pepperoni.")
#   else:
#     print("Your pizza will not have pepperoni.")
# else:
#   print("Go out")

film = input("What type of film do you like to watch? Horror or Romantic")
if film == "Romantic": 
  print("Wow, so sweat!")
  confirm = input("Have you ever watched Titanic?")
  if confirm == "yes":
    print("awesome, it's been greatest film ever but sad ending")
  else: 
    print("You should watch it! It's nice film")
elif film == "Horror":
  print("That is my type, too")
  askMore = input("Did you watch The Saw?")
  if askMore == "yes": 
    print("That's the scarest movie that I've watched :(")
  else:
    print("You should try it <3")
else: 
  print("Have a nice day ^^")