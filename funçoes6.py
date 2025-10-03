import os
os.system("cls")
# Função com passagem de parâmetros
# Criando uma função para verificar se é par ou impar
def teste(numero):
    if numero % 2 == 0:
        print ("Par")    
    else:
        print ("Impar")
numero = int(input("Digite um múmero: "))
teste(numero)
        

