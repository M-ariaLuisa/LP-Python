import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    telefone: int

QUANTIDADE_ALUNOS = 2
lista_alunos = []

print("Solicitando dados do aluno. ")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome= input("Digite o nome do aluno: "),
        idade=int(input("Informe a idade: ")),
        email=(input("Informe o email: ")),
        telefone=int(input("Informe o telefone: "))
    )
    lista_alunos.append(aluno)

print()
print("Salvando dados.")
arquivo = "dados.aluno.txt"

with open(arquivo, "a") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}, {aluno.email}, {aluno.telefone}\n")
    print("Salvo com sucesso!")

