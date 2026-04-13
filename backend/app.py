from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json"

# Crear archivo si no existe
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.route("/registro", methods=["POST"])
def registro():
    data = request.json

    with open(DATA_FILE, "r") as f:
        registros = json.load(f)

    registros.append(data)

    with open(DATA_FILE, "w") as f:
        json.dump(registros, f, indent=4)

    return jsonify({"mensaje": "Registro guardado"}), 200


@app.route("/registros", methods=["GET"])
def obtener_registros():
    with open(DATA_FILE, "r") as f:
        registros = json.load(f)

    return jsonify(registros)


if __name__ == "__main__":
    app.run(debug=True)