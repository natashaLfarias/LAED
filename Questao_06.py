from Criar_vetor import criar_vetor

v = criar_vetor(10, 1, 50)
print("V =", v)

bicho_menor = abs(v[0] - v[1])

for i in range(len(v)):
    j = i + 1
    for j in range(len(v)):
        if(v[i] > v[j]):
            dif = v[i] - v[j]
        elif(v[j] > v[i]):
            dif = v[j] - v[i]
        else:
            continue
        if(dif < bicho_menor):
            bicho_menor = dif
            a = v[i]
            b = v[j]
print(a, " e ", b, " são os mais próximos")