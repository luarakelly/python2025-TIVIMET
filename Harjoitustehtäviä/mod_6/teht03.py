# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina 
# ja palauttaa paluuarvonaan vastaavan litramäärän. 
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. 
# Muunnos on tehtävä aliohjelmaa hyödyntäen. 
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def gallona_litra(gallonat):
    return gallonat * 3.785

gallonat = 0
while gallonat >= 0:
    gallonat = float(input("Anna bensiinin määrä gallonoina (negatiivinen luku lopettaa): "))
    if gallonat >= 0:
        litrat = gallona_litra(gallonat)
        print(f"{gallonat} gallonaa on {litrat:.2f} litraa.")

print("Lopetetaan ohjelma.")

