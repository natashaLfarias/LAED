class Node:
    def __init__(self, data, min):
        self.data = data
        self.next = None
        self.min = min

class Stack:
    def __init__(self):
        self.topo = None

    def push(self, x):
        if self.topo is None:
            novoNo = Node(x, x)
        else:
            menorVal = min(x, self.topo.min)
            novoNo = Node(x, menorVal)
        
        novoNo.next = self.topo
        self.topo = novoNo

    def pop(self):
        if self.topo is None:
            print("Pilha vazia!")
            return -1
        aux = self.topo
        self.topo = self.topo.next
        val = aux.data

        return val

    def min_val(self):
        if self.topo is None:
            print("Pilha vazia!")
            return -1
            
        return self.topo.min

    def imprimirPilha(self):
        if self.topo is None:
            print("Pilha vazia")
            return -1

        valores = []
        q = self.topo
        while q is not None:
            valores.append(str(q.data))
            q = q.next  

        valores.reverse()
        resultado = " -> ".join(valores) + " <- topo"
        print(resultado)

pilha = Stack()
pilha.push(5)
pilha.imprimirPilha()
print("Mínimo atual: ", pilha.min_val())
pilha.push(3)
pilha.imprimirPilha()
print("Mínimo atual: ", pilha.min_val())
pilha.push(7)
pilha.imprimirPilha()
print("Mínimo atual: ", pilha.min_val())
pilha.push(1)
pilha.imprimirPilha()
print("Mínimo atual: ", pilha.min_val())

'''
O nó vai guardar o valor mínimo, aí cada vezz que acontece um push, a função verifica se o valor novo é menor que
o min, e se for atualiza o min.

O tempo de execução vai ser O(1), tirando a função de imprimir viu, mas o custo extra de memória vai ser a variá-
vel que guarda o valor mínimo que cada nó terá que guardar, tendo o custo extra de memória O(n).
'''
