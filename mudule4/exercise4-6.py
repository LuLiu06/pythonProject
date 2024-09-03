import random
user_points=int(input("How many random points you want to generate?"))
inside_points=0
for i in range(user_points):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2+y**2<1:
        inside_points+=1
pi_approximation=4*inside_points/user_points
print("The approximation of pi is: ",pi_approximation)
