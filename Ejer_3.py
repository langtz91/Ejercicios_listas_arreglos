# Dada una lista de 10 números enteros, se requiere imprimir esos
# números en orden inverso al que fueron ingresados.

n = 10
lista = []

for i in range(0, n):
    elementos = int(input(f"Ingrese el elemento # {i+1} de la lista: "))
    lista.append(elementos)

restador = len(lista)
for i in range(0, len(lista)):
    restador -= 1
    print(lista[restador])