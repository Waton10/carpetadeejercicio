def contar_vocales(frase):
    # Inicializar un diccionario para almacenar el recuento de vocales
    recuento_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Convertir la frase a minúsculas para hacer el conteo no sensible a mayúsculas
    frase = frase.lower()

    # Iterar a través de los caracteres en la frase
    for char in frase:
        if char in recuento_vocales:
            recuento_vocales[char] += 1

    return recuento_vocales

# Solicitar al usuario que ingrese una frase
frase = input("Ingrese una frase: ")

# Calcular el recuento de vocales usando la función contar_vocales
recuento = contar_vocales(frase)

# Imprimir el recuento de cada vocal
for vocal, cantidad in recuento.items():
    print(f"La vocal '{vocal}' aparece {cantidad} veces en la frase.")
