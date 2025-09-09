# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. 
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. 
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, 
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). 
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * (sade ** 2) / 10000  # Muutetaan neliösenttimetrit neliömetreiksi
    return hinta / pinta_ala

def main():
    halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
    hinta1 = float(input("Anna ensimmäisen pizzan hinta (euroa): "))
    halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
    hinta2 = float(input("Anna toisen pizzan hinta (euroa): "))

    yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)

    print(f"Ensimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} euroa/neliömetri")
    print(f"Toisen pizzan yksikköhinta: {yksikkohinta2:.2f} euroa/neliömetri")

    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta1 > yksikkohinta2:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmilla pizzoilla on sama yksikköhinta.")

main()