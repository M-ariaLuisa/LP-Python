import os
from dataclasses import dataclass
os.system

@dataclass
class Pessoa:
    nome:str
    idade:int
    peso:float
    altura:float

pessoa1=Pessoa("Maria",23,70,1.53)

print(f"Nome:{pessoa1.nome} \nidade:{pessoa1.idade}\npeso:{pessoa1.peso}\naltura:{pessoa1.altura}")
