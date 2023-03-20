#writeYourOwnStory
nickName = input("How can we call you?, Mr/Mrs: ")
power = input("Your ability: ")
hobbyList = input("Let us know what you like: ")
hateList = input("Something you hate: ")
friendList = input("Your happy three friends: ")

print("Hello, Mr/Mrs", nickName, "you can use your power", power, "to save",
      friendList, "and the \033[31m'world'\033[0m. We know you love",
      hobbyList, "and hate", hateList, "but we don't care, see ya'", nickName)