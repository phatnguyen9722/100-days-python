import os, time

toDoList = []


# Features
def printList():
  print()
  for items in toDoList:
    print("-", items)
  print()
  time.sleep(2)


def addItem():
  item = input("What do you want to add?\n").title()
  toDoList.append(item)


def removeItem():
  item = input("What do you want to remove?\n").title()
  check = input("Are you sure you want to remove this?\n")
  if check[0] == "y":
    if item in toDoList:
      toDoList.remove(item)


def editList():
  item = input("What do you want to edit?\n").title()
  new = input("What do you want to change it to?\n").title()
  for i in range(0, len(toDoList)):
    if toDoList[i] == item:
      toDoList[i] = new


def clearList(list):
  return list.clear()


while True:
  menu = input(
    "ToDo List Manager\nDo you want to view, add, edit, remove or clear?\n")

  # Options
  if menu == "view":
    printList()
  elif menu == "add":
    addItem()
    printList()
  elif menu == "remove":
    removeItem()
    printList()
  elif menu == "edit":
    editList()
    printList()
  elif menu == "clear":
    clearList(toDoList)
  time.sleep(1)
  os.system('clear')
