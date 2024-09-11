import random
num_dice=int(input("How many dices do you want to roll?"))
total_sum=0
for i in range(num_dice):
    number=random.randint(1,6)
    total_sum+=number
print("The total sum is: ",total_sum)