#Fix error
drink = input("Do you prefer coffee or tea? ")
if drink == "coffee":
  print("Tea is better.")
else:
  print("Excellent choice.")

#Challenge
gender = input("Your gender (male/ female): ")
if gender == "male":
  print("Have a nice travel, sir")
else:
  print("Ladies is beautiful flowers that the world ")
  
nameCharacter = input("Your DC world name: ")
if nameCharacter == "Clark Ken":
  print("Welcome Superman, go to hell to save the world!")
elif nameCharacter == "Bruce Wayne":
  print("Welcome Batman, do you have any plan for travelling with your parents this weeken?")
elif nameCharacter == "Diana":
  print("Welcome Wonder Woman")
elif nameCharacter == "Barry Allen":
  print("Welcome Flash Boy")
else:
  print("Do you have power?")

power = input("Your ablitity (1 word):")
if power == "fly":
  print("You can fly like a bird, awesome!")
elif power == "fast" or power == "Fast":
  print("Are you the Flash? - The fastest man alive!")
elif power == "swim" or power == "water":
  print("Are you Aquaman?")
elif power == "power":
  print("Wonder Woman, right?")
elif power == "none" or power == "nothing":
  print("Live like a human, please!")
elif power == "magic":
  print("Shazam? Or Black Adam?")
else: 
  print("Welcome, new hero, I got your data!")