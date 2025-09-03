# Kirjoita ohjelma, joka muuntaa tuumia(inch) senttimetreiksi niin kauan kunnes käyttäjä 
# antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuumia = float(input("Anna tuumamäärä: "))

while tuumia <= 0:
    senttimetreja = tuumia * 2.54
    print(f"{tuumia} tuumaa on {senttimetreja} cm")
    tuumia = float(input("Anna tuumamäärä: "))