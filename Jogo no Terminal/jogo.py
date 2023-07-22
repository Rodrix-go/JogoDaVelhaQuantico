# Importando funções
# teste git
from func import *
import time
print('Rodando')
nomes = ["X", "O"]
simb = ["X", "O"]
# nomes[1] = input("Digite o nome do jogador X: ")
# nomes[0] = input("Digite o nome do jogador O: ")

nomes[1] = "Rodrigo"
nomes[0] = "Ana"

# Começo do jogo
vez = False  # VEZ == TRUE -> X | VEZ == FALSE -> O
num_jogada = 0  # Numero da jogada
caminho = 0  # Tamanho do caminho quando fechar
resultado_partida = False  # Verifica se alguem fez velha

while True:
    num_jogada += 1
    print(
        f"{num_jogada}° - Vez do jogador {simb[vez]}, selecione uma casa {nomes[vez]}")
    print(opcs_validas)
    mostrar_casas()

    while True:
        prim_jogada = int(input("Digite sua primeira casa: "))
        seg_jogada = int(input("Digite sua segunda casa: "))
        if valida_escolha(prim_jogada, seg_jogada):
            marca_quadrados(simb[vez], num_jogada, prim_jogada, seg_jogada)
            caminho, resultado = verifica_jogada(num_jogada, prim_jogada)

            if (resultado == True):
                Marcando_Pontos(vez, prim_jogada, seg_jogada,
                                caminho, num_jogada)
                mostrar_casas()
                resultado_partida = verifica_ganhou()
                # print('\nResultado da Partida:', resultado_partida)

            vez = ~vez  # muda a vez
            break

    if (resultado_partida != False):
        if (resultado_partida == "O "):
            print(f'O {resultado_partida}- jogador(a) {nomes[0]} Ganhou !!!')
        if (resultado_partida == "X "):
            print(f'O {resultado_partida}- jogador(a) {nomes[1]} Ganhou !!!')
        break

    time.sleep(2)
