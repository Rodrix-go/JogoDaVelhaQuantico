import time

opcs_validas = """
Casas Disponíveis:
    0|1|2
    3|4|5
    6|7|8
"""

simb = ["O ", "X "]


def mostrar_casas():
    print("Tabuleiro:", end='')
    espacamento = 1

    for b in range(8):
        if len(casas[b]) > espacamento:
            espacamento = len(casas[b])

    # print("espaçamento: ", espacamento)

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
    print('\n')

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
    elif (simb[0] in casas[prim_escolha]) or ((simb[1] in casas[prim_escolha])):
        print(f'A casa {prim_escolha} já está definida')
        print("Selecione Novamente !!")
        return False
    elif (simb[0] in casas[seg_escolha]) or ((simb[1] in casas[seg_escolha])):
        print(f'A casa {seg_escolha} já está definida')
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
            espacamento = len(casas[b])

    # print("espaçamento: ", espacamento)

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


def verifica_jogada(num_jogada, casa_primeira_jogada):

    elementos = []
    next_casa_elementos = []

    # Primeira vez
    elementos = verifica_casa(casa_primeira_jogada)
    for elemento in elementos:
        next_casa_elementos.append(find_elements(
            elemento, ignorar=casa_primeira_jogada))
    # print(f'Primeira Vez - Elementos:{elementos} e suas proximas casas {next_casa_elementos}')

    probabilidade = num_jogada
    elementos_to_ignorar = []

    primeiros_elementos = list(elementos)
    casas_primeiros_elementos = list(next_casa_elementos)

    caminho_track = []

    cntrl_elements = 0
    if num_jogada == 1:
        return caminho_track, False

    i = 0
    fila = []
    while i < probabilidade:
        if (i == 0):
            #print(f'Trakeando o  elemento {primeiros_elementos[cntrl_elements]}, na casa {casas_primeiros_elementos[cntrl_elements]}')
            elementos_to_ignorar.append(primeiros_elementos[cntrl_elements])

            vetor = []
            vetor.append(primeiros_elementos[cntrl_elements])
            vetor.append(casas_primeiros_elementos[cntrl_elements])
            caminho_track.append(vetor)

            elemento_track = verifica_casa(
                casas_primeiros_elementos[cntrl_elements], elementos_to_ignorar)

            if (len(elemento_track) > 1):
                lista_aux = []

                lista_aux.append(primeiros_elementos[cntrl_elements])
                lista_aux.append(casas_primeiros_elementos[cntrl_elements])
                lista_aux.append(i)

                fila.insert(0, lista_aux)

            if (len(elemento_track) != 0):
                # Sempre vou para o ultimo elemento presente
                next_casa_track = find_elements(
                    elemento_track[0], casas_primeiros_elementos[cntrl_elements])
                # print(f'A Fora o {primeiros_elementos[cntrl_elements]} tem {elemento_track} e a prox casa vai ser {next_casa_track}')
        else:
            # print(f'Trakeando o  elemento {elemento_track[0]}, na casa {next_casa_track}')
            elemento_trakeado = elemento_track[0]

            elementos_to_ignorar.append(elemento_track[0])

            vetor = []
            vetor.append(elemento_track[0])
            vetor.append(next_casa_track)
            caminho_track.append(vetor)

            elemento_track = verifica_casa(
                next_casa_track, elementos_to_ignorar)
            if (len(elemento_track) > 1):
                lista_aux = []

                lista_aux(elemento_trakeado)
                lista_aux(next_casa_track)
                lista_aux(i)

                fila.insert(0, lista_aux)

            if (len(elemento_track) != 0):
                # Sempre vou pegar o primeiro
                next_casa_track = find_elements(
                    elemento_track[0], next_casa_track)
                #print(f'A Fora o {elemento_trakeado} tem {elemento_track} e a prox casa vai ser {next_casa_track}, len: {len(elemento_track)}')

        # Verificações

        if (len(elemento_track) == 0):
            #print('Só tem um elemento')
            #print('Fila:', fila)
            if (len(fila) == 0):

                if cntrl_elements != len(primeiros_elementos)-1:
                    cntrl_elements += 1
                    i = 0
                else:
                    return caminho_track, False

            else:
                #print('Não tinha nada naquele caminho, voltando...')
                aux = len(fila)-1

                elemento_track = fila[aux][0]
                next_casa_track = fila[aux][1]
                i = fila[aux][2]

                caminho_track.pop()
                fila.pop()

        elif (next_casa_track == casa_primeira_jogada):
            # print('A proxima casa volta pro começo')

            vetor = []
            vetor.append(elemento_track[0])
            vetor.append(next_casa_track)

            return caminho_track, True
        else:
            i += 1

        #print("=====================================")
        # print('press to continue', 'Valor de i:', i, 'Possibilidade:',probabilidade)
        # input()


def Marcando_Pontos(vez, casa_primeira_jogada, casa_segunda_jogada, caminho, num_jogada):
    print('Sua jogada resultou em um Colapso !!')
    print(f'        Casa {casa_primeira_jogada} ou Casa {casa_segunda_jogada}')

    # Selecionando por qual das duas opções deseja começar
    while True:
        opc = int(input('Você deseja começar por qual casa: '))
        if (opc != casa_primeira_jogada) and (opc != casa_segunda_jogada):
            print("Opção inválida !!!")
        else:
            break

    if (opc == casa_primeira_jogada):
        comeco = casa_primeira_jogada
    else:
        caminho, resultado = verifica_jogada(num_jogada, casa_segunda_jogada)
        comeco = casa_segunda_jogada

    # print('Caminho:', caminho)  # Printando como ficou o caminho
    vez = ~vez
    # print(f'Coloquei o {simb[vez]} na casa {comeco}')
    casas[comeco].pop()
    casas[comeco][0] = simb[vez]

    i = 0
    while i < len(caminho):
        vez = ~vez
        casas[caminho[i][1]].pop()
        casas[caminho[i][1]][0] = simb[vez]
        #print(f'Coloquei o {simb[vez]} na casa {caminho[i][1]}')
        i += 1


def verifica_casa(casa, remove_element=[]):
    nums_in_casa = []
    nums_in_casa = list(casas[casa])
    # print(nums_in_casa)

    for elements_to_remove in remove_element:
        if (elements_to_remove in nums_in_casa):

            nums_in_casa.remove(elements_to_remove)

    # print('Verifica_Casa (1) -',nums_in_casa)
    return nums_in_casa


def find_elements(element, ignorar=10):
    casas_elements = 0
    for a in range(9):
        for b in range(len(casas[a])):
            if (casas[a][b] == element) and (a != ignorar):
                # print(f'O elemento {element} está na casas', a)
                casas_elements = a

    return casas_elements


def verifica_ganhou():
    for i in range(2):
        if (casas[0][0] == simb[i]) and (casas[1][0] == simb[i]) and (casas[2][0] == simb[i]):
            return simb[i]
        elif (casas[3][0] == simb[i]) and (casas[4][0] == simb[i]) and (casas[5][0] == simb[i]):
            return simb[i]
        elif (casas[6][0] == simb[i]) and (casas[7][0] == simb[i]) and (casas[8][0] == simb[i]):
            return simb[i]
        elif (casas[0][0] == simb[i]) and (casas[3][0] == simb[i]) and (casas[6][0] == simb[i]):
            return simb[i]
        elif (casas[1][0] == simb[i]) and (casas[4][0] == simb[i]) and (casas[7][0] == simb[i]):
            return simb[i]
        elif (casas[2][0] == simb[i]) and (casas[5][0] == simb[i]) and (casas[8][0] == simb[i]):
            return simb[i]
        elif (casas[0][0] == simb[i]) and (casas[4][0] == simb[i]) and (casas[8][0] == simb[i]):
            return simb[i]
        elif (casas[2][0] == simb[i]) and (casas[4][0] == simb[i]) and (casas[6][0] == simb[i]):
            return simb[i]
    return False
