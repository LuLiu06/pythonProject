import random
user_input=int(input("Enter a number between 1 and 10: "))
number=random.randint(1,10)
while user_input>=1 and user_input<=10:
    if user_input==number:
        print("You've guessed the cprrect number!")
        break
    elif user_input>number:
        print("The number is too high!")
    else:
        print("The number is too low!")
    user_input=int(input("Enter a number: "))

