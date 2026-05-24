from Criar_vetor import criar_vetor

V = criar_vetor(10, 1, 50)
print("V =", V)
A = []
i = 0; j = 0
while i < len(V):
    if(V[i] % 2 != 0):
        A.append(V[i])
    i+=1
i = 1
m = A[0]
while i < len(A):
    if(A[i] > m):
        m = A[i]
    i+=1
print(f"Maior número ímpar = {m}")