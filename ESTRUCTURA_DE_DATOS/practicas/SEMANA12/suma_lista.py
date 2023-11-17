def suma_lista(lista):
    # Caso base: lista vacía
    if not lista:
        return 0
    else:
        # La suma es el primer elemento más la suma del resto de la lista
        return lista[0] + suma_lista(lista[1:])

# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5]
resultado = suma_lista(lista_numeros)

print(f"La suma de la lista {lista_numeros} es: {resultado}")
