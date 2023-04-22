import os, time

listOfEmails = []


def showEmail():
  os.system("clear")
  print("listOfEmail")
  print()
  index = 1
  for email in listOfEmails:
    print(f"{index}: {email}")
    index += 1
  time.sleep(1)


def addEmail():
  email = input("Email > ")
  listOfEmails.append(email)


def removeEmail():
  email = input("Email > ")
  if email in listOfEmails:
    listOfEmails.remove(email)


def spam(number):
  for i in range(0, number):
    print(f"""Email {i+1}
      Dear {listOfEmails[i]},
      I hope this email finds you well. I am writing to request a salary update. As you know, I have been working diligently and have taken on additional responsibilities since my last salary review.
      I have been with the company for 5 years and I am committed to contributing my best efforts to support the growth and success of the company. However, I feel that my current salary does not reflect my contributions and level of expertise.
      I would like to request a salary review and a possible salary increase that is commensurate with my skills, experience, and contributions. I believe that this adjustment would help me feel more valued and motivated to continue to provide my best work.
        Thank you for considering my request. I look forward to discussing this with you further.
      Sincerely,
      Mr.Faker""")
    time.sleep(4)
    os.system("clear")


while True:
  print("SPAMMER Inc.")

  menu = input(
    "1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
  lengthList = len(listOfEmails)
  
  if menu == "1":
    addEmail()
  elif menu == "2":
    removeEmail()
  elif menu == "3":
    showEmail()
  elif menu == "4":
    if lengthList >= 10:
      spam(10)
    else:
      print("Emails don't reach number needed to spam")
  time.sleep(2)
  os.system("clear")
