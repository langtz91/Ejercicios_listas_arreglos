# Dada dos listas (lista1 y lista2), de como resultado dos listas
# resultantes: una de la suma entre lista1 y lista2, y otra de la resta.

n1 = int(input("Ingrese cuantos elementos tendrá la primera lista: "))
lista_1 = []

for i in range(0, n1):
    elementos_1 = int(input(f"Ingrese el elemento # {i+1}: "))
    lista_1.append(elementos_1)
    
n2 = int(input("Ingrese cuantos elementos tendrá la segunda lista: "))
lista_2 = []

for i in range(0, n2):
    elementos_2 = int(input(f"Ingrese el elemento # {i+1}: "))
    lista_2.append(elementos_2)

lista_suma = []
lista_resta = []
n3 = len(lista_1)
n4 = len(lista_2)

if n3 > n4:
    n5 = n3
else:
    n5 = n4

for i in range(0, n5):
    lista_suma.append(lista_1[i] + lista_2[i])

for i in range(0, n5):
    lista_resta.append(lista_1[i] - lista_2[i])

print(f"La suma de las listas es = {lista_suma}")
print(f"La resta de las listas es = {lista_resta}")