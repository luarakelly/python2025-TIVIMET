# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. 
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai 
# lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin 
# ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. 
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa 
# tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. 
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

# === Airport data ===
lentoasemat = {
    'YYE' : 'Example1'
}

# === Vaehtoehdot ilmoitautuminen ===
print('=== VAIHTOEHDOT ===')
print('1. Lisää uusi lentoasema')
print('2. Hae lentoasema nimi')
print('3. lopettaa. ')

print('=== LENTOASEMAT TIETTY ===')
for icao in lentoasemat:
    print(icao)

while True:
    valinta = int(input('Syötää valintan numeron (1-3): '))
    # === Input checker ===
    if valinta < 1 or valinta > 3:
        print('Väärin valinta. Valitsee 1-3.')

    if valinta == 1:
        ICAO_koodin = input('Antaa lentoaseman ICAO-koodin: ')
        nimi = input('Antaa lentoaseman nimi: ')
        lentoasemat[ICAO_koodin] = nimi
        print(f'Lentoasema: {nimi}, ja ICAO-koodi: {ICAO_koodin} on lisätty.')

    elif valinta == 2:
        ICAO_koodin = input('Antaa haettavan lentoaseman ICAO-koodin: ')
        if ICAO_koodin in lentoasemat:
            print(f'Lentoaseman nimi: {lentoasemat[ICAO_koodin]}')
        else:
            print('Ei löyttyy.Tarkisttaa tietty lentoasemat ICAO-koodit.')

    else:
        print('Lopetetaan nyt.')
        break