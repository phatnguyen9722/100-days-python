from getpass import getpass as input
print("Choose a number from 0 to 1,000,000")
inputNumber = int(input("Type your number: "))

counter = 0
while True: 
  print("Guest The Number ^^ ")
  inputUser =  int(input("Type your number: "))
  if inputNumber == inputUser:
    print("Congrats! You're the Winner!")
    print("You try in",counter, "times")
    break
  else:
    counter += 1
    print("Try Again")
    if inputNumber > inputUser:
      print("Your number is lower than expected")
    elif inputNumber < inputUser:
      print("Your number is higher than expected")
    continue