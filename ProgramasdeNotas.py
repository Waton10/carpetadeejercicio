# Función para calcular el promedio de una lista de notas
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Número de estudiantes a ingresar
n = int(input("Ingrese el número de estudiantes: "))

# Crear un diccionario vacío para almacenar los datos de los estudiantes
estudiantes = {}

# Ingresar los datos de los estudiantes
for i in range(n):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j + 1} del estudiante {nombre}: "))
        notas.append(nota)
    estudiantes[nombre] = notas

# Calcular el promedio de cada estudiante y agregarlo al diccionario
for nombre, notas in estudiantes.items():
    promedio = calcular_promedio(notas)
    estudiantes[nombre].append(promedio)

# Mostrar los datos en formato de tabla
print("\nDatos de los estudiantes:")
print("{:<15} {:<10} {:<10} {:<10} {:<10}".format("Nombre", "Nota 1", "Nota 2", "Nota 3", "Promedio"))
for nombre, notas in estudiantes.items():
    print("{:<15} {:<10} {:<10} {:<10} {:<10.2f}".format(nombre, *notas))
