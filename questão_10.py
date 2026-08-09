class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def imprimirLista(p):
        p = p.head
        while p is not None:
            print(f"{p.data}", end="")
            if p.next is not None:
                print(" -> ", end="")
            p = p.next
        print()

    def insercao(p, val):
        novoNo = Node(val)
        if p.head is None:
            p.head = novoNo
            return
        q = p.head
        while q.next is not None:
            q = q.next
        q.next = novoNo

    def busca(p, k):
        q = p.head
        while q is not None:
            if q.data == k:
                return True
            q = q.next
        return False

def intersecao(p1, p2):
    resultado = LinkedList()
    q1 = p1.head
    while q1 is not None:
        q_val = q1.data
        if not resultado.busca(q_val):
            q2 = p2.head
            while q2 is not None:
                if q2.data == q_val:
                    resultado.insercao(q_val)
                    break
                q2 = q2.next
        q1 = q1.next
    return resultado

p1 = LinkedList()
p1.head = Node(3)
LinkedList.insercao(p1, 9)
LinkedList.insercao(p1, 2)
LinkedList.insercao(p1, 6)
LinkedList.insercao(p1, 4)
print("p1:")
LinkedList.imprimirLista(p1)

p2 = LinkedList()
p2.head = Node(4)
LinkedList.insercao(p2, 5)
LinkedList.insercao(p2, 2)
LinkedList.insercao(p2, 9)
LinkedList.insercao(p2, 3)
print("p2:")
LinkedList.imprimirLista(p2)

inter = LinkedList()
inter = intersecao(p1, p2)
print("Interseção:")
LinkedList.imprimirLista(inter)

# Tempo de execução = O(n^2)
