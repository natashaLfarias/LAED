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

def intercalacao(p1, p2):
    q1 = p1.head; q2 = p2.head
    p = LinkedList()
    aux = Node(0)
    ult_aux = aux

    while q1 != None and q2 != None:
        if q1.data <= q2.data:
            ult_aux.next = q1
            q1 = q1.next
        else:
            ult_aux.next = q2
            q2 = q2.next

        ult_aux = ult_aux.next

    if q1 is not None:
        ult_aux.next = q1
    else:
        ult_aux.next = q2

    p.head = aux.next

    return(p)

p1 = LinkedList()
p1.head = Node(3)
p1.head.next = Node(6)
p1.head.next.next = Node(7)
p1.head.next.next.next = Node(10)
p1.head.next.next.next.next = Node(13)

print("p1: ")
LinkedList.imprimirLista(p1)

p2 = LinkedList()
p2.head = Node(2)
p2.head.next = Node(4)
p2.head.next.next = Node(9)
p2.head.next.next.next = Node(11)
p2.head.next.next.next.next = Node(12)

print("p2: ")
LinkedList.imprimirLista(p2)

p = intercalacao(p1, p2)

print("Lista Intercalada:")
LinkedList.imprimirLista(p)

# Tempo de execução = 2 * O(n)
