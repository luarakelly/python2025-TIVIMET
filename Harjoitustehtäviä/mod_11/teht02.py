# Superclass
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

# ElectricCar subclass
class ElectricCar(Car):
    def __init__(self, registration, max_speed, battery_capacity):
        super().__init__(registration, max_speed)  # Call the Car initializer
        self.battery_capacity = battery_capacity  # kWh

# GasCar subclass
class GasCar(Car):
    def __init__(self, registration, max_speed, fuel_tank):
        super().__init__(registration, max_speed)  # Call the Car initializer
        self.fuel_tank = fuel_tank  # liters


# Create one electric car and one gas car
electric_car = ElectricCar("ABC-15", 180, 52.5)
gas_car = GasCar("ACD-123", 165, 32.3)

# Set their speeds (using accelerate)
electric_car.accelerate(150)  # set speed to 150 km/h
gas_car.accelerate(140)       # set speed to 140 km/h

# Drive for 3 hours
electric_car.drive(3)
gas_car.drive(3)

# Print the distance travelled (odometer)
print(f"Electric car ({electric_car.registration}) distance: {electric_car.distance_travelled} km")
print(f"Gas car ({gas_car.registration}) distance: {gas_car.distance_travelled} km")
