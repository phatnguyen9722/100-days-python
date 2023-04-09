import random

print("Infinite Dice !")
sides = int(input("How many sides? "))
startGame = input("Start your game? ")


def rollDice(sides):
  gameDice = random.randint(1, sides)
  print("You rolled: ", gameDice)


while startGame == "yes":
  # rollDice(sides)
  # ansContinue = input("Roll Again? ")
  # if ansContinue == "yes":
  #   rollDice(sides)
  # else:
  #   break
  rollDice(sides)
  playgame = input("Roll Again? ")