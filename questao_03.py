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
        if self.pop is None:
            print("Pilha vazia!")
            return -1
        aux = self.topo
        self.topo = self.topo.next
        removido = aux.data

        return removido

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

    def imprimirFila(self):
        if self.inicio is None:
            print("Fila vazia!")
            return -1
            
        valores = []
        q = self.inicio
        
        while q is not None:
            valores.append(str(q.data))
            q = q.next
            
        resultado = "Início -> " + " -> ".join(valores) + " <- Fim"
        print(resultado)

def inverterFila_com_Pilha(f):
    pilha_aux = Stack()
    
    while f.inicio is not None:
        valor = f.dequeue()
        pilha_aux.push(valor)
        
    while pilha_aux.topo is not None:
        valor = pilha_aux.pop()
        f.enqueue(valor)

fila = Queue()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)

fila.imprimirFila()

inverterFila_com_Pilha(fila)

fila.imprimirFila()

# Complexidade = O(n), percorre a fila toda e a pilha toda, 2 * O(n) = O(n)

'''
Dá certo inverter sem usar uma fila auxiliar, manipulando ponteiros, como ela é só
uma representeção diferente de um lista encadeado normal, dá certo percorrer ela com
variáveis que guardam o anterior, o atua e o proximo, e ir manipulando o ponteiro next
deles, para inverter a ordem e no final trocar os ponteiro inicio e o fim da fila.
'''
