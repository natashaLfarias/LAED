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

fila = Queue()
fila.enqueue(8)
fila.enqueue(15)
fila.enqueue(23)

fila.imprimirFila()

fila.enqueue(7)
fila.enqueue(11)

fila.imprimirFila()

dequeue1 = fila.dequeue()
dequeue2 = fila.dequeue()

fila.imprimirFila()

dequeue = fila.dequeue()
dequeue = fila.dequeue()
dequeue = fila.dequeue()

print("\nDepois de esvaziar a fila: ")
fila.imprimirFila()
print("início: ", fila.inicio)
print("Fim: ", fila.fim)

'''
Qunado sobra só um valor, o inicio e o fim são iguais, quando o último que sobrou é removido o inicio recebe o 
próximo (que nesse caso é nulo) e no dequeue se o inicio for vazio o fim se iguala a ele, no final ambos vão fi-
car nulos.

Se acontecer do inicio for nulo e o fim não, a fila vai quebrar, porque o inicio e o fim guardavam o mesmo valor,
o inicio vai ser atualizado para nulo, mas o fim aponta para um valor que não deveria existe mais, logo, quando for 
inserir novos elementos a gente vai perder os valores inseridos, tendo acesso apenas ao último. Vai acabar com toda
a estrutura da fila e ainda vamos perder elementos inseridos na memória, já que o enqueue ainda vai funcionar.
'''