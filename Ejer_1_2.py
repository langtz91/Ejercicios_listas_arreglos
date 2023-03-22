# Dada dos listas (lista1 y lista2), de como resultado dos listas
# resultantes: una de la suma entre lista1 y lista2, y otra de la resta.

def suma_y_resta_listas(lista_1, lista_2):
    lista_suma = []
    lista_resta = []

    for i in range(0, n):
        lista_suma.append(lista_1[i] + lista_2[i])

    for i in range(0, n):
        lista_resta.append(lista_1[i] - lista_2[i])

    return lista_suma, lista_resta

 
n = int(input("Ingrese cuantos elementos tendrán las listas: "))
lista_1 = []
print("Lista # 1")

for i in range(0, n):
    elementos_1 = int(input(f"Ingrese el elemento # {i+1} de la primera lista: "))
    lista_1.append(elementos_1)
    
lista_2 = []

print("Lista # 2")

for i in range(0, n):
    elementos_2 = int(input(f"Ingrese el elemento # {i+1} de la segunda lista: "))
    lista_2.append(elementos_2)

total_listas = suma_y_resta_listas(lista_1, lista_2)
print(f"La suma y resta de las listas correspondientemente es = {total_listas}")
