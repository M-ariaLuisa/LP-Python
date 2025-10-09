import os
os.system("cls")

def boletim():
    nota_1 = float(input("Digite a 1ª nota: "))
    nota_2 = float(input("Digite a 2ª nota: "))

    media = (nota_1 + nota_2) / 2

    print(f"Sua média {media:.2f}")
    return(media)


def resultado(media_aluno):

    if media_aluno < 7:
        print("Reprovado")
    else:
        print("Aprovado")

media_final = boletim()
resultado(media_final)
