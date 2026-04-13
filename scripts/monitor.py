import os
import json
import datetime
import requests

# URL del backend
API_URL = "http://localhost:5000/registro"

def obtener_hostname():
    return os.popen("hostname").read().strip()

def obtener_usuarios():
    return os.popen("who").read()

def obtener_uptime():
    return os.popen("uptime -p").read().strip()

def enviar_datos():
    data = {
        "pc": obtener_hostname(),
        "usuarios": obtener_usuarios(),
        "uptime": obtener_uptime(),
        "timestamp": str(datetime.datetime.now())
    }

    try:
        requests.post(API_URL, json=data)
        print("Datos enviados correctamente")
    except Exception as e:
        print("Error enviando datos:", e)

if __name__ == "__main__":
    enviar_datos()