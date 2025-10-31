import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

    def exibir_detalhes(self):
        print(f"Titulo: {self.titulo}")
        print(f"Ano de publicação: {self.ano}")
        print(f"Autor: {self.autor.nome}")

livro1= Livro(titulo=input("Informe o titulo: "),
                ano=input("Informe o ano: "), 
                autor=Autor(input("Informe o nome do autor: "),
                 biografia=input("Informe a biografia: ") )
                )


print(f"= Exibindo resultados =")
livro1.exibir_detalhes()
