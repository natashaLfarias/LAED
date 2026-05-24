from Criar_vetor import criar_vetor

v = criar_vetor(10, 1, 50)
print("V =", v)

cont = 0
for i in range(len(v)):
    for j in range(1, len(v)):
        if i < j and v[i] > v[j]:
            cont+=1
        else:
            continue
print("Número de inversões = ", cont)