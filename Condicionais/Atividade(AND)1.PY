import os
os.system("cls")

login_certo = "Maria"
senha_certa= "123456"

login= str(input("Digite o seu login "))
senha= str(input("Digite a sua senha "))

if login== login_certo and senha== senha_certa:
    print("Bem vindo")
else:
    print("Login ou senhas inválidos")

