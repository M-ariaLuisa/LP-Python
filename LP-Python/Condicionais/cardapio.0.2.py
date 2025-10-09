import os
os.system

print(""" 
Código \t Prato \t\t Valor
    1\t Picanha \t R$ 25,00
    2\t Lasanha \t R$ 20,00
    3\t Strogonoff \t R$ 18,00
    4\t Bife Acebolado  R$ 15,00
    5\t Pão com ovo \t R$ 5,00
""")

prato= int(input("Qual prato deseja:(1 2 3 4 5) "))


match prato:
    case 1:
        print("o prato escolhido é Picanha- 25,00")
    case 2:
        print("o prato escolhido é Lasanha- 20,00")     
    case 3:
        print("o prato escolhido é Strogonoff- 18,00")
    case 4: 
        print("o prato escolhido é Bife Acebolado- 15,00")
    case 5:
        print("o prato escolhido é Pão com ovo - 5,00")
    case _:
        print("opção inválida")