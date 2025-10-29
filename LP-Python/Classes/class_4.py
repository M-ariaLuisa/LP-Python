import os
from dataclasses import dataclass
os.system

@dataclass
class Pessoa:
    nome:str
    email:str
    endereco:str

    def dados_entrega(self):
        os.system
        print(f"""Nome: {self.nome}
Endereco:{self.endereco}
""")

    def dados_email_marketing(self):
        print(f"""Nome:{self.nome}
Email:{self.email}
""")

print("Solicitando os dados da pessoa")
pessoa1=Pessoa(nome=input("Informe o seu nome:\n"),
            email=input("Informe sua email:\n"),
            endereco=input("Informe seu endereço:\n"))    
                    
                    
           
print(f"= Exibindo resultados =")
pessoa1.dados_entrega()
pessoa1.dados_email_marketing()

