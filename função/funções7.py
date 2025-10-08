import os
os.system("cls")
# Função com passagem de parâmetros
# Criando uma função para verificar se é negativo ou positivo
def negativo_ou_positivo(numero):
    if numero < 0:
        print ("Negativo")    
    else:
        print ("Positivo")

numero = int(input("Digite um múmero: "))
negativo_ou_positivo(numero)