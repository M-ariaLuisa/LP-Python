import os
os.system("cls")

a= str(input("Digite o nome do aluno(a) "))
n1= int(input("Digite a primeira nota "))
n2= int(input("Digite a segunda nota "))

m= (n1 + n2) / 2

if m >= 9:
    print("A")   
    print("Aprovado")

elif m >= 7.5 and m < 9:
    print ("B")
    print("Aprovado")

elif m >= 6  and  m < 7.5:  
    print ("C")
    print("Aprovado")

elif m >= 4  and m  < 6:
    print ("D")
    print("Reprovado")

else:
    print ("E")
    print("Reprovado")

