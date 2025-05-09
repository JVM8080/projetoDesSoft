from random import randint

def rolar_dados(number):
    vector = []
    for i in range(number):
        vector.append(randint(1,6))
    return vector

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    return [dados_rolados[:dado_para_guardar] + dados_rolados[dado_para_guardar + 1:], dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    return [dados_rolados, dados_no_estoque[:dado_para_remover] + dados_no_estoque[dado_para_remover + 1:]]

def calcula_pontos_regra_simples(list):
    dictionary = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(1,7):
        for val in list:
            if val == i:
                dictionary[i] += val
    return dictionary

def calcula_pontos_soma(vector):
    acc = 0
    for val in vector: acc += val
    return acc

def calcula_pontos_sequencia_baixa(data):
    data_un = set(data)
    sequencias_baixas = [
        {1, 2, 3, 4},
        {2, 3, 4, 5},
        {3, 4, 5, 6}
    ]
    
    for seq in sequencias_baixas:
        if seq.issubset(data_un):
            return 15
    return 0

def calcula_pontos_sequencia_alta(data):
    data_un = set(data)
    sequencias_altas = [
        {1, 2, 3, 4, 5},
        {2, 3, 4, 5, 6}
    ]
    
    for seq in sequencias_altas:
        if seq.issubset(data_un):
            return 30
    return 0

def calcula_pontos_full_house(data):
    count = {}
    for number in data:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1

    value = list(count.values())
    if (len(value) == 2 and ((value[0] == 3 and value[1] == 2) or
                               (value[0] == 2 and value[1] == 3))):
        count = 0
        for number in data:
            count += number
        return count
    else:
        return 0

def calcula_pontos_quadra(data):
    counts = {}

    for number in data:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    has_four = False
    for count in counts.values():
        if count >= 4:
            has_four = True
            break

    if has_four:
        total = 0
        for number in data:
            total += number
        return total
    else:
        return 0
    
def calcula_pontos_quina(data):
    counts = {}

    for number in data:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    for count in counts.values():
        if count >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(data):
    return {
        'cinco_iguais': calcula_pontos_quina(data),
        'full_house': calcula_pontos_full_house(data),
        'quadra': calcula_pontos_quadra(data),
        'sem_combinacao': calcula_pontos_soma(data),
        'sequencia_alta': calcula_pontos_sequencia_alta(data),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(data),
    }
    
def faz_jogada(data, category, score_card):
    if category in ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']:
        advanced_scores = calcula_pontos_regra_avancada(data)
        score_card['regra_avancada'][category] = advanced_scores[category]
            
    elif category in ['1', '2', '3', '4', '5', '6']:
        category_int = int(category)
        simple_scores = calcula_pontos_regra_simples(data)
        score_card['regra_simples'][category_int] = simple_scores[category_int]
    return score_card

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)