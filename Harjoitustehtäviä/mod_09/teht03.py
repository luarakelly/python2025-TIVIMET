# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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

# Main program: Create a new car
car = Car("123-example", 120)

# Print the car's initial details
print(f"Car Details:")
print(f"Registration: {car.registration}")
print(f"Max Speed: {car.max_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Distance Travelled: {car.distance_travelled} km\n")

# Accelerating the car's speed
car.accelerate(60)   # Increase speed by 30 km/h
print(f"Car speed after acceleration: {car.current_speed} km/h")

# Driving the car for 1.5 hours
car.drive(1.5)  # The car drives for 1.5 hours at the current speed
print(f"Distance traveled after 1.5 hours: {car.distance_travelled} km")

# Emergency braking (decelerate by 200 km/h)
car.accelerate(-200)
print(f"Car speed after emergency braking: {car.current_speed} km/h")

# Driving the car for another 2 hours
car.drive(2)  # The car drives for 2 hours at the new speed
print(f"Distance traveled after 2 more hours: {car.distance_travelled} km")
