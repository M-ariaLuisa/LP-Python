import os
os.system("cls")

primeiro_numero= int(input("Digite o primeiro número "))
segundo_numero= int(input("Digite o segundo número "))
operacao= (input("Digite o caractere da operação desejada: + - * / "))

match operacao:
    case "+":
        resultado= primeiro_numero + segundo_numero
        print(f"O resultado da sua operação é {resultado}")
    case "-":
        resultado= primeiro_numero - segundo_numero
        print(f"O resultado da sua operação é {resultado}") 
    case "*":
        resultado= primeiro_numero * segundo_numero
        print(f"O resultado da sua operação é {resultado}")
    case "/":
        resultado= primeiro_numero / segundo_numero
        print(f"O resultado da sua operação é {resultado}")       

    case _:
        print("Opção invalida")