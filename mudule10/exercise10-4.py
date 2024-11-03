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


class Race:
    def __init__(self,name,distance,cars):
        self.name=name
        self.distance=distance
        self.cars=cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10,10))
            car.drive(1)

    def print_status(self):
        print(f"{'Regis num':<12}\t{'Max speed':<9}\t{'Current Speed':<12}\t{'Distance travelled':<18}")
        print("------------------------------------------------------------")
        for car in self.cars:
            print(f"{car.registration_num:<10}\t\t{car.max_speed:<10}\t\t{car.current_speed:<10}\t\t\t{car.travelled_distance:<10}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance>=self.distance:
                return True
            return False
def main():
    cars=[]
    for i in range(1,11):
        max_speed=random.randint(100,200)
        registration_num=f"ABC-{i}"
        car=Car(registration_num,max_speed)
        cars.append(car)

    race=Race("Grand Demolition Derby",8000,cars)

    hours_passed=0
    while not race.race_finished():
        race.hour_passes()
        hours_passed+=1

        if hours_passed %10==0:
            print(f"---Status after {hours_passed} hours---")
            race.print_status()

    print(f"---Final Status after {hours_passed} hours---")
    race.print_status()
    print("Race Finished!")

if __name__=='__main__':
    main()

