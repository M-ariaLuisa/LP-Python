import os
os.system("cls")

import os
os.system("cls")

lista_numeros = []

for i in range(5):
    numero = int(input(f"Digite a {i+1}ª número:"))
    lista_numeros.append(numero)

for i in range(5):
    print(f"Números {i+1}: {lista_numeros[i]}")
print(f"Maior número: {max(lista_numeros)}")
print(f"Menor número: {min(lista_numeros)}")

