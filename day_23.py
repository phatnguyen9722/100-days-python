# Subroutine
# import random

# def rollDice():
#     dice = random.randint(1, 6)
#     print("You rolled", dice)

# for i in range(10):
#   rollDice()
userName = "ntanphat2"
password = "@123"
print("username: ", userName)
print("password:", password)


def userLogin():
    while True:
        inUser = input("Type user name: ")
        inPass = input("Type your password: ")
        if inUser == userName and inPass == password:
            print("Login Successful!")
            break
        else:
            print("Try again!")
            continue

print("Login Form")
userLogin()
