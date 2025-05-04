from random import randint

def rolar_dados(number):
    vector = []
    for i in range(number):
        vector.append(randint(1,6))
    return vector

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    return [dados_rolados[:dado_para_guardar] + dados_rolados[dado_para_guardar + 1:], dados_no_estoque]