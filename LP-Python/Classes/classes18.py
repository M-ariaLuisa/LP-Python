import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

QUANTIDADE_LIVROS = 3  
catalogo_livros = []

print("Solicitando dados do aluno. ")
for i in range(QUANTIDADE_LIVROS):
    livro = Livro(
        nome= input("Informe o nome do livro: "),
        autor=str(input("Informe o nome do autor: ")),
        categoria=(input("Informe a categforia: ")),
        preco=float(input("Informe o valor do livro: "))
    )
    catalogo_livros.append(livro)

print()
print("Salvando dados.")
arquivo = "dados.livro.txt"

with open(arquivo, "a") as arquivo_catalogo_livros:
    for livro in catalogo_livros:
        arquivo_catalogo_livros.write(f"{livro.nome}, {livro.autor}, {livro.categoria}, {livro.preco}\n")
    print("Salvo com sucesso!")
