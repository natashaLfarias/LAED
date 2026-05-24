from Criar_vetor import criar_vetor

v = criar_vetor(10, 1, 20)
print("V =", v)
achou = 0
achei = 0
for i in range(len(v)):
    achei = 0
    j = i + 1
    for j in range(len(v)):
        if v[j] == v[i]*2:
            if achei:
                continue
            else:
                print(f"Os números {v[i]} e {v[j]}")
                achei = 1
                achou = 1
if(not achou):
    print("Não tem")