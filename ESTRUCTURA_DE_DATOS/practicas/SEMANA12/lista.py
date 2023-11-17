def busqueda_binaria_recursiva(lista, elemento, inicio=0, fin=None):
    # Verificar el caso base: lista vacía o elemento no encontrado
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return -1  # Elemento no encontrado

    # Calcular el índice medio
    medio = (inicio + fin) // 2

    # Verificar si el elemento está en el medio
    if lista[medio] == elemento:
        return medio  # Elemento encontrado en el índice medio

    # Si el elemento es menor que el valor medio, buscar en la mitad izquierda
    elif lista[medio] > elemento:
        return busqueda_binaria_recursiva(lista, elemento, inicio, medio - 1)

    # Si el elemento es mayor que el valor medio, buscar en la mitad derecha
    else:
        return busqueda_binaria_recursiva(lista, elemento, medio + 1, fin)

# Ejemplo de uso
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_a_buscar = 6
resultado = busqueda_binaria_recursiva(lista_ordenada, elemento_a_buscar)

if resultado != -1:
    print(f"El elemento {elemento_a_buscar} está en la posición {resultado}.")
else:
    print(f"El elemento {elemento_a_buscar} no se encuentra en la lista.")
