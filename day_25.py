# def area_square(side1, side2):
#   area = side1 * side2
#   return area

# result = area_square(4, 12)
# print(result)

import random

print("Health Stats Generator")
print("For only Character in Video Game")
print()


def rollDice(sides):
  anySize = random.randint(1, sides)
  return anySize


def hpGenerator():
  firstDice = rollDice(6)
  secondDice = rollDice(8)
  return firstDice * secondDice


while True:
  inputCharacter = input("Your Character Name: ")
  healthCharacter = hpGenerator()
  power = rollDice(6)
  print("Character Heath: ", healthCharacter)
  print("Power: ", power)
