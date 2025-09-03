# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, 
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku = input("Antaa lukuja: ")

pienimän = luku
suurimman = luku

while luku:
    if luku >= suurimman:
        suurimman = luku
    elif luku <= pienimän:
        pienimän = luku
    
    luku = input("Antaa lukuja: ")

print(f"Pienimmän luku: {pienimän}, suurimman luku: {suurimman}")