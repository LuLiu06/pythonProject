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

#main
car=Car("ABC-123",142)
car.accelerate(30)
print(f"Curren speed after increased by 30km/h: {car.current_speed} km/h")

car.accelerate(70)
print(f"Current speed after increased by 70km/h:{car.current_speed} km/h")

car.accelerate(50)
print(f"Current speed after increased by 50km/h:{car.current_speed} km/h")

car.accelerate(-200)
print(f"Current speed after increased by -200km/h:{car.current_speed} km/h")
