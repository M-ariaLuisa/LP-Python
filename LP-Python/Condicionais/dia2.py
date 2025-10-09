import os
os.system("cls")

dia= int(input("Digite o número que representa o dia da semana: "))

match dia:
    case 1:
        print("Domingo")
        print("Fim de semana")
    case 2:
        print("Segunda-feira")
        print("Dia útil")
    case 3:
         print("Terça-feira")
         print("Dia útil")
    case 4:
        print("Quarta-feira")
        print("Dia útil")
    case 5:
        print("Quinta-feira")
        print("Dia útil")
    case 6:
        print("Sexta-feira")
        print("Dia util")
    case 7: 
        print("Sábado")
        print("Fim de semana")
    case _:
        print("Opção inválida")