import os
os.system("cls")

# Definindo variávies
menor_salario = 9999
maior_salario = 0
soma_salario = 0
quantidade_familias = 0
soma_filhos = 0

while True:
    os.system("cls")
    print("""        
Código   |   Descrição
   1     | Adicionar pessoa
   2     | Sair e exibir resultados    
""")
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
            soma_filhos += filhos

             # Maior e menor salário.
            if salario < menor_salario:
             menor_salario = salario   
            if salario > maior_salario:
                maior_salario = salario
        case 2:
            if quantidade_familias == 0:
                print("Nenhuma família foi adicionada")
            else:    
                media_salarial = soma_salario / quantidade_familias
                media_filhos = soma_filhos / quantidade_familias
          
                print("\n= Exibindo resultados =")
                print(f"""
                Total de familias {quantidade_familias}
                Média de salário da população {media_salarial:.2f}
                Média do numero de filhos {media_filhos}
                Maior salário {maior_salario:.2f}
                Menor salário {menor_salario:.2f}
                """)

                input("\nPressione ENTER para fechar o programa.")
            break # Encerra o loop e o programa

        case _:
             input("Opção inválida! Pressione ENTER para tentar novamente.")
