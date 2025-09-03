# Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

alku_num = 1
loppu_num = 1000

while alku_num <= loppu_num:
    if alku_num % 3 == 0:
        print(alku_num)
    alku_num += 1