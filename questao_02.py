class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def imprimirLista(p):
    q = p
    while q is not None:
        print(q.data, end="")
        if q.next is not None:
            print(" <-> ", end="")
        q = q.next
    print()

def atualizar(p, x, y):
    q = p
    while q is not None and q.data != x:
        q = q.next

    if q is None:
        return(p)
    
    q.data = y
    if (q.prev is None or q.prev.data <= y) and (q.next is None or q.next.data >= y):
        return p

    if q.prev is not None:
        q.prev.next = q.next
    else:
        p = q.next

    if q.next is not None:
        q.next.prev = q.prev

    q.next = None
    q.prev = None
    if p is None or p.data >= y:
        q.next = p
        if p is not None:
            p.prev = q
        return q

    busca = p
    while busca.next is not None and busca.next.data < y:
        busca = busca.next

    q.next = busca.next
    if busca.next is not None:
        busca.next.prev = q

    busca.next = q
    q.prev = busca

    return(p)

p = Node(3)

p.next = Node(5)
p.next.prev = p

p.next.next = Node(9)
p.next.next.prev = p.next

p.next.next.next = Node(10)
p.next.next.next.prev = p.next.next

p.next.next.next.next = Node(15)
p.next.next.next.next.prev = p.next.next.next

print("\np original: ")
imprimirLista(p)
print("\np atualizado c/ x = 9 e y = 12")
p_atualizado = atualizar(p, 9, 12)
imprimirLista(p_atualizado)
print()

# Tempo de execução = O(n)