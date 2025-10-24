import os
from dataclasses import dataclass
os.system

@dataclass
class Pessoa:
    nome:str
    cpf:str
    telefone:str

    def mostrar_dados(self):
        print("= Dados do usuário =")
        print(f"Nome:{self.nome}")
        print(f"CPF:{self.cpf}")
        print(f"Telefone:{self.telefone}")

    def dados_sms_marketing(self):
        print("= Telefone do usuário =")
        print(f"Telefone:{self.telefone}")

print("Solicitando os dados da pessoa")
lista_pessoas = []

for i in range(3):
    pessoa=Pessoa(nome=input("Informe o seu nome:\n"),
           cpf=input("Informe seu cpf:\n"),
            telefone=input("Informe seu telefone:\n"))    
    lista_pessoas.append(pessoa)
    os.system("cls")
           
print(f"= Exibindo dados =")
for pessoa in lista_pessoas:
    pessoa.mostrar_dados()

print(f"= Somente telefones =")
for pessoa in lista_pessoas:
    pessoa.dados_sms_marketing()