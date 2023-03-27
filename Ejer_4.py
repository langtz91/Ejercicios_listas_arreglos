# Dada dos listas de caracteres, se requiere contar las diferencias entre
# ellas y mostrar dicho conteo.
# ○ Ejemplo: Si se tienen las listas [“A”, “B”, “C”] y [“A”, “E”, “H”],
# entonces el conteo sería 2 ya que hay dos diferencias.
# Nota: Las listas deben ser de igual longitud y esto debe ser validado

n = int(input("Ingrese longitud de las listas: "))

lista_1 = []
lista_2 = []
print("Lista # 1")

for i in range(0, n):
    elemento_1 = input(f"Ingrese el caracter # {i+1} de la primera lista: ")
    lista_1.append(elemento_1)

print("Lista # 2")

for i in range(0, n):
    elemento_2 = input(f"Ingrese el caracter # {i+1} de la segunda lista: ")
    lista_2.append(elemento_2)

limite = 0
contador_igual = 0
posicion = 0

while len(lista_2) > limite:
    limite += 1 

    for i in range(0, len(lista_1)):
        if lista_1[posicion] == lista_2[i]:
            contador_igual += 1

    posicion += 1
    
diferencias = len(lista_1) - contador_igual 

print(f"Las diferencias que hay entre las listas son: {diferencias}")