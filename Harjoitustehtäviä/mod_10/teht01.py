class Elevator:
    def __init__(self, lowest_floor, highest_floor):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = lowest_floor
        print(f"Elevator created. Current floor: {self.current_floor}")

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


# --- Main program ---
# Create an elevator from floor 1 to 10
e = Elevator(1, 10)

# Move to floor 5
print("\nMoving to floor 5:")
e.go_to_floor(5)

# Return to the lowest floor
print("\nReturning to the lowest floor:")
e.go_to_floor(e.lowest_floor)
