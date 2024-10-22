class Car:
    def __init__(self,registration_num,max_speed):
        self.registration_num=registration_num
        self.max_speed=max_speed
        self.current_speed=0
        self.travelled_distance=0

car=Car("ABC-123",142)

print(f"Registration Number:{car.registration_num}")
print(f"Max Speed:{car.max_speed}")
print(f"Current Speed:{car.current_speed}")
print(f"Travelled Distance:{car.travelled_distance}")
