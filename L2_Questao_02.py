import random
from Criar_vetor import criar_vetor
from Selection_Sort import selection_sort

v = criar_vetor(10, 1, 50)
k = random.randint(1, 10)
print("V ñ ordenado =", v)
selection_sort(v)
print("V Ordenado =", v, "K =", k)
print("O", k,"maior é =", v[k - 1])

#Tempo de execução = (Esse eu vou fazer com o select sort) O(n^2) + O(1)*3 = O(n^2)


