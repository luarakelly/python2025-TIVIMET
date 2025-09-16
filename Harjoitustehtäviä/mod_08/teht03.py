# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen 
# etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys 
# geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla View / 
# Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
import os
from dotenv import load_dotenv
from geopy.distance import geodesic  # import geodesic for distance calculation

# Load environment variables
load_dotenv()

# Connect to the database
DB = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_LENTO_PELI"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    autocommit=True
)

def get_coordinates(icao_code):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s"
    cursor = DB.cursor()
    cursor.execute(sql, (icao_code,))
    coords = cursor.fetchone()
    if coords:
        return (coords[0], coords[1])  # (latitude, longitude)
    else:
        return None

# Ask for two ICAO codes
icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")

# Get coordinates from the database
coords1 = get_coordinates(icao1)
coords2 = get_coordinates(icao2)

if coords1 and coords2:
    distance_km = geodesic(coords1, coords2).kilometers
    print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {distance_km:.2f} kilometriä.")
else:
    if not coords1:
        print(f"Lentokenttää ICAO-koodilla '{icao1}' ei löytynyt.")
    if not coords2:
        print(f"Lentokenttää ICAO-koodilla '{icao2}' ei löytynyt.")
