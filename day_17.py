# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")
#     exit()
# print("The game is over, you've failed!")
from getpass import getpass as input
print("This is Rock, Paper, Scissors game! ")
print("--- Basic Rules for two players ---")
print("Rock: R, Paper: P, Scissors: S")


counter1 = 0 
counter2 = 0
while True:
  print("Player 1 > ")
  inputPlayer1 = input("You choose R, S or P: ")
  print("Player 2 > ")
  inputPlayer2 = input("You choose R, S or P: ")
  print()
  
  if(inputPlayer1=="R"):
    if(inputPlayer2=="R"):
      print("Draw")
    elif(inputPlayer2=="S"):
      print("Player 1 Won")
      counter1 += 1
    elif(inputPlayer2=="P"):
      print("Player 2 Won")
      counter2 += 1
  elif(inputPlayer1=="S"):
    if(inputPlayer2=="S"):
      print("Draw")
    elif(inputPlayer2=="R"):
      print("Player 2 Won")
      counter2 += 1
    elif(inputPlayer2=="P"):
      print("Player 1 Won")
      counter1 += 1
  elif(inputPlayer1=="P"):
    if(inputPlayer2=="P"):
      print("Draw")
    elif(inputPlayer2=="S"):
      print("Player 2 Won")
      counter2 += 1
    elif(inputPlayer2=="R"):
      print("Player 1 Won")
      counter1 += 1  
  print("Player 1 has", counter1, "wins.")
  print("Player 2 has", counter2, "wins.")
  
  if inputPlayer1 == 3 or inputPlayer2==3:
    print("End Game!")
    exit()
  else:
    print("--- Next Round ---")
    continue