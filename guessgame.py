# guess the number 
import random

number = random.randint(1 , 100)
attempt = 0
while True:
    num = int(input("Enter a number"))
    attempt = attempt + 1
    if num == number:
        print("you got it")
        break

    elif num > number:
        print("too high")

    elif num < number:
        print("too low")
print("your attempts:",attempt)