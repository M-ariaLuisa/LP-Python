import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: str

@dataclass
class Cliente:
    nome: str
    endereco: Endereco

    def mostrar_dados(self):
        print(f"Nome: {cliente1.nome}")
        print(f"Endereco: {cliente1.endereco.logradouro}")
        print(f"Número: {cliente1.endereco.numero}")

cliente1=  Cliente(nome="Marta",
                   endereco=Endereco(logradouro="Rua A", numero=23))

print("Mostrar dados do cliente")
cliente1.mostrar_dados

