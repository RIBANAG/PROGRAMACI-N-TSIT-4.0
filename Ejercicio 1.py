#Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar -1.

suma = 0
numero = 0

while numero != -1:
    numero = int(input("Ingresa un número (-1 para salir): "))
    if numero != -1:
        suma += numero

print("La sumatoria de los números ingresados es:", suma)
