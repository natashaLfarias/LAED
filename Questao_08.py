from Criar_vetor import criar_vetor

v = criar_vetor(10, 1, 50)
u = criar_vetor(10, 1, 50)
print("V =", v)
print("U =", u)
a = []
achei = 0
for i in range(len(v)):
        for j in range(len(u)):
            if v[i] == u[j] and v[i] not in a:
                print(u[j], "aparece em ambas as listas")
                a.append(u[j])
                achei = 1
                break
if not achei:
     print("Não tem!")