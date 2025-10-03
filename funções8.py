import os
os.system("cls")
def tabuada (numero):
    for i in range (0,10):
        resultado = numero*(i+1)
        print(f"{numero} x {i+1} = {resultado}")

numero = int(input("Digite um número: "))

tabuada(numero)