def bubbleSort(V, ini, fim):

    continua = True

    while(continua):
        continua = False
        for i in range(ini, fim):
            if(V[i] > V[i+1]):
                V[i], V[i+1] = V[i+1], V[i]
                continua = True
        fim = fim - 1

    return(V)