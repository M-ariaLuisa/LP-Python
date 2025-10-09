import os
os.system('cls')

soma = 0
quant_nota = 0

while True:
    nota = float(input("Digite uma nota:\n"))
    quant_nota+=1
    soma+= nota
    resposta = input("Deseja inserir mais de uma nota?\nUse S ou N:\n")
    if resposta == "N":
        break
media = soma/quant_nota
print(f"\nMédia:{media:.2f}")