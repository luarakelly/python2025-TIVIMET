# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. 
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, 
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuhan_pitus = float(input("Anna kuhan pitus senttimetreinä: "))

if kuhan_pitus < 37:
    puuttuu = 37 - kuhan_pitus
    print(f"Kuha on alamittainen, laske se takaisin järveen. Pyyntimitasta puuttuu {puuttuu:.1f} cm.")
else:
    print("Kuha on sallittu pyyntimitan mukainen.")
