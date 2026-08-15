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

def troca(p1, p2):
    ant_p1 = p1.prev
    dep_p2 = p2.next

    if ant_p1 is not None:
        ant_p1.next = p2

    if dep_p2 is not None:
        dep_p2.prev = p1

    p2.prev = ant_p1
    p2.next = p1
    p1.prev = p2
    p1.next = dep_p2

def varredura(p):
    if p is None or p.next is None:
        return(p)

    q = p
    head = p

    while q is not None and q.next is not None:
        if q.data > q.next.data:
            if q == head:
                head = q.next

            troca(q, q.next)

        else:
            q = q.next

    return head

p = Node(8)

p.next = Node(5)
p.next.prev = p

p.next.next = Node(7)
p.next.next.prev = p.next

p.next.next.next = Node(2)
p.next.next.next.prev = p.next.next

p.next.next.next.next = Node(13)
p.next.next.next.next.prev = p.next.next.next


print("\np original: ")
imprimirLista(p)
print("\np c/ varredura:")
p_varredura = varredura(p)
imprimirLista(p_varredura)
print()

# Tempo = O(n)

