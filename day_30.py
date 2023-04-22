# name = "Katie"
# age = "28"
# pronouns = "she/her"

# print("This is {}, using {} pronouns, and is {} years old.".format(name, pronouns, age))

# local variables
# name = "Katie"
# age = "28"
# pronouns = "she/her"

# print("This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age))

# name = "Katie"
# age = "28"
# pronouns = "she/her"

# response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"

# print(response)

# for i in range(1, 31):
#   print(f"Day {i: <2} of 30")

print("What did you think in the past 30 days?")
print()

inputEntity = input("start? (Y/N) > ")
if inputEntity == "Y":
  start = True
else:
  start = False

while start:
  for i in range(1, 31):
    thoughtInput = input(f"Day {i}:\n")
    print("------------")
    text = f"You thought day {i} was"
    print(f"{text:^34}")
    print(f"{thoughtInput:^34}")
    print()
