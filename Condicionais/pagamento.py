import os
os.system("cls")

valor= float(input("Digite o valor do produto: "))

print("""
1- À vista
2- À Prazo
""")

forma_pagamento= int(input("Digite o codigo da forma de pagamento desejada: "))



match forma_pagamento:
    case 1:
        # Obtendo o valor do desconto de 10%
        print("Pagamento à vista")
        desconto= valor * 0.10
        resultado = valor - (valor * 0.10)
        print(f"{resultado:.2f}")
        print(f"""
                Valor do produto : R${valor:.2f}
                Forma de pagamento: à vista
                Valor do desconto: R${desconto:.2f}
                Total a pagar: R${resultado:.2f}
            """)
    case 2:
        print("Pagamento à prazo")
        parcelas= int(input("Digite a quantidade de parcelas:(1-6): "))
        if parcelas >= 1 and parcelas <= 6:
            valor_por_parcela= valor / parcelas
            resultado: valor
            print(f"{valor_por_parcela:.2f}")
            print(f"""
                Valor do produto : R$ {valor:.2f}
                Forma de pagamento: à prazo
                Valor por parcela: R${valor_por_parcela:.2f}
                Total a pagar: R${valor}
                """)
        else:
            print("Opção indisponível")
    case _:
        print("Opção indisponível")

        print("Pagamento efetuado")
    
    

    
