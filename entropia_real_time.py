import requests
import matplotlib.pyplot as plt
import time

# === Configuración inicial ===
API_KEY = '7b209e22-26c0-4089-b5e6-9890fe0f3f4f'  # Reemplaza por tu key
url = 'https://api.random.org/json-rpc/4/invoke'

# Almacenamos los datos a lo largo del tiempo
historial = []

# Cantidad de ciclos que quieres que tome (ejemplo: 10 ciclos)
num_ciclos = 10

# === Función para obtener números de la API ===
def obtener_numeros():
    payload = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": API_KEY,
            "n": 100,        # Cantidad de números por ciclo
            "min": 0,
            "max": 100,
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

# === Recolección de datos en tiempo real ===
for ciclo in range(num_ciclos):
    print(f"Ciclo {ciclo + 1}/{num_ciclos}")
    numeros = obtener_numeros()
    if numeros:
        promedio = sum(numeros) / len(numeros)
        historial.append(promedio)
        print(f"Promedio del ciclo: {promedio}")
    else:
        historial.append(0)

    time.sleep(2)  # Espera 2 segundos entre ciclos para simular tiempo real

# === Visualización final ===
plt.plot(historial, marker='o')
plt.title('Evolución de la Entropía Atmosférica (Ruido Real)')
plt.xlabel('Ciclo de Medición')
plt.ylabel('Promedio de Valores Aleatorios')
plt.grid(True)
plt.show()
