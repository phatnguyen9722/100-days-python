import random

# myNumber = random.randint(1,100)
# print(myNumber)

# for i in range(10):
#   myNumber = random.randint(1, 100)
#   print(myNumber)

from getpass import getpass as input

print("Choose a number from 0 to 1,000,000")
guestNumber = random.randint(1, 1000000)
attempt = 1
while True:
    print("Guest The Number ^^ ")
    inputUser = int(input("Type your number: "))
    if inputUser == guestNumber:
        print("Congrats! You're the Winner!")
        print("You try in", attempt, "times")
        break
        exit()
    elif inputUser > guestNumber:
        attempt += 1
        print("Your number is higher than expected")
        continue
    elif inputUser < guestNumber:
        attempt += 1
        print("Your number is lower than expected")
        continue
    else:
        print("That is not a number I recognize.")
