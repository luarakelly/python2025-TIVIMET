from flask import Flask, jsonify
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_LENTO_PELI"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        autocommit=True
    )

def hae_airport_(icao_koodi):
    yhteys = get_db_connection()
    kursori = yhteys.cursor()
    sql = "SELECT name, municipality FROM airport WHERE ident=%s;"
    kursori.execute(sql, (icao_koodi,))
    tulos = kursori.fetchall()
    kursori.close()
    yhteys.close()

    if len(tulos) > 0:
        rivi = tulos[0]
        return {"ICAO": icao_koodi.upper(), "Name": rivi[0], "Municipality": rivi[1]}
    else:
        return {"error": f"Airport with ICAO code '{icao_koodi}' not found"}

@app.route('/kenttä/<icao_koodi>', methods=['GET'])
def hae_kentta(icao_koodi):
    return jsonify(hae_airport_(icao_koodi))

app.run(host=os.getenv("API_HOST"), port=3000, debug=True)
