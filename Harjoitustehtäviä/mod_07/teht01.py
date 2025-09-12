# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, 
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, kesä, talvi). 
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, 
# että joulukuu on ensimmäinen talvikuukausi.

# === Constants === 
kuukaudet_nimet = ('Tammikuu', 'Helmikuu', 'Maaliskuu', 'Huhtikuu', 'Toukokuu', 'Kesäkuu', 'Heinakuu', 'Elokuu', 'Syyskuu', 'Lokakuu', 'Marraskuu', 'Joulukuu')
vuodenajat = ('talvi', 'kevät', 'kesä', 'syksy') 

# === Answer builder ===
def vuodenajan_vastaus(kuukauden_n):
    # === Input checker ===
    if kuukauden_n > 12 or kuukauden_n < 1:
        return print('Väärin kuukauden numeron, pitäisin olla 1-12 välillä.')
    
    vuodenajan = ''
    kuukauden_nimen = kuukaudet_nimet[kuukauden_n-1]
    
    # === Season logic ===
    if kuukauden_n < 3: # talvi
        vuodenajan = vuodenajat[0]
    elif kuukauden_n < 6: # kevät
        vuodenajan = vuodenajat[1]
    elif kuukauden_n < 9: # kesä
        vuodenajan = vuodenajat[2]
    else: # syksy
        vuodenajan = vuodenajat[3]

    return f'Kuukauden: {kuukauden_n} = {kuukauden_nimen}, vuodenajan on {vuodenajan}!'

kuukauden_numeron = int(input("Annaa kuukauden numero (1-12): "))
print(vuodenajan_vastaus(kuukauden_numeron))