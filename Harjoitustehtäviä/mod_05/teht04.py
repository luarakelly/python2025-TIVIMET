# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan 
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen. 
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. 
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

kaupungin_nimet = []
for _ in range(5):
    kaupungin_nime = input("Antaa kaupungin nimen: ")
    kaupungin_nimet.append(kaupungin_nime)   

for name in kaupungin_nimet:
    print(name) 