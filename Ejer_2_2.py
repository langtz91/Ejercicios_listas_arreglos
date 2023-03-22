# Dado un arreglo de números (numbers) y un número entero n,
# determine si n se encuentra en el arreglo. El programa debe imprimir
# True o False como corresponda.

n = int(input("Ingrese cuantos elementos tendrá la listas: "))
lista = []

for i in range(0, n):
    elemento = int(input(f"Ingrese el elemento # {i+1} de la lista: "))
    lista.append(elemento)

contador_numero = 0
numero = int(input("Ingrese un número entero: "))
for elemento in lista:
    if elemento == numero:
        contador_numero += 1

if contador_numero == 1:
    print("True")
    print(f"El número entero se encuentra {contador_numero} vez en la lista")
elif contador_numero > 1:
    print("True")
    print(f"El número entero se encuentra {contador_numero} veces en la lista")
else:
    print("False")

