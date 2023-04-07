print("Welcome to Multiple Math Game")
print()
inputMultiple = int(input("Multiples of: "))
print()
counter = 0
for i in range(1, 11):
  correct_answer = i*inputMultiple
  print(i, "x", inputMultiple)
  answer = int(input("> "))
  if answer == correct_answer:
    print("Perfect!")
    counter += 1
  else:
    print("That's not correct. It should have been", correct_answer)
if counter == 10:
  print("Wow! A perfect score! 🥳")
else:
  print("You got", counter, "scores out of 10 correct.")