import os
os.system("cls")

# Função com passagem de parâmetros
# Criando uma função
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo(a)")

nome = input("Digite seu nome: ")

# Chamando a função
saudacao(nome)