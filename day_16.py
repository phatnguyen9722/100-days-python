print("Fill in the blank with the correct word!")

counter = 1
while True:
    lyrics = input("My whole world ... from the moment I met you: ")
    if lyrics == "changed" or lyrics == "Changed":
        print("You got it!")
        print("next ..")
        counter2 = 1
        while True:
            lyrics2 = input("And it would never be the ...: ")
            if lyrics2 == "same" or lyrics == "Same":
                print("You got it! Well Done")
            else:
                print("Nope! Try again!")
                counter2 += 1
            if lyrics2 == "same":
                break
    else:
        print("Nope! Try again!")
        counter += 1
    if lyrics == "changed":
        break
print("Thanks for playing!")
print("You got the correct lyrics 1 in", counter, "attempt(s).")
print("You got the correct lyrics 2 in", counter2, "attempt(s).")
