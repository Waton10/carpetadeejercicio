def invertir_cadena(cadena):
    # Caso base: cadena vacía
    if not cadena:
        return cadena
    else:
        # La cadena invertida es el último carácter más la cadena invertida del resto
        return cadena[-1] + invertir_cadena(cadena[:-1])

# Ejemplo de uso
cadena_original = "Hola, mundo!"
cadena_invertida = invertir_cadena(cadena_original)

print(f"Cadena original: {cadena_original}")
print(f"Cadena invertida: {cadena_invertida}")
