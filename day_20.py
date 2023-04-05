# for i in range (0, 1000, 25):
#   print(i)

print("List Generator")
inputStart = int(input("Start Number: "))
inputEnd = int(input("End Number: "))
inputIncreasement = int(input("Increasing Number: "))

for i in range (inputStart, inputEnd, inputIncreasement):
  print(i)