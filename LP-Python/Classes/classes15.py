import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Aluno:
    idade: int

Quantidade_Alunos = 2
lista_alunos = []

print("Solicitando dados do aluno. ")
for i in range(Quantidade_Alunos):
    aluno= Aluno(
            nome= input("Digite seu nome: ")
    )