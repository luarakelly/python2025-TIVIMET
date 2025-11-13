from flask import Flask, jsonify
import math

app = Flask(__name__)

def onko_alkuluku(kokonaisluvun):
    onko_jopallinen_luku = kokonaisluvun % 2 == 0
    if (onko_jopallinen_luku or kokonaisluvun < 2) and kokonaisluvun != 2:
        return False
    else:
        for luku in range(2, int(math.sqrt(kokonaisluvun)) + 1):
            if kokonaisluvun % luku == 0:
                return False
        return True

@app.route('/alkuluku/<int:kokonaisluvun>', methods=['GET'])
def tarkista_alkuluku(kokonaisluvun):
    tulos = {
        "Number": kokonaisluvun,
        "isPrime": onko_alkuluku(kokonaisluvun)
    }
    return jsonify(tulos)

app.run(host='127.0.0.1', port=3000, debug=True)
