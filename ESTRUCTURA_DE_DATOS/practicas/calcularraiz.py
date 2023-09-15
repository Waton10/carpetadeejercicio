def calcular_raiz_n(numero, n):
    if numero >= 0:
        raiz_n = numero ** (1 / n)
        return raiz_n
    else:
        return "El número debe ser no negativo para calcular la raíz."

# Solicitar al usuario ingresar el número y el valor de n
try:
    numero = float(input("Ingrese un número: "))
    n = int(input("Ingrese el valor de n para la raíz: "))
    
    resultado = calcular_raiz_n(numero, n)
    
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"La raíz {n}-ésima de {numero} es: {resultado}")
except ValueError:
    print("Por favor, ingrese un número válido y un valor entero para n.")
