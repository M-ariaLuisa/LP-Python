import os
os.system("cls")

# texto que desejo salvar.
texto = input(" Informe seu nome: ")

#Definir nome do arquivo para salvar.
nome_arquivo = "exemplo.txt"

# Comandos para salvar.
with open(nome_arquivo, "a") as meu_arquivo:
     meu_arquivo.write(f"{texto}\n")
     print("Salvo com sucesso")