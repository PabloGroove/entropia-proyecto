import random
import matplotlib.pyplot as plt

# Configuración inicial
moléculas = 1000
temperatura = 0  # Frío inicial (0 = sólido ordenado)
estados = []

# Simulación: aumento de temperatura
for t in range(100):
    temperatura += 1
    desorden = 0
    for _ in range(moléculas):
        # A mayor temperatura, mayor probabilidad de moverse
        if random.random() < temperatura / 100:
            desorden += 1
    estados.append(desorden / moléculas)

# Visualización
plt.plot(estados)
plt.title('Simulación de Entropía en un Sistema Natural')
plt.xlabel('Incremento de Temperatura')
plt.ylabel('Nivel de Desorden (Entropía)')
plt.show()
