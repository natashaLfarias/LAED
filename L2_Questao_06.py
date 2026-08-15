from Criar_vetor import criar_vetor
from Selection_Sort import selection_sort

v = criar_vetor(10, 1, 10)
a = criar_vetor(10, 1, 10)

print("V =", v)
print("A =", a)

selection_sort(v)
selection_sort(a)

print("\nV ordenado =", v)
print("A ordenado =", a)

if a == v:
    print("\nSim, A é uma permutação de V")
else:
    print("\nNão")

#Tempo de Execução = 2 * O(n^2) = O(n^2) por conta da ordenção