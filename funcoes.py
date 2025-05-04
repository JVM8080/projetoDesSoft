from random import randint

def rolar_dados(number):
    vector = []
    for i in range(number):
        vector.append(randint(1,6))
    return vector
