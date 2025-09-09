# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, 
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def heitä_noppaa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))

noppa = heitä_noppaa(tahkojen_maara)

while noppa != tahkojen_maara:
    print(f"Sait silmäluvun: {noppa}")
    noppa = heitä_noppaa(tahkojen_maara)

print(f"Sait silmäluvun: {tahkojen_maara}, lopetetaan heittäminen.")