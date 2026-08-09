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

def elem_repetidos(p):
    if p is None:
        print("Não!")

    q = p.head
    repetidos = False

    while q is not None:
        l = q.next

        while l is not None:
            if l.data == q.data:
                repetidos = True
                print("Sim!")
                
            l = l.next

        q = q.next

    if not repetidos:
        print("Não!")
        return

p = LinkedList()
p.head = Node(2)
p.head.next = Node(9)
p.head.next.next = Node(7)
p.head.next.next.next = Node(4)
p.head.next.next.next.next = Node(1)

LinkedList.imprimirLista(p)
elem_repetidos(p)

p2 = LinkedList()
p2.head = Node(2)
p2.head.next = Node(9)
p2.head.next.next = Node(9)
p2.head.next.next.next = Node(4)
p2.head.next.next.next.next = Node(1)

LinkedList.imprimirLista(p2)
elem_repetidos(p2)

# Tempo de execução = O(n^2)

            
