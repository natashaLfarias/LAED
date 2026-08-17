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

    def imprimirPilha(self):
        if self.topo is None:
            print("Pilha vazia")
            return
            
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
pilha.push(17)
pilha.push(42)

pilha.imprimirPilha()

pilha.push(99)
pilha.push(3)

pilha.imprimirPilha()

pop1 = pilha.pop()
print("Primeiro Pop: ", pop1)
pilha.imprimirPilha()
pop2 = pilha.pop()
print("Segundo Pop: ", pop2)
pilha.imprimirPilha()

'''
A gente guarda o pop numa variável auxiliar, para poder retornar o valor do elemento que foi removido antes de
tirar ele da memória.

Se liberar o nó atual e sem atualizar o topo, eu perco a variável que guarda a pilha, porque se o topo for excluido
vai ter erro ao tentar acessar o topo.next.

'''
