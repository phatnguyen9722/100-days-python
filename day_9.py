# INT
# myScore = int(input("Your score: "))
# if myScore > 100000:
#   print("Winner!")
# else:
#   print("Try again 😭")

# FLOAT
# myPi = float(input("What is Pi to 3dp? "))
# if myPi == 3.142 :
#   print("Exactly!")
# else:
#   print("Try again 😭")

# FIX CODE 1:
# myPi = float(input("What is Pi to 3dp? "))
# if myPi == 3.142 :
#   print("Exactly!")
# else:
#   print("Try again 😭")

# FIX CODE 2:
# myPi = float(input("What is Pi to 3dp?"))
# if myPi == 3.142 :
#   print("Exactly!")
# else:
#   print("Try again 😭")

# Fix CODE 3:
# score = int(input("What was your score on the test?"))
# if score >= 80:
#   print("Not too shabby")
# elif score > 70:
#   print("Acceptable.")
# else:
#   print("Dude, you need to study more!")

# Challenge Day 9:

birthdayInput = int(input("You was born in: "))
if (birthdayInput >= 1925) and (birthdayInput <= 1946):
    print("You are a part of Traditionalists 😅")
elif (birthdayInput > 1946) and (birthdayInput <= 1964):
    print("You are a part of Baby Boomers 🤣")
elif (birthdayInput > 1964) and (birthdayInput <= 1981):
    print("You are a part of Generation X 🫠")
elif (birthdayInput > 1981) and (birthdayInput <= 1995):
    print("You are a part of Millenials 😊")
else:
    print("You are a part of Generation Z 😀")
