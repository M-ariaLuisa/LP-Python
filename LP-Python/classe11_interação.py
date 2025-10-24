import os
from dataclasses import dataclass

os.system("cls")
    
@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str

class Cliente:
    nome: str
    email: str
    endereco1: Endereco

    def mostrar_dados(self):
        print("== Dados do cliente ==")
        print(f"Nome:{self.nome}")
        print(f"Email: {self.email}")
        print(f"Endereço:{self.endereco1.logradouro}")
        print(f"Número:{self.endereco1.numero}")
        print(f"Cidade: {self.endereco1.cidade}")

 #Vetor.
lista_de_clientes = []

for i in range(1):
    cliente1 = Cliente(nome=input("Digite seu nome: "),
                        email=input("Digite seu email: "),
                        endereco1=Endereco(logradouro=input("Digite o logradouro: "),
                                            numero= int(input("Informe o número: ")), 
                                            cidade=input("Informe a cidade: ")))
    lista_de_clientes.append(cliente1)
    os.system("cls")

cliente1.mostrar_dados()
        

