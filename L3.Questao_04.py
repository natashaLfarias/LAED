from Criar_matriz import criar_matriz

m = criar_matriz(4, 4, 1, 9)
aux = []

for linha in m:
    print(linha)

for i in range(len(m)):
    for j in range(len(m)):
        elem = m[i][j]
        for l in range(len(m)):
            for c in range(len(m)):
                if i != l and j != c:
                    if elem == m[l][c] and m[l][c] not in aux:
                        print(f"Sim,o elemento {elem} aparece mais de uma vez")
                        aux.append(m[l][c])
