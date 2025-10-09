import os
os.system("cls")

# Definindo variávies
menor_salario = 9999
maior_salario = 0
soma_salario = 0
quantidade_familias = 0
quantidade_filhos = 0
soma_filhos = 0

while True:
    os.system("cls")
    print(""        
Código   |   Descrição
   1     | Adicionar pessoa
   2     | Sair e exibir resultados    
"")
    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            # Solicitando dados.
           
            salario = float(input("Digite o valor salário: "))
            filhos = int(input("Informe a quantidade de filhos: "))

               # Média de salários.
            quantidade_familias += 1
            soma_salario += salario

             # Média de filhos
            quantidade_filhos += 1
            soma_filhos += filhos

             # Maior e menor salário.
            if salario < menor_salario:
             menor_salario = salario   
            
        case 2:
         media_salarial = soma_salario / quantidade_familias
            if menor_salario == 9999:
                menor_salario = 0
               
            print("\n= Exibindo resultados =")
           
    
