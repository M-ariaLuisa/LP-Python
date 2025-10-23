import os
from dataclasses import dataclass
os.system

@dataclass
class Pessoa:
    nome:str
    idade:str

    def mostrar_dados(self):
        print(f"""Nome: {self.nome}
        Idade: {self.idade}
        """)

print("Solicitando os dados da pessoa")
pessoa1=Pessoa(nome=input("Informe o seu nome:\n"),
           idade=input("Informe sua idade:\n"),
            )   
pessoa2=Pessoa(nome=input("Informe o seu nome:\n"),
           idade=input("Informe sua idade:\n"),
            )   
                    
                    
                
print(f"= Exibindo resultados =")
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()
