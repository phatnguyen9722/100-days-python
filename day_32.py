import random
greetings = ["Xin chào!", "Hi, guy!", "你好", "How are you today?", "Konnichiwa", "nyoung haseyo"]
maxLength = len(greetings) - 1
index = random.randint(0, maxLength)
print(greetings[index])
