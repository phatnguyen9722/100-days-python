exit = "no"
while exit == "no":
  animal_sound = input("What animal sound do you want to hear? ")
  
  if animal_sound == "cow" or animal_sound == "Cow":
    print("🐮 Mooooooo")
  elif animal_sound == "pig" or animal_sound == "Pig":
    print ("🐷 ọt ẹc ec ec ec ec")
  elif animal_sound == "sheep" or animal_sound == "Sheep":
    print ("🐑 Baaaaaaaa")
  elif animal_sound == "duck" or animal_sound == "Duck":
    print("🦆 Quack Quack")
  elif animal_sound == "dog" or animal_sound == "Dog":
    print("🐶 Gâu Gâu")
  elif animal_sound == "cat" or animal_sound == "Cat":
    print("🐱 Meo meo meo")
  else: 
    print("I don't know that animal sound. Try again.")
  exit = input("Do you want to exit?: ")