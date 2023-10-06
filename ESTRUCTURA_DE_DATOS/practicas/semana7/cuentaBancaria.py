class CuentaBancaria:
    def __init__(self, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.saldo = saldo_inicial

    def retirar(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad a retirar no puede ser negativa")

        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo en la cuenta para retirar esa cantidad")

        self.saldo -= cantidad

    def consultar_saldo(self):
        return self.saldo

# Ejemplo de uso
try:
    cuenta = CuentaBancaria(1000)  # Crear una cuenta con saldo inicial de 1000
    print("Saldo actual:", cuenta.consultar_saldo())

    cantidad_a_retirar = 500
    cuenta.retirar(cantidad_a_retirar)
    print(f"Retirado {cantidad_a_retirar} pesos. Saldo restante:", cuenta.consultar_saldo())

    cantidad_a_retirar = 800  # Intentar retirar más dinero del que hay en la cuenta
    cuenta.retirar(cantidad_a_retirar)
    print(f"Retirado {cantidad_a_retirar} pesos. Saldo restante:", cuenta.consultar_saldo())

except ValueError as e:
    print("Error:", e)
