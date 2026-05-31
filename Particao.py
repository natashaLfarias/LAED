import random

def particao(V):

    fim = len(V) - 1

    k = random.randint(0, fim)
    
    V[k], V[fim] = V[fim], V[k]
    
    pivo = V[fim]
    
    i = 0
    for j in range(0, fim):
        if V[j] < pivo:
            V[i], V[j] = V[j], V[i]
            i += 1

    V[i], V[fim] = V[fim], V[i]
    
    return V, pivo, i

