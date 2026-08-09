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

def inverterLista(p):
    q = p.head
    ant_q = None
    dep_q = None
    while q is not None:
        dep_q = q.next
        q.next = ant_q
        ant_q = q
        q = dep_q
    p.head = ant_q
    return(p)

p = LinkedList()
p.head = Node(3)
p.head.next = Node(2)
p.head.next.next = Node(5)
p.head.next.next.next = Node(9)
p.head.next.next.next.next = Node(4)

LinkedList.imprimirLista(p)
inverterLista(p)
print("Lista Invertida: ")
LinkedList.imprimirLista(p)

# Tempo de execução = O(n)
