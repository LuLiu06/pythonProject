class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor=bottom_floor
        self.top_floor=top_floor
        self.current_floor=bottom_floor

    def go_to_floor(self,target_floor):
        if target_floor<self.bottom_floor or target_floor>self.top_floor:
            print("This floor is not valid")
            return

        while target_floor<self.current_floor:
            self.floor_down()

        while target_floor>self.current_floor:
            self.floor_up()

    def floor_down(self):
        if self.current_floor>self.bottom_floor:
            self.current_floor-=1
            print(f"You are on the {self.current_floor} floor")
        else:
            print("You are already on the bottom floor")

    def floor_up(self):
        if self.current_floor<self.top_floor:
            self.current_floor+=1
            print(f"You are on the {self.current_floor} floor")
        else:
            print("You are already on the top floor")

class Building:
    def __init__(self,bottom_floor,top_floor,num_of_elevators):
        self.bottom_floor=bottom_floor
        self.top_floor=top_floor
        self.elevators=[Elevator(bottom_floor,top_floor) for _ in range(num_of_elevators)]

    def run_elevator(self,elevator_num,target_destination):
        if elevator_num<0 or elevator_num>=len(self.elevators):
            print(f"Elevator {elevator_num} is not valid")
            return
        print(f"Running elevator {elevator_num} to floor {target_destination}")
        self.elevators[elevator_num].go_to_floor(target_destination)


if __name__=="__main__":
    building=Building(0,12,3)

    building.run_elevator(1,6)

    building.run_elevator(2,3)

    building.run_elevator(0,0)