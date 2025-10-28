# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu 
# matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin 
# arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma, 
# jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen 
# luodun auton kaikki ominaisuudet.

class Car:
    def __init__(self, registration, max_speed):
        """Initializes the car with registration, max speed, and sets the current speed and distance to zero."""
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_travelled = 0

# Main program: Create a new car
car = Car("123-example", 150)

# Print the car's attributes
print(f"Car Details:")
print(f"Registration: {car.registration}")
print(f"Max Speed: {car.max_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Distance Travelled: {car.distance_travelled} km")
