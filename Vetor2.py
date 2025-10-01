import os
os.system("cls")

lista_notas = []

for i in range(3):
    nota = int(input(f"Digite a {i+1}ª nota:"))
    lista_notas.append(nota)
soma = sum(lista_notas)
media = soma / len(lista_notas)

#Mostrar situação do aluno:

if media >= 7:
     print(f"Aluno aprovado com média {media}")

elif media >=5:
    print(f"Aluno em recuperação com média {media}")
else:
    print(f"Aluno reprovado com média {media}")