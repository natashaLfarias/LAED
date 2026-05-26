import random
from Criar_vetor import criar_vetor

v = criar_vetor(10, 1, 10)
k = random.randint(1, 5)

print("V =", v, "k =", k)
achei = 0

for i in range(len(v)):
    for j in range(i + 1, len(v) - 1):
        if v[i] == v[j] and j == i + k:
            achei = 1
            print("Sim, o", v[i], "nas posições", i, "e", j)

if not achei:
    print("Não tem!")

#Tempo de Execução = O(n^2) + O(1) * 3 = O(n^2)