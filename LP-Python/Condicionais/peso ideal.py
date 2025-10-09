import os
os.system("cls")

genero= str(input("Identifique o seu genero com a inicial dele: "))
altura= float(input("Digite a sua altura: "))

match genero:
    case "M":
        peso_ideal= (72.7 * altura- 58)
        print(f"Seu peso ideal é {peso_ideal:.2f}")
    case "F":
        peso_ideal=(62.1 * altura - 44.7)
        print(f" Seu peso ideal é {peso_ideal:.2f}")
    case _:
        print("Opção indisponível")
        