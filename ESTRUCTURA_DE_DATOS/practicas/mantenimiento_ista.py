# Función para agregar un elemento a la lista
def agregar_elemento(lista, elemento):
    lista.append(elemento)
    print(f"Elemento '{elemento}' agregado correctamente.")

# Función para modificar un elemento en la lista
def modificar_elemento(lista, indice, nuevo_elemento):
    if indice >= 0 and indice < len(lista):
        lista[indice] = nuevo_elemento
        print(f"Elemento en el índice {indice} modificado a '{nuevo_elemento}'.")
    else:
        print("Índice fuera de rango. No se pudo modificar el elemento.")

# Función para eliminar un elemento de la lista
def eliminar_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
        print(f"Elemento '{elemento}' eliminado correctamente.")
    else:
        print(f"Elemento '{elemento}' no encontrado en la lista. No se pudo eliminar.")

# Lista de ejemplo
mi_lista = ["Manzana", "Banana", "Cereza", "Dátil"]

while True:
    print("\nMENU:")
    print("1. Agregar elemento")
    print("2. Modificar elemento")
    print("3. Eliminar elemento")
    print("4. Mostrar lista")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1/2/3/4/5): ")
    
    if opcion == "1":
        elemento = input("Ingrese el elemento que desea agregar: ")
        agregar_elemento(mi_lista, elemento)
    elif opcion == "2":
        indice = int(input("Ingrese el índice del elemento que desea modificar: "))
        nuevo_elemento = input("Ingrese el nuevo elemento: ")
        modificar_elemento(mi_lista, indice, nuevo_elemento)
    elif opcion == "3":
        elemento = input("Ingrese el elemento que desea eliminar: ")
        eliminar_elemento(mi_lista, elemento)
    elif opcion == "4":
        print("Lista actual:")
        for i, elemento in enumerate(mi_lista):
            print(f"{i}. {elemento}")
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
