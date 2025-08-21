# Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

# ---

# user input variables
luku1 = float(input("Anna ensimmäinen kokonaisluku: "))
luku2 = float(input("Anna toinen kokonaisluku: "))
luku3 = float(input("Anna kolmas kokonaisluku: "))

# calculations
suma = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = suma / 3

# output
print(f"Lukujen summa: {suma:.2f}, tulo: {tulo:.2f}, keskiarvo: {keskiarvo:.2f}")

