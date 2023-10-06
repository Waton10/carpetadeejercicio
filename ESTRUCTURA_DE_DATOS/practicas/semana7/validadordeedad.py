class ValidadorDeEdad:
    def validar(self, edad_str):
        try:
            edad = int(edad_str)
            if edad < 0:
                raise ValueError("La edad no puede ser un número negativo")
            return True, edad
        except ValueError:
            return False, None

# Ejemplo de uso
validador = ValidadorDeEdad()

while True:
    edad_str = input("Ingresa tu edad: ")

    es_valido, edad = validador.validar(edad_str)

    if es_valido:
        print("Edad válida:", edad)
        break
    else:
        print("Edad no válida. Ingresa un número entero válido.")
