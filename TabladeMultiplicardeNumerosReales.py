def tabla_de_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    print("  Factor  |  Producto")
    print("---------------------")
    for i in range(1, 11):
        producto = numero * i
        print(f"   {i:<7} |   {producto}")

try:
    numero_real = float(input("Ingrese un número real: "))
    tabla_de_multiplicar(numero_real)
except ValueError:
    print("Error: Por favor ingrese un número real válido.")
