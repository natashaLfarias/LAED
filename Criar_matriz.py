import random

def criar_matriz(l, c, lim_i, lim_f):

    matriz = []
    
    for i in range(l):
        linha = [0] * c
        for j in range(c):
            linha[j] = random.randint(lim_i, lim_f)
        matriz.append(linha)
        
    return matriz

