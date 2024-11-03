class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor=bottom_floor
        self.top_floor=top_floor
        self.current_floor=bottom_floor

    def go_to_floor(self,target_floor):
        if target_floor>self.top_floor or target_floor<self.bottom_floor:
            print(f"{target_floor} is not valid.")
            return

        while target_floor<self.current_floor:
            self.floor_down()

        while target_floor>self.current_floor:
            self.floor_up()

    def floor_down(self):
        if self.current_floor>self.bottom_floor:
            self.current_floor-=1
            print(f"Elevator is at {self.current_floor} floor")
        else:
            print("You are already at the bottom floor")

    def floor_up(self):
        if self.current_floor<self.top_floor:
            self.current_floor+=1
            print(f"Elevator is at {self.current_floor} floor")
        else:
            print("You are already at the top floor.")

if __name__=="__main__":
    elevator=Elevator(0,12)

    elevator.go_to_floor(6)

    elevator.go_to_floor(0)