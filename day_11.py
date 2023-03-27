print ("This app is to calculate seconds in a year!")
print("Is this year leap or not?")
recentYear = input("Your answer: ")
dayOfYear = NotImplementedError
if recentYear == "yes":
  dayOfYear = 366
else:
  dayOfYear = 365
print("This year has",dayOfYear,"days")
transferToHours = int(dayOfYear * 24)
transferToMinutes = int(transferToHours * 60)
transferToSeconds = int(transferToMinutes * 60)
print("This year has",transferToSeconds,"seconds")