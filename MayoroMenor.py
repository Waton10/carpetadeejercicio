# Solicitar al usuario ingresar dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Encontrar el número mayor y el número menor
if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

# Mostrar los resultados
print("El número mayor es:", mayor)
print("El número menor es:", menor)
