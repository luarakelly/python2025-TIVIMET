# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random

arpakuutioiden_lukumäärän = int(input("Antaa arpakuutioiden lukumäärän: "))

if arpakuutioiden_lukumäärän <= 0:
    print("Lukumäärän tulee olla positiivinen kokonaisluku.")

silmälukujen_summa = 0

for noppa in range(arpakuutioiden_lukumäärän):
    noppa_heittäminen = random.randint(1, 6)
    silmälukujen_summa += noppa_heittäminen

print(f"Silmälukujen summan on: {silmälukujen_summa}")
