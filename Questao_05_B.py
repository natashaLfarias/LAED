from Criar_vetor import criar_vetor
from Selection_Sort import selection_sort

v = criar_vetor(10, 1, 50)
selection_sort(v)
print("V =", v)
i = 0; j = 1
achei = 0
while j < len(v):
    if v[j] == 2 * v[i]:
        print(f"Os números {v[i]} e {v[j]}")
        achei = 1
        i += 1
        j += 1
    elif v[j] < 2 * v[i]:
        j += 1
    else:
        i += 1
        if i == j:
            j += 1
if(not achei):
    print("Não tem!")