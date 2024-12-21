import random

campo_batalha = [[0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0]]


def criar_campo_batalha():
    fortes_restantes = 3
    while fortes_restantes > 0:
        linha = random.randint(0,4)
        coluna = random.randint(0,4)
        if campo_batalha[linha][coluna] == 0:
            campo_batalha[linha][coluna] = 1
            fortes_restantes -= 1
    return campo_batalha

def exibir_matriz(matriz, revelar = False):
    for linha in matriz:
        linha_formatada = []
        for posicao in linha:
            if posicao == 1 and not revelar:
                linha_formatada.append(0)
            elif posicao == -1:
               linha_formatada.append(-1)
            else:
               linha_formatada.append(posicao)
        print(linha_formatada)



def jogar():
    campo_batalha = criar_campo_batalha()
    fortes_destruidos = 0

    while fortes_destruidos < 3:
        exibir_matriz(campo_batalha)

        linha = int(input("Escolha uma linha (0-4): "))
        coluna = int(input("Escolha uma coluna (0-4): "))

        if campo_batalha[linha][coluna] == 1:
            print("Acertou!")
            campo_batalha[linha][coluna] = -1
            fortes_destruidos += 1
        else:
            print("Errou!")
    print("Vitória! Todos os fortes foram destruídos!")
    exibir_matriz(campo_batalha, revelar=True)

jogar()