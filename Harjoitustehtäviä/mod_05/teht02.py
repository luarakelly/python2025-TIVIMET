# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, 
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

luku = input("Anna luku: ")

luvut = []

while luku != "":
    luvut.append(int(luku))
    luku = input("Anna luku: ")

suurimmasta_alkaen = luvut.sort(reverse=True)

print(f"Viisi suurinta lukua ovat: {luvut[0:5]}")