import os
os.system("cls")

Pedidos = []
soma = 0

menu= print("Menu do restaurante")
print("1- picanha- 25,00")
print("2- lasanha- 20,00")
print("3- Strogonoff- 18,00")
print("4- Bife Acebolado- 15,00")
print("5- Pão com ovo - 5,00" )

prato = int(input("Digite o número do prato desejado: "))

match prato:
    case 1:
        print("Você pediu Picanha- 25,00")
        soma += 25
    case 2:
        print("Você pediu Lasanha- 20,00")
        soma += 20
    case 3:
        print("Você pediu Strogonoff- 18,00")
        soma += 18
    case 4:
        print ("Você pediu Bife Acebolado- 15,00")
        soma += 15
    case 5:
        print("Você pediu Pão com ovo - 5,00")
        soma += 5
    case _:
        print("Opção inválida")
Pedidos.append(prato)


while True:
    mais = input("Deseja pedir mais algo? (s/n)").lower()
    if mais == "s":
      prato = int(input("Digite o número do prato desejado: "))
    match prato:
            case 1:
                print("Você pediu Picanha- 25,00")
                soma += 25
            case 2:
                print("Você pediu Lasanha- 20,00")
                soma += 20
            case 3:
                print("Você pediu Strogonoff- 18,00")
                soma += 18
            case 4:
                print ("Você pediu Bife Acebolado- 15,00")
                soma += 15
            case 5:
                print("Você pediu Pão com ovo - 5,00")
                soma += 5
            case _:
                print("Opção inválida")
    Pedidos.append(prato)
    if mais == "n":
        break



print(f"Você pediu {Pedidos}")
print(f"O total da sua conta é {soma}")
print("Fim do programa")


