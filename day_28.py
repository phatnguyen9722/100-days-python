import os
import random
import time


def creatingCharacter(playerNum):
  characterName = input(f"Name of Player {playerNum}: ")
  print("Character Type: Wizard, Hero, Teddy, Elf or Knight")

  while True:
    characterType = input("Type of Character: ")
    if characterType == "Wizard" or characterType == "Knight" or characterType == "Teddy" or characterType == "Hero" or characterType == "Elf":
      print("----------")
      print("Welcome", characterName, "to the Fantastic World")
      print(
        f"Now you are the {characterType} on the way to save this World from Saitama"
      )
      break
    else:
      print("Not in list!")
      continue

  print("Creating Your Properties, please wait ......")
  time.sleep(2)
  
  print("----------")
  print(f"Player {playerNum} Name:", characterName)
  time.sleep(1)
  print(f"Player {playerNum} Type:", characterType)
  time.sleep(1)
  hp = creatingHp()
  print("Your HP: ", hp)
  time.sleep(1)
  strength = creatingStrength()
  print("Your Power: ", strength)
  time.sleep(1)
  print("----------")
  time.sleep(2)
  print("Let's save this Fucking World!")
  time.sleep(1)
  return {
    "Name": characterName,
    "Type": characterType,
    "HP": hp,
    "Strength": strength
  }


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
  return int(hp)


def creatingStrength():
  # bonusStrength = int(input("Type bonus for Strength: "))
  bonusStrength = 12
  strength = fomularForProperties(bonusStrength)
  return int(strength)


# Welcome
def welcome():
  print("     📷 Adventure Time 📷")
  print("------- Welcome Players --------")
  print("  --- Battles & Adventure ---")
  print()


def autoBattle():
  player1Name = players[0]["Name"]
  player2Name = players[1]["Name"]

  player1Power = players[0]["Strength"]
  player2Power = players[1]["Strength"]

  player1Health = players[0]["HP"]
  player2Health = players[1]["HP"]

  round = 1
  winner = None
  
  while True:
    player1Dice = rollDice(6)
    player2Dice = rollDice(6)

    difference = abs(player1Power - player2Power) + 1

    if player1Dice > player2Dice:
      player2Health -= difference
      if round == 1:
        print(player1Name, "wins the 1st Round")
        print("----------")
      else: 
        print(player1Name, "wins round", round)
        print("----------")
    elif player1Dice > player2Dice:
      player1Health -= difference
      if round == 1:
        print(player2Name, "wins the 1st Round")
        print("----------")
      else: 
        print(player2Name, "wins round", round)
        print("----------")
    else:
      print("Draw this round!")
      print("----------")

    print()
    print(player1Name)
    print("HEALTH:", player1Health)
    print()
    print(player2Name)
    print("HEALTH:", player2Health)
    print()
    if player1Health<=0:
      print(player1Name, "has died!")
      winner = player2Name
      break
    elif player2Health<=0:
      print(player2Name, "has died!")
      winner = player1Name
      break
    else:
      print("And they're both standing for the next round")
      round += 1
      

players = []
play = True
while play:
  os.system("clear")
  welcome()
  print("Create Your Characters? ")
  for i in range(1, 3):
    print()
    answer = input(f"Player {i} (Y/N) > ")
    if answer == "Y":
      player = creatingCharacter(i)
      players.append(player)
    else:
      print(f"Player {i} will not play!")
      break
  else:
    play = False
  print()

print("First Two of you must take a battle to find the leader! ")
print("⚔️ BATTLE TIME ⚔️")
print("Players in balltes:")
for player in players:
  print("Name: ", player["Name"])
  print("Type: ", player["Type"])
  print("HP: ", player["HP"])
  print("Strength: ", player["Strength"])
  print("----------")
autoBattle()
