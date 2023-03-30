from getpass import getpass as input
print("This is Rock, Paper, Scissors game! ")
print("--- Basic Rules for two players ---")
print("Rock: R, Paper: P, Scissors: S")
print("Player 1 > ")
inputPlayer1 = input("You choose R, S or P: ")
print("Player 2 > ")
inputPlayer2 = input("You choose R, S or P: ")

if inputPlayer1 == "R" and inputPlayer2 == "S":
  print("Player 1 Won!")
elif inputPlayer1 == "R" and inputPlayer2 == "P":
  print("Player 2 Won!")
elif inputPlayer1 == "R" and inputPlayer2 == "R":
  print("Draw, play again!")
elif inputPlayer1 == "S":
  if inputPlayer2 == "R":
    print("Player 2 Won!")
  elif inputPlayer2 == "P":
    print("Player 1 Won!")
  else:
    print("Draw, play again")
else: 
  if inputPlayer2 == "R":
    print("Player 1 Won!")
  elif inputPlayer2 == "S":
    print("Player 2 Won!")
  else:
    print("Draw, play again") 