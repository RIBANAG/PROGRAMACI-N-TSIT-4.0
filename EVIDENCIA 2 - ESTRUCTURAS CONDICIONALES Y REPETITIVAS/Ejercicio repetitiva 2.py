num_numeros = int(input("¿Cuántos números vas a introducir? "))
numeros_mayores = 0
numeros_menores = 0
numeros_iguales = 0

for _ in range(num_numeros):
    numero = float(input("Ingresa un número: "))
    if numero > 0:
        numeros_mayores += 1
    elif numero < 0:
        numeros_menores += 1
    else:
        numeros_iguales += 1

print("Cantidad de números mayores a 0:", numeros_mayores)
print("Cantidad de números menores a 0:", numeros_menores)
print("Cantidad de números iguales a 0:", numeros_iguales)
