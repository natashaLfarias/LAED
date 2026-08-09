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

def elem_mais_recorrente(p):
    if p is None:
        return(p)
    
    elem_rec = None
    max_aparicoes = 0
    q = p.head

    while q is not None:
        cont = 1
        l = q.next

        while l is not None:
            if l.data == q.data:
                cont+=1

            l = l.next

        if cont > max_aparicoes:
            max_aparicoes = cont
            elem_rec = q.data

        q = q.next

    return elem_rec

p = LinkedList()
p.head = Node(8)
p.head.next = Node(8)
p.head.next.next = Node(3)
p.head.next.next.next = Node(5)
p.head.next.next.next.next = Node(8)
p.head.next.next.next.next.next = Node(3)

print("p:")
LinkedList.imprimirLista(p)
print("Elemento mais recorrente: ", elem_mais_recorrente(p))

# Tempo de execução = O(n)