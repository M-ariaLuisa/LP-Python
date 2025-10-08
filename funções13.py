import os

def limpa_tela():
    os.system("cls")

def adicionar_juros(n1):
    if n1 < 100:
     return n1 + (n1 * 0.1)
    else:
        return n1 + (n1 * 0.2)

def mostrar_resultado(multiplicacao):
    print(f"O resultado é {multiplicacao:} ")

limpa_tela()
preco = float(input("Informe o valor do produto: "))
resultado = adicionar_juros(preco)
mostrar_resultado(resultado)



    










