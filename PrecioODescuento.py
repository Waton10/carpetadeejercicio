def calcular_descuento(precio, cantidad):
    if cantidad >= 5 and cantidad <= 10:
        descuento = 0.05
    elif cantidad >= 11 and cantidad <= 20:
        descuento = 0.1
    elif cantidad > 20:
        descuento = 0.15
    else:
        descuento = 0  # No se aplica descuento si la cantidad es menor que 5

    total_descuento = precio * descuento
    precio_con_descuento = precio - total_descuento
    return precio_con_descuento, total_descuento

# Solicitar al usuario la cantidad de productos y sus detalles
n = int(input("Ingrese la cantidad de productos: "))
productos = []

for i in range(n):
    precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    cantidad = int(input(f"Ingrese la cantidad de producto {i + 1} comprada: "))
    productos.append((precio, cantidad))

# Calcular el total a pagar y mostrar la salida
print("\nResumen de Compra:")
total_a_pagar = 0

for i, (precio, cantidad) in enumerate(productos):
    precio_con_descuento, descuento = calcular_descuento(precio, cantidad)
    total_a_pagar += precio_con_descuento
    print(f"Producto {i + 1}: Cantidad: {cantidad}, Total con Descuento: ${precio_con_descuento:.2f}, Descuento: ${descuento:.2f}")

print("\nTotal a Pagar: ${:.2f}".format(total_a_pagar))
