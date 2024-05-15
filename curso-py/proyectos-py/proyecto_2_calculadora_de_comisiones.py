empleado = input("Inserta tu nombre ")
ventas = input("inserta tus ventas ")
ventas = int(ventas)
comision = ventas * 13 / 100
comision = round(comision, 2)

print(f"Sr/a {empleado} su comision de este mes es de {comision}$")
