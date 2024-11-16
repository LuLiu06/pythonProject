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
        self.travelled_distance=self.current_speed * hours

class ElectricCar(Car):
    def __init__(self,registration_num,max_speed,battery_capacity):
        super().__init__(registration_num,max_speed)
        self.battery_capacity=battery_capacity
    def print_information(self):
         print(f"Electric car {self.registration_num} | Max speed:{self.max_speed} km/h | Battery Capacity:{self.battery_capacity} kwh")

class GasolineCar(Car):
    def __init__(self,registration_num,max_speed,tank_volume):
        super().__init__(registration_num,max_speed)
        self.tank_volume=tank_volume

    def print_information(self):
        print(f"Gasoline Car {self.registration_num}| Max speed:{self.max_speed} km/h | Tank Volume:{self.tank_volume} liters")


def main():
    electric_car=ElectricCar("ABC_15",180,52.5)
    gasoline_car=GasolineCar("ABC-123",165,32.3)

    electric_car.accelerate(100)
    gasoline_car.accelerate(120)

    electric_car.drive(3)
    gasoline_car.drive(3)

    electric_car.print_information()
    print(f"Travelled distance: {electric_car.travelled_distance}")

    gasoline_car.print_information()
    print(f"Travelled distance:{gasoline_car.travelled_distance}")

if __name__=="__main__":
    main()