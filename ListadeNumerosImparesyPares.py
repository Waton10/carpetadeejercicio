# Crear la lista con la serie de números
numeros = [1, 4, 6, 7, 8, 10, 13, 2, 9, 28, 9, 10, 7, 3, 8]

# Inicializar listas para almacenar los números pares e impares
pares = []
impares = []

# Clasificar los números en pares e impares
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostrar la salida en el formato deseado
print("Números Pares:")
for num in pares:
    print(num, end=' ')

print("\nNúmeros Impares:")
for num in impares:
    print(num, end=' ')
