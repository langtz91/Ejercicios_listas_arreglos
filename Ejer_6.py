# Dado un arreglo, indique si es simétrico, un arreglo es simétrico si
# siendo longitud par los números de la primera mitad son iguales al
# inverso de la otra mitad.
# ○ Ejemplo: El arreglo [1,2,3,3,2,1] es simétrico.
# En caso de que la longitud sea impar, se ignorará el elemento central
# y se seguirá la misma lógica anterior.
# ○ Ejemplo: El arreglo [3,5,7,8,7,5,3] es de longitud impar y es
# simétrico.

n = int(input("Ingrese longitud de la lista: "))

lista = []

for i in range(0, n):
    elemento = input(f"Ingrese el elemento # {i+1} de la lista: ")
    lista.append(elemento)

n = len(lista) // 2

if n % 2 != 0:
    n = (len(lista) // 2) 

restador = len(lista)
diferencias = 0

for i in range(0, n):
    restador -= 1
    if lista[i] != lista[restador]:
        diferencias += 1

if diferencias != 0:
    print(f"La lista {lista} no es simétrica")
else:
    print(f"La lista {lista} es simétrica")

