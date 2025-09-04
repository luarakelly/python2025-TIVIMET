# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. 
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

import math

kokonaisluvun = int(input("Anna kokonaisluvun: "))

onko_jopallinen_luku = kokonaisluvun % 2 == 0
if (onko_jopallinen_luku or kokonaisluvun < 2) and kokonaisluvun != 2:
    print(f"{kokonaisluvun} ei ole alkuluku.")
else:
    for luku in range(2, int(math.sqrt(kokonaisluvun))+1):
        if kokonaisluvun % luku == 0:
            print(f"{kokonaisluvun} ei ole alkuluku.") 
            break     
    else:
        print(f"{kokonaisluvun} on alkuluku.")

