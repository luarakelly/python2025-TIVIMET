# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

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

# Main program: Create a new car
car = Car("123-example", 150)

# Print the car's initial details
print(f"Car Details:")
print(f"Registration: {car.registration}")
print(f"Max Speed: {car.max_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Distance Travelled: {car.distance_travelled} km\n")

# Accelerating the car's speed
car.accelerate(30)   # Increase speed by 30 km/h
car.accelerate(70)   # Increase speed by 70 km/h
car.accelerate(50)   # Increase speed by 50 km/h
print(f"Car speed after acceleration: {car.current_speed} km/h")

# Emergency braking (decelerate by 200 km/h)
car.accelerate(-200)
print(f"Car speed after emergency braking: {car.current_speed} km/h")
