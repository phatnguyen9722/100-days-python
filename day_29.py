# for i in range(0, 50):
#   print(i, end=", ")
# print(i, end="\n")
# print(i, end="\t")
# print(i, end="\v")

# print("If you put")
# print("\033[33m", end="")  #yellow
# print("nothing as the")
# print("\033[35m", end="")  #purple
# print("end character")
# print("\033[32m", end="")  #green
# print("then you don't")
# print("\033[0m", end="")  #default
# print("get odd gaps")

# print("If you put", "\033[33m", "nothing as the", "\033[35m", "end character", "\033[32m", "then you don't", "\033[0m", "get odd gaps", end="")

# import os
# import time

# print('\033[?25l', end="")
# for i in range(1, 20):
#   print(i)
#   time.sleep(0.2)
#   os.system("clear")
import os
import time


def changeTextColor(color, text):
  if color == "red" or color == "Red":
    print("\033[31m", text, sep="", end="\n")
    print()
  elif color == "green" or color == "Green":
    print("\033[32m", text, sep="", end="")
    print()
  elif color == "yellow" or color == "Yellow":
    print("\033[33m", text, sep="", end="")
    print()
  elif color == "blue" or color == "Blue":
    print("\033[34m", text, sep="", end="")
    print()
  elif color == "purple" or color == "Purple":
    print("\033[35m", text, sep="", end="")
    print()
  else:
    print("\033[0m", text, sep="", end="")
    print()


start = True
while start:
  # os.system("clear")
  print("This is App to Change Color of your text!")
  print("Option: Red, Green, Yellow, Blue, Purple")
  inputContinue = input("Continue? (Y/N) > ")
  if inputContinue == "Y" or inputContinue == "yes" or inputContinue == "Yes":
    inputText = input("Type your content here: ")
    inputColor = input("Type your color want to change here: ")
    time.sleep(1)
    changeTextColor(inputColor, inputText)
    changeTextColor("Default", "")
    continue
  else:
    start = False
print("Have a nice day!")
