import random
from Criar_vetor import criar_vetor

V = criar_vetor(10, 1, 50)
A = []
k = random.randint(1, 50)
print("V =", V, " K =", k)
i = 0
achei = 0
while i < len(V):
    if V[i] == k:
        print(k, "está na lista!")
        achei = 1
        break
    else:
        prox = abs(V[i] - k)
        A.append(prox)
    i += 1
if(not achei):
    j = 1
    men = A[0]
    while j < len(A):
        if A[j] < men:
            men = A[j]
            aux = j
        j+=1
    print(f"{k} não está lá, más eu achei {V[aux]}")