import requests
import string
import csv
from datetime import datetime

# === Configuración ===
API_KEY = '7b209e22-26c0-4089-b5e6-9890fe0f3f4f'  # Reemplaza con tu API Key real
url = 'https://api.random.org/json-rpc/4/invoke'

# Longitud deseada de la contraseña
longitud_password = 16

# Caracteres que vamos a usar para la contraseña
caracteres_disponibles = string.ascii_letters + string.digits + string.punctuation

# === Función para obtener números de la API ===
def obtener_numeros(cantidad):
    payload = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": API_KEY,
            "n": cantidad,
            "min": 0,
            "max": len(caracteres_disponibles) - 1,
            "replacement": True
        },
        "id": 1
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data['result']['random']['data']
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return []

# === Generamos la contraseña ===
indices = obtener_numeros(longitud_password)
password_generada = ''.join(caracteres_disponibles[i] for i in indices)

# === Mostramos la contraseña generada ===
print(f"\n🔒 Contraseña generada con entropía natural:\n{password_generada}\n")

# === Guardamos la contraseña en un archivo CSV ===
archivo_csv = 'passwords_entropia.csv'
hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open(archivo_csv, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([hora_actual, password_generada])

print(f"✅ Contraseña guardada exitosamente en '{archivo_csv}' 📂")
