# Importando funções
# teste git
from func import *

nomes = ["O", "X"]
simb = ["O", "X"]
# nomes[1] = input("Digite o nome do jogador X: ")
# nomes[0] = input("Digite o nome do jogador O: ")

nomes[1] = "Rodrigo"
nomes[0] = "Ana"


# Começo do jogo
vez = True  # VEZ == TRUE -> X | VEZ == FALSE -> O
num_jogada = 0  # Numero da jogada
while True:
    num_jogada += 1
    if (vez):

        print(
            f"{num_jogada}° - Vez do jogador {simb[vez]}, selecione uma casa {nomes[vez]}")
        print(opcs_validas)

        while True:
            print("=====================================")
            prim_jogada = int(input("Digite sua primeira casa:"))
            seg_jogada = int(input("Digite sua segunda casa:"))
            if valida_escolha(prim_jogada, seg_jogada):
                marca_quadrados(simb[vez], num_jogada, prim_jogada, seg_jogada)
                verifica_jogada(vez, prim_jogada, seg_jogada)
                vez = ~vez  # muda a vez
                break
