opcs_validas = """
0|1|2
3|4|5
6|7|8
"""


def valida_escolha(prim_escolha, seg_escolha):
    if prim_escolha > 8:
        print("A primeira opção está fora dos valores permitidos")
        print("Selecione Novamente !!")
        return False
    elif seg_escolha > 8:
        print("A segunda opção está fora dos valores permitidos")
        print("Selecione Novamente !!")
        return False
    elif seg_escolha == prim_escolha:
        print("Os quadrados não podem ser iguais")
        print("Selecione Novamente !!")
        return False
    else:
        return True


casas = [["  "], ["  "], ["  "],
         ["  "], ["  "], ["  "],
         ["  "], ["  "], ["  "],]


def marca_quadrados(simbolo, num_jogada, prim_escolha, seg_escolha):

    if (casas[seg_escolha][0] == "  "):
        casas[seg_escolha][0] = (f'{simbolo}{num_jogada}')
    else:
        casas[seg_escolha].append(f'{simbolo}{num_jogada}')

    if (casas[prim_escolha][0] == "  "):
        casas[prim_escolha][0] = (f'{simbolo}{num_jogada}')
    else:
        casas[prim_escolha].append(f'{simbolo}{num_jogada}')

    espacamento = 1

    for b in range(8):
        if len(casas[b]) > espacamento:
            print(casas[b], b)
            espacamento = len(casas[b])

    print("espaçamento: ", espacamento)

    for i in range(9):

        if (i % 3 == 0):
            print()
        else:
            print(" | ", end="")

        if (len(casas[i]) != espacamento):
            qntd_de_espaco = espacamento - len(casas[i])
            for opcs in casas[i]:
                print(opcs, end=" ")
            espaco = "   "
            print(f"{espaco*qntd_de_espaco}", end="")

        else:
            for a in casas[i]:
                print(a, end=" ")
    print("\n=====================================")


def verifica_jogada(simbolo, prim_escolha, seg_escolha):

    # Verifica o posicionamento da primeira escolha:
    if (len(casas[prim_escolha]) >= 2):
        print("Nada Colocado nessa casas - 1")

    # Verifica o posicionamento da segunda escolha:
    if (len(casas[seg_escolha]) >= 2):
        print("Nada Colocado nessa casas - 2")
