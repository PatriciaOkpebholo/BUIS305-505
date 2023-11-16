# Request a number from user

for number1 in range (20):
    if number1% 3== 0 and number1% 5== 0:
        print(number1, "Tic Tac")
    elif( number1 % 3 == 0):
        print(number1, "Tic")
    elif(number1 % 5 == 0):
        print(number1, "Tac")
    else:
        print(number1,"The number is not divisible by either 3 or 5")

# print number from 1 to 20 using the while loop

number1=1
while number1<=20:
    print(number1)
    number1+=1

# print only one of them if it satisfies the condition.

number1=int(input("enter number"))
count=1
while number1 < 16:
    number1=number1+1
    if number1 % 3 == 0 and number1 % 5 == 0:
        print ("Tic Tac")
    elif number1 % 3 == 0:
        print("Tic")
    elif number1 % 5 == 0:
        print("Tac")

# import ramdom by generating random integer between 1 and 10

import random
random_number=random.randint(1,100)
count=0
while count<5:
    user_number=int(input("enter a number greater than 0:"))
    if user_number >0:
        break
    else:
        count+=1
        print("Invalid Input. Please enter a number greater than 0:")


import random

random_number = random.randint(1, 100)
attempts = 0
while attempts < 5:
    user_value = int(input("Enter a positive integer: "))
    if user_value > 0:
        break
    else:
        print("Value must be greater than 0. Try again.")
        attempts += 1

if attempts == 5:
    print("You exceeded the maximum number of attempts.")
else:
    if random_number == user_value:
        print("Perfect match!")
    else:
        print(f"Random number: {random_number}, Your number: {user_value}. Numbers don't match.")

