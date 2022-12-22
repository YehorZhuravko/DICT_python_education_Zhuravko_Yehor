print("Hello! My name is Chat Bot.")
print("I was created in 2022.")
print("Please, remind me your name.")
user_input = input()
print("What a great name you have,",user_input)
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int (input())
remainder5 = int (input())
remainder7 = int (input())
user_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is", user_age, "that's a good time to start programming!E")
print ("Now I will prove to you that I can count to any number you want.")
user_number = int (input())
user_start_number = 0
while user_start_number < user_number:
    user_start_number += 1
    print(user_start_number,"!")
print("Let's test your programming knowledge.")
print ('''
What is the correct file extension for Python files?
1. .pyth
2. .py
3. .pt
4. .pyt
''')
user_answer = int (input())
while user_answer != 2:
    print ("Please, try again.")
    user_answer = int(input())
print('''
Completed, have a nice day!
Congratulations, have a nice day!''')
