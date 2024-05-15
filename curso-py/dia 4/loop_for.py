lista = ("Ana", "Ruben", "Meri", "Julia", "Javier")
for nombre in lista:
    print("hola " + nombre)

print("\n")
for nombre in lista:
    posicion = lista.index(nombre) + 1
    print(f"hola {nombre} estas en el puesto n. {posicion}")

print("\n")
for nombre in lista:
    if nombre.startswith("J"):
        print("hola " + nombre)

print("\n")
lista2 = 1,2,3,4,5
variable = 0
for numero in lista2:
    variable = variable + numero
    print(variable)

print("\n")
print(variable)

print("\n")
palabra = "python"
for letra in palabra:
    print(letra.upper())

print("\n")
lista3 = ([1, 2], [3, 4], [5,6])
for grupo in lista3:
    print(grupo)

print("\n")
lista3 = ([1, 2], [3, 4], [5,6])
for a,b in lista3:
    print(a)
    print(b)