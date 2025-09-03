# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. 
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. 
# (Oikea käyttäjätunnus on python ja salasana rules).

# luo tilin tiedot 
luo_käyttäjätunnus = input("Luo käyttäjätunnus: ")
luo_salasana = input("Luo salasana: ")

# kirjaudy
käyttäjätunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

# tarkastetaan onko tunnus ja salasana oikein
yritykset = 1

while yritykset <= 5:
    if käyttäjätunnus == luo_käyttäjätunnus and salasana == luo_salasana:
        print("Tervetuloa.")
        break
    elif käyttäjätunnus != luo_käyttäjätunnus or salasana != luo_salasana:
        if yritykset == 5:
            print("Pääsy evätty.")
            break
    
        print("Väärä käyttäjätunnus tai salasana, yritä uudelleen.")
        käyttäjätunnus = input("Anna käyttäjätunnus: ")
        salasana = input("Anna salasana: ")
    
    yritykset += 1