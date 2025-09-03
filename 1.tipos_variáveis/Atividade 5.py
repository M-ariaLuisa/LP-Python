import os
os.system("cls")


qntd = int(input("Digite a quantidade de maçãs desejadas "))

if qntd >= 12: 
    total1= (1.00 * qntd)
    print(f"O valor é {total1:.2f}" )
    

else:
    total2=  (1.30 * qntd)
    print(f"O valor é {total2:.2f}")
