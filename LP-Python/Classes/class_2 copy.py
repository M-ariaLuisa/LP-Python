import os
from dataclasses import dataclass
os.system

@dataclass
class Pessoa:
    nome:str
    email:str
    telefone:str
    endereco:str

    def mostrar_dados(self):
        print(f"""Nome: {self.nome}
        Email: {self.email}
        Telefone: {self.telefone}
        Endereço: {self.endereco}""")

print("Solicitando os dados da pessoa")
pessoa1=Pessoa(nome=input("Informe o seu nome:\n"),
            email=input("Informe seu email:\n"),
            telefone=input("Informe seu telefone:\n"),
            endereco=input("Informe seu endereço:\n"))   
                    
                
print(f"= Exibindo resultados =")
pessoa1.mostrar_dados()