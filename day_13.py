nameTest = input("Please, your test name here: ")
maxScore = int(input("Max score of test: "))
currentScore = float(input("Your score: "))
percentageScore = (currentScore/maxScore)*100
roundPercentageScore = round(percentageScore,3)
print("You got",roundPercentageScore,"%")

if roundPercentageScore < 50:
  print("Grade U")
elif roundPercentageScore < 60:
  print("Grade D")
elif roundPercentageScore < 70:
  print("Grade C")
elif roundPercentageScore < 80:
  print("Grade B")
elif roundPercentageScore < 90:
  print("Grade A")
else: 
  print("\033[1;32m Excellent, Grade A+ !")