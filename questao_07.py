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

def remover_copias(p, k):
    dep_q = Node(0)
    dep_q.next = p.head
    q = dep_q

    while q.next is not None:
        if q.next.data == k:
            q.next = q.next.next
        else:
            q = q.next

    p.head = dep_q.next
    return(p)

    
p = LinkedList()
p.head = Node(1)
p.head.next = Node(3)
p.head.next.next = Node(3)
p.head.next.next.next = Node(2)
p.head.next.next.next.next = Node(3)
p.head.next.next.next.next.next = Node(2)

LinkedList.imprimirLista(p)
remover_copias(p, 3)
LinkedList.imprimirLista(p)

# Tempo de execução = O(n)