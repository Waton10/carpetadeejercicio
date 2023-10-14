school = {
    "clase1": [
        {
            "nombre": "Juan",
            "edad": 15,
            "calificaciones": [90, 85, 88]
        },
        {
            "nombre": "Ana",
            "edad": 16,
            "calificaciones": [92, 89, 94]
        }
    ],
    "clase2": [
        {
            "nombre": "Luis",
            "edad": 14,
            "calificaciones": [87, 78, 91]
        },
        {
            "nombre": "María",
            "edad": 15,
            "calificaciones": [95, 96, 93]
        }
    ]
}

# Recorrer y manipular la estructura anidada
for clase, estudiantes in school.items():
    print(f"Clase: {clase}")
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print("Calificaciones:")
        for calificacion in estudiante['calificaciones']:
            print(f"- {calificacion}")

# Actualizar una calificación
school["clase1"][0]["calificaciones"][0] = 94

# Agregar un nuevo estudiante a una clase
nuevo_estudiante = {
    "nombre": "Pedro",
    "edad": 16,
    "calificaciones": [88, 90, 86]
}
school["clase2"].append(nuevo_estudiante)

# Mostrar la estructura actualizada
print("Estructura actualizada:")
for clase, estudiantes in school.items():
    print(f"Clase: {clase}")
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print("Calificaciones:")
        for calificacion in estudiante['calificaciones']:
            print(f"- {calificacion}")
