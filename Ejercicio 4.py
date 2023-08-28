suma = 0
contador = 0

while True:
    numero = float(input("Ingresa un número (0 para salir): "))
    
    if numero == 0:
        break
    
    suma += numero
    contador += 1

if contador == 0:
    print("No se ingresaron números.")
else:
    media = suma / contador
    print("Suma de los números:", suma)
    print("Media de los números:", media)
