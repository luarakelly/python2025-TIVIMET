# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. 
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. 
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. 
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

arvottu_luku = random.randint(1, 10)
arvaus = 0

while arvaus != arvottu_luku:
    arvaus = int(input("Arvaa luku väliltä 1-10: "))
    if arvaus < arvottu_luku:
        print("Liian pieni arvaus")
    elif arvaus > arvottu_luku:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
