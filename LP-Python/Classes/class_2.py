import os
from dataclasses import dataclass
os.system

@dataclass
class Pessoa:
    nome:str
    email:str
    telefone:str
    endereco:str

pessoa1=Pessoa(nome=input("Informe o seu nome:\n"),
                email=input("Informe seu email:\n"),
                telefone=input("Informe seu telefone:\n"),
                endereco=input("Informe seu endereço:\n"))   
                    
                
print(f"= Exibindo resultados =")
print(f"""Nome: {pessoa1.nome}
Email: {pessoa1.email}
Telefone: {pessoa1.telefone}
Endereço: {pessoa1.endereco}
""")
