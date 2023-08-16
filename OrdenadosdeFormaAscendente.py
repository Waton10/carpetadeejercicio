# Pedir al usuario que ingrese 5 números
numbers = []
for i in range(5):
    number = float(input("Ingrese el número {}: ".format(i + 1)))
    numbers.append(number)

# Ordenar los números de forma ascendente (usando el algoritmo de selección)
for i in range(len(numbers)):
    min_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# Mostrar los números ordenados
print("Números ordenados de forma ascendente:")
for number in numbers:
    print(number)
