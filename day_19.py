print("Loan Calculator")
inputMoney = int(input("Input your money you owe: "))
# inputRate = int(input("Input your rate %: "))
rate = 0.05
for i in range(10):
  inputMoney+=(inputMoney*rate)
  print("Year", i+1, "is", round(inputMoney,2))