class Biblioteca:
    def __init__(self):
        self.pila_libros = []

    def prestar_libro(self, libro):
        self.pila_libros.append(libro)
        print(f"Libro '{libro}' prestado con éxito.")

    def devolver_libro(self):
        if self.pila_libros:
            libro_devuelto = self.pila_libros.pop()
            print(f"Libro '{libro_devuelto}' devuelto correctamente.")
        else:
            print("No hay libros prestados para devolver.")

    def mostrar_estado_pila(self):
        if self.pila_libros:
            print("Libros prestados actualmente:")
            for libro in reversed(self.pila_libros):
                print(f" - {libro}")
        else:
            print("La pila de libros está vacía.")

# Crear instancia de la clase Biblioteca
mi_biblioteca = Biblioteca()

# Operaciones de préstamo y devolución
mi_biblioteca.prestar_libro("Cien años de soledad")
mi_biblioteca.prestar_libro("Don Quijote de la Mancha")
mi_biblioteca.mostrar_estado_pila()

mi_biblioteca.devolver_libro()
mi_biblioteca.mostrar_estado_pila()
