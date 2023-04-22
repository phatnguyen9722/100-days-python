listName = []


def printFullName():
  print()
  for name in listName:
    print("Name: ", name)
  print()


while True:
  firstName = input("Your First Name: ").strip().capitalize()
  lastName = input("Your Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in listName:
    listName.append(name)
  else:
    print("Duplicate Name, please check it out!")
  printFullName()
