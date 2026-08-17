from typing import List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enqueue(self, x):
        novoNo = Node(x)
        if self.fim is None:
            self.inicio = self.fim = novoNo
        else:
            self.fim.next = novoNo
            self.fim = novoNo

    def dequeue(self):
        if self.inicio is None:
            return -1
        
        remocao = self.inicio.data
        self.inicio = self.inicio.next
        if self.inicio is None:
            self.fim = None
            
        return remocao

def radix_sort(lista: List[int]) -> List[int]:

    if not lista:
        return []

    maior_valor = max(lista)
    exp = 1
    filas = [Queue() for _ in range(10)]

    while maior_valor // exp > 0:
        for num in lista:
            digito = (num // exp) % 10
            filas[digito].enqueue(num)

        lista_ordenada = []
        for f in filas:
            while f.inicio is not None:
                lista_ordenada.append(f.dequeue())

        lista = lista_ordenada
        exp *= 10

    return lista



v = [481, 329, 143, 612, 937, 480, 256]

print(f"Vetor: {v}")
v_ordenado = radix_sort(v)
print(f"Vetor Ordenado: {v}")

'''
O radix sort precisa da estabilidade que a fila dá, por ela ser FIFO, ela dá estabilidade quando há números com
o mesmo número na unidade, dezena, centena... , no v tem o 480 e 481 seriam os afetados caso fosse uma pilha, 
porque na pilha de dezena 8, quem sairia primeiro seria o 481, pela propriedade da pilha LIFO, no final, como os
outros não tem o mesmo número em algum decimal, eles não seriam afetados, mas ,nesse caso, no vetor final o 481 e
o 480 ficariam trocados e no final o vetor não ficaria ordenado. 

'''

'''
0: inicio -> 480 <-fim | 0: inicio ->  <-fim           | 0: inicio ->  <-fim
1: inicio -> 481 <-fim | 1: inicio -> 612 <-fim        | 1: inicio -> 143 <-fim 
2: inicio -> 612 <-fim | 2: inicio -> 329 <-fim        | 2: inicio -> 256 <-fim 
3: inicio -> 143 <-fim | 3: inicio -> 937 <-fim        | 3: inicio -> 329 <-fim 
4: inicio -> <-fim     | 4: inicio -> 143 <-fim        | 4: inicio -> 480 <- 481 <-fim
5: inicio -> <-fim     | 5: inicio -> 256 <-fim        | 5: inicio ->  <-fim  
6: inicio -> 256 <-fim | 6: inicio ->  <-fim           | 6: inicio -> 612 <-fim
7: inicio -> 937 <-fim | 7: inicio ->  <-fim           | 7: inicio ->  <-fim 
8: inicio -> <-fim     | 8: inicio -> 480 <- 481 <-fim | 8: inicio ->  <-fim
9: inicio -> 329 <-fim | 9: inicio ->  <-fim           | 9: inicio -> 937 <-fim 

'''
'''
Complexidade: O(l * (n + sigma))

para o merge sort seria complexidade O(n * log(n)), ele depende somente da quantidade de Strings, mas como é um 
número n qualquer, o radix sort leva vantagem quando é um número muito grande de dados, mas o  sigma e o l não 
são números muito extensos.

'''
