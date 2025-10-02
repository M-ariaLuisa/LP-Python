import os
os.system("cls")

#Criando um vetor
lista_numero = []
#Definindo a quantidade de números a serem lidos
QUANTIDADE_NUMEROS = 6
pares = 0
impares = 0


for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista_numero.append(numero)
    #Verificando se o número é par ou ímpar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    #Exibindo os resultados
#for i in range(QUANTIDADE_NUMEROS):
    #print(f"Número {i}: {lista_numero[i]}")

for numero in lista_numero:
    print(f"Número: {numero}")
    
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Números digitados: {lista_numero}")