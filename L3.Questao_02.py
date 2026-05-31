from Criar_vetor import criar_vetor
from BubbleSort import bubbleSort

v = criar_vetor(12, 1, 50)

a = (2 * len(v)//3)
b = len(v)//3

print("V =", v)

print("Bubble 1 =", bubbleSort(v, 0, a - 1))
print("Bubble 2 =", bubbleSort(v, b, len(v) - 1))
print("Bubble 3 =", bubbleSort(v, 0, a - 1))

#Tempo de execução = 3 * O((2n/3)^2)