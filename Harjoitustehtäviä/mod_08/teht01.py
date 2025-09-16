# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. 
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. 
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector
import os # importing os module for environment variables
from dotenv import load_dotenv

load_dotenv() # loading variables from .env file
# secret variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_LENTO_PELI = os.getenv("DB_LENTO_PELI")
DB_PORT = os.getenv("DB_PORT")
DB_HOST = os.getenv("DB_HOST")

#connect to data base
yhteys = mysql.connector.connect(
    host= DB_HOST,
    port= DB_PORT,
    database= DB_LENTO_PELI,
    user= DB_USER,
    password= DB_PASSWORD,
    autocommit=True
)

def hae_airport_(icao_Koodi):
    # NON parameterized query:
    # f"SELECT name, municipality FROM airport WHERE ident='{icao_Koodi}';"
    # parameterized query: Avoids sql injection =>
    sql = "SELECT name, municipality FROM airport WHERE ident=%s;"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao_Koodi,)) # <- Needs a coma here to make it a tuple.
    tulos = kursori.fetchall()

    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"lentokentän nimen: {rivi[0]} ja sen sijaintikunnan: {rivi[1]}.")
    else:
        print(f"Ei löytynyt ICAO-koodi: {icao_Koodi}.")

    return 

icao_koodi = input('Anna ICAO-koodi: ')
hae_airport_(icao_koodi)