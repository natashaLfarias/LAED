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

def duplicarImpares(p):
    q = p.head
    while q is not None:
        if q.data % 2 != 0:
            novoNo = LinkedList()
            novoNo.data = q.data
            novoNo.next = q.next
            q.next = novoNo
            q = novoNo.next
        else:
            q = q.next

    return(p)

p = LinkedList()
p.head = Node(2)
p.head.next = Node(7)
p.head.next.next = Node(6)
p.head.next.next.next = Node(3)

LinkedList.imprimirLista(p)
duplicarImpares(p)
print("Ímpares Duplicados: ")
LinkedList.imprimirLista(p)

# Tempo de execução = O(n)