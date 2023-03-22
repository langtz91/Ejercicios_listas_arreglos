# Dado un arreglo de números (numbers) y un número entero n,
# determine si n se encuentra en el arreglo. El programa debe imprimir
# True o False como corresponda.

n = int(input("Ingrese cuantos elementos tendrá la listas: "))
lista = []

for i in range(0, n):
    elemento = int(input(f"Ingrese el elemento # {i+1} de la lista: "))
    lista.append(elemento)

numero = int(input("Ingrese un número entero: "))
for elemento in lista:
    if elemento == numero:
        print("True")
        exit()

print("False")