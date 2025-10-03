import os
os.system("cls")

# Função com passagem de parâmetros
# Criando uma função
def saudacao(nome,idade):
    print(f"Olá, {nome}! Bem-vindo(a)")
    print(f"Sua idade é {idade} anos.")
    print(f"Sua altura é {altura} .")
    print(f"Seu peso é {peso} kg .")

print("Solicitando dados")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))


# Chamando a função
saudacao(nome,idade,altura,peso)