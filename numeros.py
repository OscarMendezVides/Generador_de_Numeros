import random
import os

# Generamos una lista con 1000000 números aleatorios entre -10000000 y 10000000
numbers = [random.randint(-10000000, 10000000) for i in range(1000000)]

# Obtenemos la ruta hacia el escritorio
Desktop_path = os.path.join(os.path.join(os.path.expanduser("~")), "OneDrive")

# Guardamos los números en un archivo txt sin ordenar en el escritorio
with open(os.path.join(Desktop_path, "numeros_desordenados.txt"), "w") as f:
    for number in numbers:
        f.write(str(number) + "\n")

# Guardamos los números en un archivo txt ordenados en el escritorio
numbers_sorted = sorted(numbers)
with open(os.path.join(Desktop_path, "numeros_ordenados.txt"), "w") as f:
    for number in numbers_sorted:
        f.write(str(number) + "\n")
