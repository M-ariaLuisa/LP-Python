import os
os.system('cls')

par=0
impar=0
soma=0
soma2=0
soma3=0
quant=0
while True:
    num = int(input("Digite um número inteiro:\n"))
    if num == 0:
        break
    elif num %2==0:
        par+=1
        soma2+=num
    else:
        impar+=1
        soma3+=num
    soma+=num
    quant+=1
media2=soma2/par
media3=soma3/impar
media_total=soma/quant

print(f"""Resultado:
total de pares: {par}
total de ímpares: {impar}
soma dos pares: {soma2}
média dos pares: {media2:.2f}
soma dos ímpares: {soma3}
média dos ímpares: {media3:.2f}
soma total: {soma}
média total: {media_total:.2f}
""")