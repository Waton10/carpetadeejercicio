# Crear un diccionario de productos y precios
productos = {
    "producto1": 10.0,
    "producto2": 15.0,
    "producto3": 20.0,
    "producto4": 25.0,
}

# Solicitar al usuario el nombre y cantidad del producto
nombre_producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

# Verificar si el producto existe en el diccionario
if nombre_producto in productos:
    precio_unitario = productos[nombre_producto]
    total_a_pagar = precio_unitario * cantidad
    print(f"Total a pagar por {cantidad} {nombre_producto}: ${total_a_pagar:.2f}")
else:
    print("El producto no se encuentra disponible.")
