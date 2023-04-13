import os
import random
import time


def creatingCharacter():
  characterName = input("Name of Adventor: ")
  print("Character Type: Wizard, Hero, Teddy, Elf or Knight")

  while True:
    characterType = input("Type of Character: ")
    if characterType == "Wizard" or characterType == "Knight" or characterType == "Teddy" or characterType == "Hero" or characterType == "Elf":
      print("----------")
      print("Welcome", characterName, "to the Fanstatic World")
      print("Now you are the", characterType,
            "on the way to save this World from Saitama")
      break
    else:
      print("Not in list!")
      continue
  print("Creating Your Properties, please wait ......")
  time.sleep(4)
  print("----------")
  print("Your Name: ", characterName)
  time.sleep(1)
  print("Your Type: ", characterType)
  time.sleep(1)
  creatingHp()
  time.sleep(1)
  creatingStrengh()
  time.sleep(1)
  print("----------")
  time.sleep(3)
  print("Let's save this fucking world!")
  time.sleep(2)


def rollDice(sides):
  anySide = random.randint(1, sides)
  return anySide


def fomularForProperties(bonus):
  firstDice = rollDice(6)
  secondDice = rollDice(12)
  totalDice = firstDice + secondDice
  return totalDice / 2 + bonus


def creatingHp():
  # bonusHp = int(input("Type bonus for HP: "))
  bonusHp = 10
  hp = fomularForProperties(bonusHp)
  print("Your HP: ", hp)


def creatingStrengh():
  # bonusStrengh = int(input("Type bonus for Strengh: "))
  bonusStrengh = 12
  strengh = fomularForProperties(bonusStrengh)
  print("Your Power: ", strengh)


# Welcome
def welcome():
  print("     📷 Adventure Time 📷")
  print("------- Welcome Player --------")
  print("  --- Battles & Adventures ---")
  print()


play = True
while play:
  os.system("clear")
  welcome()
  print("Create Your Character? ")
  answer = input("Y/N: ")
  if answer == "Y":
    creatingCharacter()
  else:
    print("Have a nice day!")
    play = False
