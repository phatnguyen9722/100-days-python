# # Fix Code

# # multiplication
# multiple = 3.4 * 6.8
# print(multiple)

# # division
# division = 2467 / 4673
# print(division)

# #raise 10 to the power of 2
# power = pow(10,2)
# print(power)

# # print the remainder when 343 is divided by 4
# remainder = 343 % 4
# print(remainder)


# myBill = float(input("What was the bill?: "))
# numberOfPeople = int(input("How many people?: "))
# answer = myBill / numberOfPeople
# answerFinal = round(answer)
# print("You all owe", answerFinal)

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tipNumber = float(input("Your % tip: "))

bill_with_tip = tipNumber / 100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_amount = round(bill_per_person, 2)

print("You all owe", final_amount)
 
