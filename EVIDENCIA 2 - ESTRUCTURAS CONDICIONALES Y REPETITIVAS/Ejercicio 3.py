# Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, 
# otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
# ingresado no es ninguno de esos, imprimir otro mensaje.

dia_semana = input("Ingresa un día de la semana: ")
if dia_semana.lower() == "lunes":
    print("¡Comienza la maldita semana laboral!")
elif dia_semana.lower() == "viernes":
    print("¡Llegó el amado cierre de la semana laboral!")
elif dia_semana.lower() == "sábado" or dia_semana.lower() == "domingo":
    print("¡Es fin de semana!")
else:
    print("Ese día no corresponde a los especificados.")
