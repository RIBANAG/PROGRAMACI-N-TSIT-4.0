# Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir: ¡Usted ha ganado el sorteo!
# Si el número es menor imprimir: ¡Falto un poco,seguí participando! 
# Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!

numero = int(input('Ingrese un número:'))
if numero == 10:
    print('Usted ha ganado el sorteo')
elif numero < 10:
    print('Falto un poco, seguí participando')
else:
    print('Te pasaste, seguí participando')