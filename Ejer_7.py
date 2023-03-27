# Dada un alista de números enteros, determine si esta tiene elementos duplicados. El programa debe decir:
# La lista contiene elementos duplicados
# o La lista no contiene elementos duplicados

n = int(input("Ingrese longitud de la lista: "))

lista = []

for i in range(0, n):
    elemento = input(f"Ingrese el elemento # {i+1} de la lista: ")
    lista.append(elemento)

limite = 0
posicion = 0

while len(lista) > limite:
    limite += 1 
    contador_igual = 0

    for i in range(0, len(lista)):
        if lista[posicion] == lista[i]:
            contador_igual += 1
    
    if contador_igual > 1:
        print( f"La lista {lista} contiene elementos duplicados")
        break

    posicion += 1

if contador_igual == 1:
        print( f"La lista {lista} no contiene elementos duplicados")

    

