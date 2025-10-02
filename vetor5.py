import os
os.system("cls")

lista_numero = []
QUANTIDADE_NUMEROS = 6
pares = 0
impares = 0


for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista_numero.append(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
i

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
