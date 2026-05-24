from Criar_vetor import criar_vetor

v = criar_vetor(10, 1, 50)
print("V =", v)
achei = 0
for i in range(len(v)):
    if v[i] % 2 != 0:
        cont = 0
        j = i + 1
        for j in range(len(v)):
            if v[j] == v[i]:
                cont+=1
        if cont%2 != 0:
            print(f"O nº {v[i]} aparece {cont} vezes!")
            achei = 1

if not achei:
    print("Não tem no vetor!")