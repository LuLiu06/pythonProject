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
car=Car("ABC-123",142)

car.accelerate(60)
car.drive(1.5)
print(f"The travelled distance is: {car.travelled_distance} km")
