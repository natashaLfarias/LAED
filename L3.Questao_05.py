from Criar_matriz import criar_matriz

m = criar_matriz(4, 4, 1, 9)

for linha in m:
    print(linha)

n = len(m)
achei = 0
for i in range(n):
    for j in range(i + 1, n):
        if m[i] == m[j]:
            print(f"\nA linha {i+1} é igual à linha {j+1}")
            achei = 1

if not achei:
    print("\nNão tem")