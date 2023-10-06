class Divisor:
    def dividir(self, numerador, denominador):
        try:
            resultado = numerador / denominador
            return resultado
        except ZeroDivisionError:
            raise ValueError("No se puede dividir por cero")

# Ejemplo de uso
divisor = Divisor()

try:
    numerador = 10
    denominador = 0  # Intentar dividir por cero
    resultado = divisor.dividir(numerador, denominador)
    print(f"Resultado de la división: {resultado}")
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Otro error:", e)
