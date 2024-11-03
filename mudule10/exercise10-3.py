class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor=bottom_floor
        self.top_floor=top_floor
        self.current_floor=bottom_floor

    def floor_down(self):
        if self.current_floor>self.bottom_floor:
            self.current_floor-=1
            print(f'Elevator is at {self.current_floor} floor')
        else:
            print('You are already at the bottom floor')


    def floor_up(self):
        if self.current_floor<self.top_floor:
            self.current_floor+=1
            print(f"Elevator is at {self.current_floor} floor")

        else:
            print("You are already at the top floor")

    def go_to_floor(self,target_floor):
        if target_floor>self.top_floor or target_floor<self.bottom_floor:
            print(f"{target_floor} is not valid")
            return

        while target_floor<self.current_floor:
            self.floor_down()

        while target_floor>self.current_floor:
            self.floor_up()

class Building:
    def __init__(self,bottom_floor,top_floor,num_of_elevators):
        self.bottom_floor=bottom_floor
        self.top_floor=top_floor
        self.elevators=[Elevator(bottom_floor,top_floor) for _ in range(num_of_elevators)]

    def run_elevator(self,elevator_num,target_floor):
        if elevator_num<0 or elevator_num>=len(self.elevators):
            print(f"Elevator {elevator_num} is not valid")
            return

        print(f"Running elevator {elevator_num} to floor {target_floor}")
        self.elevators[elevator_num].go_to_floor(target_floor)
    def fire_alarm(self):
        print("Fire alarm! Move all the elevators to the bottom floor!")
        for index,elevator in enumerate(self.elevators):
            print(f"Move elevator {index} to the bottom floor.")
            elevator.go_to_floor(self.bottom_floor)


if __name__=="__main__":
    building=Building(1,25,3)

    building.run_elevator(1,5)

    building.run_elevator(0,6)

    building.run_elevator(0,1)

    building.fire_alarm()