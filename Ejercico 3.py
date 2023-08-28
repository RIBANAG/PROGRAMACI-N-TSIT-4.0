while True:
    caracter = input("Ingresa un caracter (0 para salir): ")

    if caracter == '0':
        break

    if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("VOCAL")
    else:
        print("NO VOCAL")
