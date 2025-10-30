import random

class Car:
    def __init__(self, registration, max_speed):
        """Initializes the car with registration, max speed, and sets the current speed and distance to zero."""
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_travelled = 0
    
    def accelerate(self, speed_change):
        """Changes the car's speed. Speed cannot exceed max_speed or go below 0."""
        new_speed = self.current_speed + speed_change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed
    
    def drive(self, hours):
        """Increases the traveled distance based on the current speed for the given number of hours."""
        distance_covered = self.current_speed * hours
        self.distance_travelled += distance_covered

# --- Kilpailu (Race) class ---
class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Car':<12} {'Distance(km)':>15} {'Speed(km/h)':>15}")
        print("-" * 45)
        for car in self.cars:
            print(f"{car.registration:<12} {car.distance_travelled:>15.1f} {car.current_speed:>15}")

    def is_over(self):
        return any(car.distance_travelled >= self.distance_km for car in self.cars)


# --- Main program ---
# Create 10 cars with random max speed between 100 and 200 km/h
cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

# Create race
big_race = Race("Suuri romuralli", 8000, cars)

hours = 0
while not big_race.is_over():
    big_race.hour_passes()
    hours += 1
    # Print status every 10 hours
    if hours % 10 == 0:
        print(f"\nStatus after hour {hours}:")
        big_race.print_status()

# Print final results
print(f"\nRace ended after {hours} hours!")
big_race.print_status()
