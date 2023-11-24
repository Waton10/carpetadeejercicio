from collections import deque

class Banco:
    def __init__(self):
        self.cola_clientes = deque()

    def llegada_cliente(self, cliente):
        self.cola_clientes.append(cliente)
        print(f"Cliente {cliente} llegó y se unió a la cola.")

    def atender_cliente(self):
        if self.cola_clientes:
            cliente_atendido = self.cola_clientes.popleft()
            print(f"Atendiendo al cliente {cliente_atendido}.")
        else:
            print("No hay clientes en la cola.")

    def mostrar_estado_cola(self):
        if self.cola_clientes:
            print("Clientes en la cola:")
            for cliente in self.cola_clientes:
                print(f" - {cliente}")
        else:
            print("La cola de clientes está vacía.")

# Crear instancia de la clase Banco
mi_banco = Banco()

# Simulación de atención de clientes
mi_banco.llegada_cliente("Cliente A")
mi_banco.llegada_cliente("Cliente B")
mi_banco.mostrar_estado_cola()

mi_banco.atender_cliente()
mi_banco.mostrar_estado_cola()

mi_banco.atender_cliente()
mi_banco.mostrar_estado_cola()
