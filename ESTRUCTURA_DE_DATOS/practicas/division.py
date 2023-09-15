def division_segura(dividendo, divisor):
    if divisor == 0:
        return "La división entre cero no está definida"
    else:
        resultado = dividendo / divisor
        return resultado

# Solicitar al usuario ingresar el dividendo y el divisor
try:
    dividendo = float(input("Ingrese el dividendo: "))
    divisor = float(input("Ingrese el divisor: "))
    
    resultado_division = division_segura(dividendo, divisor)
    
    print(f"Resultado de la división: {resultado_division}")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
