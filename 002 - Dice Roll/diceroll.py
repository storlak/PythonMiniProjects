import random
import time

print("Welcome to the dice roll simulator")
print("**********************************")

while True:
    askuser = input("Do you want to roll the dice? (y/n): ").lower()
    if askuser == "y" or askuser == "yes":
        print("Rolling...")
        time.sleep(1.5)
        num = random.randint(1, 6)
        print("You got", num, "!")
    elif askuser == "n" or askuser == "no":
        print("Not cool! Goodbye!")
        break
    else:
        print("Invalid input")
