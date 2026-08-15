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

def particao(head, fim, k):
    if head is None:
        return None

    q = head
    while fim.next is not None:
        fim = fim.next

    r = fim

    while True:
        while q != r and q.data <= k:
            q = q.next

        while r != q and r.data > k:
            r = r.prev

        if q == r:
            break

        q.data, r.data = r.data, q.data
        
    return head


p = Node(12)

p.next = Node(17)
p.next.prev = p

p.next.next = Node(9)
p.next.next.prev = p.next

p.next.next.next = Node(5)
p.next.next.next.prev = p.next.next

p.next.next.next.next = Node(13)
p.next.next.next.next.prev = p.next.next.next

print("\np original: ")
imprimirLista(p)

print("\np c/ partição:")
p_particao = particao(p, p, 11)
imprimirLista(p_particao)
print()

# Tempo = O(n0)