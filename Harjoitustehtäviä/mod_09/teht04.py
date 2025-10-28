#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

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

# Main program: Create a list of 10 cars
cars = []

# Create 10 cars with random max speed between 100 km/h and 200 km/h
for i in range(1, 11):
    registration = f"ABC-{i}"
    max_speed = random.randint(100, 200)  # Random max speed between 100 and 200 km/h
    car = Car(registration, max_speed)
    cars.append(car)

# Race simulation: Start the race
race_over = False
hour = 0

while not race_over:
    hour += 1
    for car in cars:
        # Randomly change the car's speed between -10 and +15 km/h
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        
        # Drive the car for 1 hour
        car.drive(1)
    
    # Check if any car has traveled at least 10,000 km
    for car in cars:
        if car.distance_travelled >= 10000:
            race_over = True
            break

# Print the race results in a table format
print(f"{'Registration':<12} {'Max Speed':<12} {'Speed':<8} {'Distance Traveled':<16}")
print("-" * 50)

for car in cars:
    print(f"{car.registration:<12} {car.max_speed:<12} {car.current_speed:<8} {car.distance_travelled:<16}")
