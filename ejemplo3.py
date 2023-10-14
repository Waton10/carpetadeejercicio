# Ejemplo de una lista de diccionarios de tuplas
lista_anidada = [
    {'nombre': 'Juan', 'puntuaciones': [(10, 'Matemáticas'), (8, 'Ciencias')]},
    {'nombre': 'María', 'puntuaciones': [(9, 'Matemáticas'), (7, 'Ciencias')]}
]

# Acceso a elementos en la estructura de datos
puntuacion_juan_mate = lista_anidada[0]['puntuaciones'][0]  # Tupla (10, 'Matemáticas')
nombre_maria = lista_anidada[1]['nombre']  # Nombre 'María'
