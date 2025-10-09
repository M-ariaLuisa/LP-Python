import os
os.system("cls")

#Criando um vetor
lista_numero = []
#Definindo a quantidade de números a serem lidos
QUANTIDADE_NUMEROS = 5




for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    if numero < 0:
        lista_numero.append(0)
    else:
        lista_numero.append(numero)
    
print(f"Números digitados: {lista_numero}")