# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan. 
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

# ---

# user input variables
kanta = float(input("Anna suorankulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

# calculations
piiri = 2 * (kanta + korkeus)  # piiri formula => P = 2 * (pituus + leveys)
pinta_ala = kanta * korkeus  # ala formula => Ala = kanta * korkeus

# output
print(f"Suorakulmion piiri: {piiri:.2f} ja pinta-ala: {pinta_ala:.2f}")


