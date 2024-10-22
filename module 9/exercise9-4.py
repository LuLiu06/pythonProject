import random
class Car:
    def __init__(self,registration_num,max_speed):
        self.registration_num=registration_num
        self.max_speed=max_speed
        self.current_speed=0
        self.travelled_distance=0

    def accelerate(self,change_of_speed):
        new_speed=self.current_speed+change_of_speed
        if new_speed>self.max_speed:
            self.current_speed=self.max_speed
        elif new_speed<0:
            self.current_speed=0
        else:
            self.current_speed=new_speed

    def drive(self,hours):
        self.travelled_distance+=self.current_speed*hours


#main

cars=[]
for i in range(1,11):
    max_speed=random.randint(100,200)
    registration_num=f"ABC-{i}"
    car=Car(registration_num,max_speed)
    cars.append(car)

max_distance=0
while max_distance<10000:
    for car in cars:
        car.accelerate(random.randint(-10,15))
        car.drive(1)
        if car.travelled_distance>max_distance:
            max_distance=car.travelled_distance


print(f"{'Regis num':<12}\t{'Max speed':<9}\t{'Current speed':<12}\t{'Distance travelled':<18}")
print("-------------------------------------------------------------------------")
for car in cars:
   print(f"{car.registration_num:<10}\t\t{car.max_speed:<10}\t{car.current_speed:<10}\t\t{car.travelled_distance:<10}")
