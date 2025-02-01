# bingo_python

import random

def modo():
    modo = 2
    while modo != 0 and modo != 1:
        modo = int(input("Indique o modo de jogo:\n0 - Rápido\n1 - Demorado\n"))
        print(modo)
    if modo == 0:
        quant_cartelas = 2
        linhas, colunas = 2, 3
        intervalo = [(1, 10), (11, 20), (21, 30)] 
        return quant_cartelas, linhas, colunas, intervalo
    if modo == 1:
        quant_cartelas = 4
        linhas, colunas = 3, 4
        intervalo = [(1, 10), (11, 20), (21, 30), (31, 40)]
        return quant_cartelas, linhas, colunas, intervalo
    
def criar_cartelas(quant_cartelas, linhas, colunas, intervalo):
    cartelas = []
    for utilidade0 in range(quant_cartelas):
        cartela = []
        for coluna in range(colunas):
            inicio, fim = intervalo[coluna]
            numeros_coluna = []
            while len(numeros_coluna) < linhas:
                num = random.randint(inicio, fim)
                if num not in numeros_coluna:
                    numeros_coluna.append(num)
            for linha in range(linhas):
                if len(cartela) <= linha:
                    cartela.append([])
                cartela[linha].append(numeros_coluna[linha])
        cartelas.append(cartela)
    return cartelas, quant_cartelas