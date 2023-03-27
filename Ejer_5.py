# De una lista de números, identifique el que más se repite.

n = int(input("Ingrese longitud de la lista: "))

lista = []

for i in range(0, n):
    elemento = input(f"Ingrese el elemento # {i+1} de la lista: ")
    lista.append(elemento)

limite = 0
contador_igual_mayor = 0
posicion = 0

while len(lista) > limite:
    limite += 1 
    contador_igual = 0

    for i in range(0, len(lista)):
        if lista[posicion] == lista[i]:
            contador_igual += 1

    if contador_igual_mayor < contador_igual:
        contador_igual_mayor = contador_igual
        número_mas_repetido = lista[posicion]
        
    posicion += 1

print(f"El número más repetido es el: {número_mas_repetido}. Se repite {contador_igual_mayor} veces")
