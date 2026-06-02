from Criar_vetor import criar_vetor
from BubbleSort import bubbleSort
from Particao import particao

v = criar_vetor(10, 1, 50)
print("\nV =", v)
pivo = particao(v)[1]

print("\nV c/ partição =", particao(v)[0], "Pivô =", pivo)

for i in range(len(v) - 1):
    if v[i] == pivo:
        posP = i
        break

print("\nV c/ bubble =", bubbleSort(v, 0, posP - 1))

print("\nV c/ bubble 2 =", bubbleSort(v, posP + 1, len(v) - 1), "\n")

'''
Melhor Caso: A partição irá dividir a lista exatamento ou aproximadamento ao meio, tendo uma tempo de
execução = O(n). Nesse caso o bubble será feito O(n^2/2) duas vezes, mas como o babble é modificado, se
for o caso de as duas partes já estarem ordenadas, ele vai ter tempo = 2 * O(n/2).
    No total = O(n) + 2 * O(n/2)

Pior Caso: O pivo da partição será uma das extremidades sendo O(n). Assim o bubble percorrerá a lista 
(n-1) vezes, tendo aproximadamente O(n^2).
    No total = O(n) + O(n^2)

'''