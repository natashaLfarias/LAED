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
if(A[0] > A[1]):
    m1 = A[0]
    m2 = A[1]
else:
    m1 = A[1]
    m2 = A[0]
while i < len(A):
    if(A[i] > m1):
        m2 = m1
        m1 = A[i]
    elif(A[i] > m2):
        m2 = A[i]
    i+=1
print(f"Segundo maior número ímpar é {m2}")