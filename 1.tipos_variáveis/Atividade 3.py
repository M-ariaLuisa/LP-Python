import os
os.system("cls")

idade = int(input("Digite sua idade "))

if idade < 16 :
    print ("Não pode votar ")

elif idade >= 18 and idade <65:
    print ("Voto obrigatório")

elif idade >= 16:
    print ("Voto opcional")

elif idade >= 65:
    print("Voto não obrigatório")








