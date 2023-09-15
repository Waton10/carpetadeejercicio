# Función para ingresar n datos a una lista
def ingresar_datos():
    lista = []
    n = int(input("Ingrese la cantidad de datos que desea ingresar: "))
    for i in range(n):
        dato = float(input(f"Ingrese el dato {i + 1}: "))
        lista.append(dato)
    return lista

# Función para ordenar una lista de menor a mayor (usando el algoritmo de burbuja)
def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Función para calcular la sumatoria de los datos de una lista
def calcular_sumatoria(lista):
    sumatoria = 0
    for dato in lista:
        sumatoria += dato
    return sumatoria

# Función para calcular la media de los datos
def calcular_media(lista):
    sumatoria = calcular_sumatoria(lista)
    n = len(lista)
    media = sumatoria / n
    return media

# Función para calcular la mediana de una lista ordenada
def calcular_mediana(lista):
    n = len(lista)
    if n % 2 == 0:
        # Si la lista tiene un número par de elementos, se toma el promedio de los dos del medio
        medio1 = lista[n // 2 - 1]
        medio2 = lista[n // 2]
        mediana = (medio1 + medio2) / 2
    else:
        # Si la lista tiene un número impar de elementos, se toma el elemento del medio
        mediana = lista[n // 2]
    return mediana

# Función para calcular la moda de una lista
def calcular_moda(lista):
    frecuencias = {}
    for dato in lista:
        if dato in frecuencias:
            frecuencias[dato] += 1
        else:
            frecuencias[dato] = 1

    moda = []
    max_frecuencia = max(frecuencias.values())
    for dato, frecuencia in frecuencias.items():
        if frecuencia == max_frecuencia:
            moda.append(dato)

    return moda

# Función para calcular la desviación típica o estándar para datos sin agrupar
def calcular_desviacion_estandar(lista):
    media = calcular_media(lista)
    n = len(lista)
    suma_de_cuadrados = 0
    for dato in lista:
        suma_de_cuadrados += (dato - media) ** 2
    desviacion_estandar = (suma_de_cuadrados / n) ** 0.5
    return desviacion_estandar

# Main
datos = ingresar_datos()
ordenar_lista(datos)
print(f"Lista ordenada: {datos}")
print(f"Sumatoria: {calcular_sumatoria(datos)}")
print(f"Media: {calcular_media(datos)}")
print(f"Mediana: {calcular_mediana(datos)}")
print(f"Moda: {calcular_moda(datos)}")
print(f"Desviación Estándar: {calcular_desviacion_estandar(datos)}")
