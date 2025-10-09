import os
os.system("cls")

lista_notas=[]

#Inserir notas:
for i in range(3):
    nota = int(input(f"Digite a {i+1}ª nota:"))
    lista_notas.append(nota)

    soma = sum(lista_notas)  # Soma todos os elementos da lista
    media= soma /3

    