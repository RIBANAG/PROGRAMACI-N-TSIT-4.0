# Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir: ¡Usted ha ganado el sorteo!
numero = int(input('Ingrese un número:'))
if numero == 10:
    print('Usted ha ganado el sorteo')
else:
    print('No ha ganado el sorteo')