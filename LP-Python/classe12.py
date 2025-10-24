import os
from dataclasses import dataclass
os.system

@dataclass
class Pessoa:
    nome:str
    idade:int
    peso:float
    altura:float

    def mostrar_dados(self):
        os.system
        print("= Dados do usuário =")
        print(f"Nome: {self.nome}")
        print(f"Idade:{self.idade}")
        print(f"Peso:{self.peso}")
        print(f"Altura:{self.altura}")


lista_pessoas = []
quant = int(input("Digite a quantidade de cadastros a serem realizados:\n"))
os.system("cls")

for i in range(quant):
    pessoa=Pessoa(nome=input("Informe o seu nome: \n"),
            idade=input("Informe sua idade: \n"),
            peso=input("Informe seu peso: \n"),
            altura= input("Informe sua altura: "))    
    lista_pessoas.append(pessoa)
                           
print(f"= Exibindo resultados =")
for pessoa in lista_pessoas:
    pessoa.mostrar_dados()


