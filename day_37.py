# myString = "Hello there my friend."
# print(myString[::-1])

#This code reverses the string, outputting '.dneirf ym ereht olleH'

print("STAR WARS NAME GENERATOR")
print()

print("-----------------------")
firstName = input("Your First Name > ")
lastName = input("Your Last Name > ")
maidenName = input("Your Mother's Maiden Name > ")
cityName = input("Your City: ")
sliceFirstName = firstName[:3].title()
sliceLastName = lastName[:3]
sliceMaidenName = maidenName[:2].title()
sliceCityName = cityName[:3]
print("-----------------------")


def combineFirstName(fname, lname):
  starWarFirstName = f"{fname}{lname}"
  return starWarFirstName


def combineLastName(mdname, cityname):
  starWarLastName = f"{mdname}{cityname}"
  return starWarLastName


userFirstName = combineFirstName(sliceFirstName, sliceLastName)
userLastName = combineLastName(sliceMaidenName, sliceCityName)
name = f"{userFirstName} {userLastName}"
print(f"Your Star Wars full name: {name}")
