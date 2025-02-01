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

def mostrar_cartela(jogadores, cartelas):
    for i in range(len(cartelas)):
        print(f"\n{jogadores[i]}")
        for linha in cartelas[i]:
            for num in linha:
                print(f"{num:02}", end=" ")
            print()

def ajustar_cartelas(cartelas, num_cartelas, linhas, colunas):
    cartelas_certinhas = []
    for cartela in range(num_cartelas):
        nova_cartela = []
        for linha in range(linhas):
            nova_cartela.append([])
            for coluna in range(colunas):
                nova_cartela[linha].append(cartelas[cartela][linha][coluna])
        cartelas_certinhas.append(nova_cartela)
    return cartelas_certinhas

def sorteio_dezenas(intervalos):
    all_dezenas = []
    for i in range(len(intervalos)):
        inicio, fim = intervalos[i]
        for num in range(inicio, fim+1):
            all_dezenas.append(num)
    sorteadas = [] 
    contador = 0
    while contador < len(all_dezenas):
        num = all_dezenas[random.randint(0, len(all_dezenas)-1)]
        repetidos = 0
        for indice in range(contador):
            if sorteadas[indice] == num:
                repetidos = 1
        if repetidos == 0:
            sorteadas.append(num) 
            contador += 1
    return sorteadas

def alinhar_cartelas(cartelas, jogadores, sorteadas):
    for i in range(len(cartelas)):
        print(f"\nJogador {jogadores[i]}:")
        for linha in cartelas[i]:
            for num in linha:
                if num in sorteadas:
                    print(f"({num:02})", end=" ")  
                else:
                    print(f" {num:02} ", end=" ")  
            print()

def verificar_vencedor(cartela, sorteadas):
    for linha in cartela:
        for num in linha:
            if num not in sorteadas:
                return False
    return True

def jogar():
    # TESTE
    num_cartelas, linhas, colunas, intervalos = modo()
    jogadores = []
    for i in range(1, num_cartelas+1):
        jogadores.append(i)
    cartelas, utilidade0 = criar_cartelas(num_cartelas, linhas, colunas, intervalos)  
    cartelas = ajustar_cartelas(cartelas, num_cartelas, linhas, colunas)
    alinhar_cartelas(cartelas, jogadores, [])
    todas_dezenas = sorteio_dezenas(intervalos)
    sorteadas = []
    sorteadas_len = 0
    vencedores = []
    for utilidade0 in range(num_cartelas):
        vencedores.append(0)
    while True:
        input("\nDigite ENTER para continuar ")
        n = todas_dezenas[sorteadas_len]
        sorteadas.append(n)
        sorteadas_len += 1
        sorteadas.sort()
        print(f"=> Última dezena sorteada: {n}")
        print(f"Dezenas sorteadas até o momento:", end=" ")
        for i in range(sorteadas_len):
            print(sorteadas[i], end=" ")
        alinhar_cartelas(cartelas, jogadores, sorteadas)
        for i in range(num_cartelas):
            if vencedores[i] == 0:
                if verificar_vencedor(cartelas[i], sorteadas):
                    vencedores[i] = 1
                    print(f"\nJogador {jogadores[i]} é o ganhador!")
        if sum(vencedores) > 0:
            input("\nClique ENTER para sair da tela. ")
            break

jogar()