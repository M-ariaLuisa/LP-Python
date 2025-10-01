import os
os.system("cls")

#Criando um vetor (lista):
lista_notas = []

#Inserir notas:
for i in range(3):
    nota = int(input(f"Digite a {i+1}ª nota:"))
    lista_notas.append(nota)
    #soma += nota
    soma = sum(lista_notas)  # Soma todos os elementos da lista

#Mostrar notas:
#print(f"Nota: {lista_notas}")
#print(f"Nota: {lista_notas[0]}")


for i in range(3):
    print(f"Nota {i+1}: {lista_notas[i]}")
print(f"Soma: {soma}")


print("FIM")