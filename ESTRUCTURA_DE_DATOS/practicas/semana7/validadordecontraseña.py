class ValidadorContraseña:
    def __init__(self, longitud_minima):
        self.longitud_minima = longitud_minima

    def validar(self, contraseña):
        try:
            if len(contraseña) < self.longitud_minima:
                raise ValueError(f"La contraseña debe tener al menos {self.longitud_minima} caracteres")
            else:
                print("La contraseña es válida.")
        except ValueError as e:
            print("Error:", e)

# Ejemplo de uso
validador = ValidadorContraseña(8)  # Configurar una longitud mínima de 8 caracteres

contraseña = input("Ingresa tu contraseña: ")
validador.validar(contraseña)
