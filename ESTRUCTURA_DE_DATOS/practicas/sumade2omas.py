# Función que calcula la suma de números indeterminados
def suma(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

# Solicitar al usuario ingresar números hasta que desee terminar
numeros = []
while True:
    try:
        numero = float(input("Ingrese un número (o cualquier letra para terminar): "))
        numeros.append(numero)
    except ValueError:
        break

# Llamar a la función suma con los números ingresados
resultado_suma = suma(*numeros)

# Mostrar el resultado
print(f"La suma de los números ingresados es: {resultado_suma}")
