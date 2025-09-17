# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien 
# lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä 
# lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector
import os 
from dotenv import load_dotenv

load_dotenv()
# secret variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_LENTO_PELI = os.getenv("DB_LENTO_PELI")
DB_PORT = os.getenv("DB_PORT")
DB_HOST = os.getenv("DB_HOST")

#connect to data base
DB = mysql.connector.connect(
    host= DB_HOST,
    port= DB_PORT,
    database= DB_LENTO_PELI,
    user= DB_USER,
    password= DB_PASSWORD,
    autocommit=True
)

def lentokenttien_lukumäärät_tyypeittäin(maakoodin):
    sql = "SELECT type FROM airport WHERE iso_country=%s"
    cursor = DB.cursor()
    cursor.execute(sql, (maakoodin,))
    lentokenta_tyypit = cursor.fetchall()

    counter = {}
    for row in lentokenta_tyypit:
        #print(row)
        lentokenta_tyypi = row[0] 
        if lentokenta_tyypi in counter:
            counter[lentokenta_tyypi] += 1
        else:
            counter[lentokenta_tyypi] = 1   
    
    return counter

maakoodin = input("Anna maakoodin (esimerkiksi FI): ")
counted = lentokenttien_lukumäärät_tyypeittäin(maakoodin)

print(f"pieniä lentokenttiä on: {counted['small_airport']}, helikopterikenttiä on: {counted['heliport']}, keski lentokenttiä: {counted['medium_airport']} ja iso lentokenttiä on: {counted['large_airport']}")