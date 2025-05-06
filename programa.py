from funcoes import *

score_card = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(score_card)

for rodada in range(12):
    dados_guardados = []
    rerrolagens = 0
    dados_rolados = rolar_dados(5)

    while True:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        input_jogada = input()

        while input_jogada not in ["0", "1", "2", "3", "4"]:
            print("Opção inválida. Tente novamente.")
            input_jogada = input()

        if input_jogada == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            index = input()
            if index.isdigit():
                index = int(index)
                if 0 <= index < len(dados_rolados):
                    dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, index)
                else:
                    print("Índice fora do intervalo.")
            else:
                print("Entrada inválida. Digite um número de 0 a 4.")

        elif input_jogada == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            index = input()
            if index.isdigit():
                index = int(index)
                if 0 <= index < len(dados_guardados):
                    dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, index)
                else:
                    print("Índice fora do intervalo.")
            else:
                print("Entrada inválida. Digite um número de 0 a 4.")

        elif input_jogada == "3":
            if rerrolagens < 2:
                rerrolagens += 1
                dados_rolados = rolar_dados(5 - len(dados_guardados))
            else:
                print("Você já usou todas as rerrolagens.")

        elif input_jogada == "4":
            imprime_cartela(score_card)

        elif input_jogada == "0":
            print("Digite a combinação desejada:")
            while True:
                categoria = input()
                if categoria in ["1", "2", "3", "4", "5", "6"]:
                    categoria_num = int(categoria)
                    if score_card["regra_simples"][categoria_num] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        break
                elif categoria in score_card["regra_avancada"]:
                    if score_card["regra_avancada"][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        break
                else:
                    print("Combinação inválida. Tente novamente.")

            dados = dados_guardados + dados_rolados
            faz_jogada(dados, categoria, score_card)
            break

imprime_cartela(score_card)

total = 0
simples = 0

for i in range(1, 7):
    if score_card["regra_simples"][i] != -1:
        simples += score_card["regra_simples"][i]
        total += score_card["regra_simples"][i]

for nome in ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']:
    if score_card["regra_avancada"][nome] != -1:
        total += score_card["regra_avancada"][nome]

if simples >= 63:
    total += 35

print(f"Pontuação total: {total}")
