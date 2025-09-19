import os
os.system('cls')

soma=0
quant=0

while True:
    num = int(input("Digite um número inteiro:\n"))
    if num < 0:
        break
    quant+=1
    soma += num
media=soma/quant
print(f"Resultado: {soma} e {media:.2f}")