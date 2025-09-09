# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. 
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. 
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def heitä_noppaa():
    return random.randint(1, 6)

noppa = heitä_noppaa()

while noppa != 6:
    print(f"Sait silmäluvun: {noppa}")
    noppa = heitä_noppaa()

print("Sait silmäluvun: 6, lopetetaan heittäminen.")