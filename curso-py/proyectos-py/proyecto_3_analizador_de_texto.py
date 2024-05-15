vari1 = input("por favor inserta una frace aqui: ")
vari2 = []
vari1 = vari1.lower()

vari2.append(input("ingrese la primera letra ").lower())
vari2.append(input("ingrese la segunda letra letra ").lower())
vari2.append(input("ingrese la tercera letra ").lower())

print("\n")
print("hemos encontrado las letras que pedistes")
letra1 = vari1.count(vari2[0])
letra2 = vari1.count(vari2[1])
letra3 = vari1.count(vari2[2])
print(f"hemos encontrado la letra '{vari2 [0]}' un total de'{letra1}'")
print(f"hemos encontrado la letra '{vari2 [1]}' un total de'{letra2}'")
print(f"hemos encontrado la letra '{vari2 [2]}' un total de'{letra3}'")

print("\n")
print("palabras totales")
lista1 = vari1.split()
print(f"hemos encontrado {len(lista1)} palabras en tu frase")

print("\n")
print("Letras de Inicio y Fin")
inicio = vari1[0]
final = vari1[-1]
print(f"la letra con la cual inicia la frase es: '{inicio}' y finaliza con la letra: '{final}'")

print("\n")
print("Texto Invertido")
p4 = lista1[::-1]
lista_invertida = " ".join(p4)
print(f"si leo la frase al reves dice: {lista_invertida}")

print("\n")
print("Buscando Python en tu Frase")
p5 = ("python" in lista1)
dic = {True: "si", False: "no"}
print(f"la palabra Phyton '{dic[p5]}'se encuentra en mi frase")
