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

def maior_final(p):
    if(p.head == None or p.head.next == None):
        return(p)
    
    q = p.head; m = p.head
    ant = None; ant_m = None

    while(q != None):
        if(q.data > m.data):
            m = q
            ant_m = ant
        ant = q
        q = q.next

    ultimo = ant

    if(m == ultimo):
        return
    if(m == p):
        p.head = p.head.next
    else:
        ant_m.next = m.next

    ultimo.next = m
    m.next = None

p = LinkedList()
p.head = Node(5)
p.head.next = Node(8)
p.head.next.next = Node(13)
p.head.next.next.next = Node(2)
p.head.next.next.next.next = Node(10)

LinkedList.imprimirLista(p)
maior_final(p)
LinkedList.imprimirLista(p)

# O tempo de execução é igual a O(n), pois percorre todos o elementos da lista encadeada.
