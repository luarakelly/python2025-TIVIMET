# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. 
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, 
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain 
# mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()

while True:
    nimi = input('Anna nime (Tyhjä lopettaa): ')
    if nimi == '':
        print('Lopetetaan')
        break

    if nimi in nimet:
        print(f'{nimi} nimi on aiemmin syötetty.')
    else:
        print(f'{nimi} nimi on uusi')
        nimet.add(nimi)

print('Nimet lisätyneet: ')
for nimi in nimet:
    print(nimi)