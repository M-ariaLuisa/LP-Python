import os
import time

# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(3) # Espera 3 segundos.
    os.system("cls")

# Função com parâmetros e com retorno.
def multiplicar(n1):
    return n1 * 100

def mostrar_resultado(multiplicacao):
    print(f"O resultado é {multiplicacao:.0f} cm")

limpa_tela()
metros = float(input("Informe a quantidade de metros: "))
resultado = multiplicar(metros)
mostrar_resultado(resultado)

    










