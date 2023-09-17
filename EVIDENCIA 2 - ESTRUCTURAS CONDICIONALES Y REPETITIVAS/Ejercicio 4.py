#Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”.

letra = input("Ingresa una letra: ")

if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u':
    print("¡Es una vocal!")
else:
    print("No es una vocal.")
