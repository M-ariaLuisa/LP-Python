import os
os.system("cls")

menu= print("Menu do restaurante")
print("1- picanha- 25,00")
print("2- lasanha- 20,00")
print("3- Strogonoff- 18,00")
print("4- Bife Acebolado- 15,00")
print("5- Pão com ovo - 5,00" )

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
