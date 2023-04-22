list = []


def viewList():
  print()
  print("List of to-do items:\n")
  for i in list:
    print("-", i)
  print()


def addItem():
  item = input("What do you want to add?\n")
  list.append(item)
  print("+ List after add:")
  for i in list:
    print("-", i)


def removeItem():
  item = input("What do you want to remove?\n")
  if item in list:
    list.remove(item)
  print("+ List after remove:")
  for i in list:
    print("-", i)


while True:
  inputAction = input("View, Add or Remove? \n")
  if inputAction == "view" or inputAction == "View":
    viewList()
  elif inputAction == "add" or inputAction == "Add":
    addItem()
  elif inputAction == "remove" or inputAction == "Remove":
    removeItem()
  else:
    print("Invalid action! Please try again!")
