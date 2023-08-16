def metros_a_kilometros(metros):
    kilometros = metros / 1000
    return kilometros

cantidad_metros = float(input("Ingrese una cantidad en metros: "))
cantidad_kilometros = metros_a_kilometros(cantidad_metros)

print(f"{cantidad_metros} metros son equivalentes a {cantidad_kilometros} kilómetros")
