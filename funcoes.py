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