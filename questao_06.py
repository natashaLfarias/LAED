class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.topo = None

    def push(self, x):
        aux = Node(x)
        aux.next = self.topo
        self.topo = aux

    def pop(self):
        if self.topo is None:
            print("Pilha vazia!")
            return -1
        aux = self.topo
        self.topo = self.topo.next
        removido = aux.data

        return removido

class QueueComPilhas:
    def __init__(self):
        self.p1 = Stack()
        self.p2 = Stack()

    def enqueue(self, x):
        self.p1.push(x)

    def dequeue(self):
        if self.p2.topo is None:
            if self.p1.topo is None:
                print("Vazia!")
                return -1

            while self.p1.topo != None:
                valor = self.p1.pop()
                self.p2.push(valor)

        return self.p2.pop()


fila = QueueComPilhas()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)

deq1 = fila.dequeue()
deq2 = fila.dequeue()
deq3 = fila.dequeue()
print("Na fila: inicio -> 1 <- 2 <- 3 <- fim")
print(f"remoção em ordem: {deq1}, {deq2}, {deq3}")

# A fila funciona normalmento, o primeiro a entra é o primeiro a sair.

'''
Enqueue: o custo real é O(1) (um único Push em P1), e Φ aumenta em 1 (mais um elemento em P1). 
Custo amortizado = custo real + ΔΦ = O(1) + O(1) = O(1).

Dequeue quando P2 não está vazia: custo real O(1) (um único Pop em P2), e Φ não muda (P1 não é tocada). 
Custo amortizado = O(1) + 0 = O(1).

Dequeue quando P2 está vazia e P1 tem k elementos: o custo real é O(k) (k Pops em P1 seguidos de k Pushes em P2) 
mais O(1) do Pop final em P2, ou seja O(k+1). Mas Φ diminui em k (P1 perde seus k elementos), então ΔΦ = -k. 
Custo amortizado= O(k+1) - k = O(1).
'''
