import os
os.system('cls')

soma_notas= 0
print("Deseja aplicar mais de uma nota?")
print("1)- SIM")
print("2) - NÃO")
esc=int(input("Escolha uma opção (1 ou 2):\n"))

while True:
    match esc:
        case 1:
            quant_notas = int(input("Digite a quantidade de notas a serem aplicadas:\n"))
            for i in range (quant_notas):
                nota = float(input(f"Digite a {i+1}° nota:\n"))
                soma_notas = soma_notas + nota
            media = soma_notas/quant_notas
            print(f"Média: {media:.2f}")
            break
        case 2:
            nota2 = float(input("Digite o valor da nota do aluno:\n"))
            print(f"Nota:{nota2:.2f}")
            break
        case _:
            print("Opção inváliida.")
            print("Tente novamente....")
            break