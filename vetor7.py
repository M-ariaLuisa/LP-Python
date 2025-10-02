import os
os.system("cls")

lista_numeros = []

import os
os.system("cls")

#Criando um vetor
lista_numero = []
#Definindo a quantidade de números a serem lidos
QUANTIDADE_NUMEROS = 5
positivos = 0
negativos = 0
soma = 0


for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista_numero.append(numero)
    #Verificando se o número é par ou ímpar
    if numero < 0:
        negativos += 1
    else:
        positivos += 1
        soma += numero
    #Exibindo os resultados
#for i in range(QUANTIDADE_NUMEROS):
    #print(f"Número {i}: {lista_numero[i]}")

for numero in lista_numero:
    print(f"Número: {numero}")
    
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Números digitados: {lista_numero}")
print(f"Soma dos números positivos : {soma}")