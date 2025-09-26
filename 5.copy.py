import os
os.system('cls')

pares=0
impares=0
soma_pares=0
soma_geral=0
contador_geral=0
while True:
    num = int(input("Digite um número inteiro:\n"))
    if num > 0:
        contador_geral =+ 1
        soma_geral+=num
        break
    if num % 2 == 0:
        pares+=1
        soma_pares+=num
    else:
        impares += 1
    if num == 0:
      break
# Calculando
#if pares != 0:
    media_pares= soma_pares / pares
#else:
#    media_pares = 0
#if contador_geral ! == 0:
#    media_geral= soma_geral / contador_geral
#else:
#    media_geral = 0

#Operação ternária
media_pares = soma_pares / pares if pares != 0 else 0
media_geral = soma_geral / contador_geral if contador_geral != 0 else 0
    



print(f"""Resultado:
total de pares: {pares}
total de ímpares: {impares}
soma dos pares: {soma_pares}
média dos pares: {media_pares:.2f}
média total: {media_geral:.2f}
""")