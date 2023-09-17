# DATOS DE LOS HABITANTES DE NUESTRO HOGAR
Hogar = {'35708386':'Franco', '33063036':'Ribana'}
print(Hogar)
# LAS SENTENCIAS ANTERIORES IMPRIMEN EL DICCIONARIO DE LOS HABITANTES DE MI HOGAR

# AÑADO DATOS DE FAMILIARES QUE VISITAN Y SE HOSPEDAN EN NUESTRO HOGAR
familia = dict(Hogar)  # Crear una copia del diccionario Hogar para la familia
familia.update({
    '45678901D': 'Mirta',       # Abuela materna
    '56789012E': 'Daniel',      # Padre
    '67890123F': 'Emanuel',     # Cuñado
    '78901234G': 'Dario',       # Tío
})

# Crear el diccionario de números de teléfono
telefonos = {
    '123456789': '35708386',  # Número de Franco
    '234567890': '33063036',  # Número de Ribana
    '345678901': '45678901D',  # Número de Mirta
    '567890123': '56789012E',  # Número de Daniel
    '678901234': '67890123F',  # Número de Emanuel
    '789012345': '78901234G',  # Número de Dario
}

# Mostrar ambos diccionarios
print("Diccionario de Núcleo Familiar:")
for dni, nombre in familia.items():
    print(f"DNI: {dni}, Nombre: {nombre}")

print("\nDiccionario de Números de Teléfono:")
for telefono, dni in telefonos.items():
    print(f"Teléfono: {telefono}, DNI: {dni}")