import random

# --- Assuming Auto class from previous task ---
class Auto:
    def __init__(self, nimi, max_nopeus):
        self.nimi = nimi
        self.max_nopeus = max_nopeus  # max speed in km/h
        self.nopeus = random.randint(0, max_nopeus)  # current speed
        self.matka = 0  # distance travelled in km

    def arvo_nopeusmuutos(self):
        # Randomly change speed by -10 to +10 km/h
        muutos = random.randint(-10, 10)
        self.nopeus += muutos
        # Ensure speed stays within 0 and max_nopeus
        self.nopeus = max(0, min(self.nopeus, self.max_nopeus))

    def kulje(self):
        self.matka += self.nopeus


# --- Kilpailu class ---
class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.arvo_nopeusmuutos()
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"\n{'Auto':<10} {'Matka(km)':>10} {'Nopeus(km/h)':>15}")
        print("-" * 37)
        for auto in self.autot:
            print(f"{auto.nimi:<10} {auto.matka:>10.1f} {auto.nopeus:>15}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus_km:
                return True
        return False


# --- Main program ---
# Create 10 cars
autot = [Auto(f"Auto{i+1}", random.randint(100, 200)) for i in range(10)]

# Create race
suuri_romuralli = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not suuri_romuralli.kilpailu_ohi():
    suuri_romuralli.tunti_kuluu()
    tunnit += 1
    # Print every 10 hours
    if tunnit % 10 == 0:
        print(f"\nTilanne tunnin {tunnit} jälkeen:")
        suuri_romuralli.tulosta_tilanne()

# Print final standings
print(f"\nKilpailu päättyi tunnin {tunnit} jälkeen!")
suuri_romuralli.tulosta_tilanne()
