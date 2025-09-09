# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def summa(lista):
    return sum(lista)

def main():
    luvut = [1, 2, 3, 4, 5]  # kokonaislukuja
    tulos = summa(luvut)
    print(f"Lukujen summa on: {tulos}")

main()
