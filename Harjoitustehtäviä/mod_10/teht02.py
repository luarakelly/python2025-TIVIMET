class Elevator:
    def __init__(self, lowest_floor, highest_floor):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = lowest_floor

    def floor_up(self):
        if self.current_floor < self.highest_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")
        else:
            print("Elevator is already at the highest floor!")

    def floor_down(self):
        if self.current_floor > self.lowest_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")
        else:
            print("Elevator is already at the lowest floor!")

    def go_to_floor(self, target_floor):
        if target_floor < self.lowest_floor or target_floor > self.highest_floor:
            print("Error: Target floor is out of range.")
            return
        
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, lowest_floor, highest_floor, num_elevators):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.elevators = [Elevator(lowest_floor, highest_floor) for _ in range(num_elevators)]
        print(f"Building created with {num_elevators} elevators, floors {lowest_floor} to {highest_floor}.")

    def operate_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nOperating elevator {elevator_number} to floor {target_floor}:")
            self.elevators[elevator_number].go_to_floor(target_floor)
        else:
            print("Error: Invalid elevator number.")


# --- Main program ---
# Create a building with 1-10 floors and 3 elevators
my_building = Building(1, 10, 3)

# Move elevator 0 to floor 5
my_building.operate_elevator(0, 5)

# Move elevator 1 to floor 8
my_building.operate_elevator(1, 8)

# Return elevator 0 to the lowest floor
my_building.operate_elevator(0, my_building.lowest_floor)
