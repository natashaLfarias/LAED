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

def particao(p, k):
    aux_maior = Node(0)
    aux_menor = Node(0)
    aux_igual = Node(0)

    menores = aux_menor
    maiores = aux_maior
    iguais = aux_igual

    q = p.head

    while q is not None:
        if q.data < k:
            menores.next = q
            menores = menores.next
        elif q.data == k:
            iguais.next = q
            iguais = iguais.next
        else:
            maiores.next = q
            maiores = maiores.next
        q = q.next

    maiores.next = None

    if aux_igual.next is not None:
        menores.next = aux_igual.next
        iguais.next = aux_maior.next
    else:
        menores.next = aux_maior.next

    partionada = LinkedList()

    if aux_menor.next is not None:
        partionada.head = aux_menor.next
    elif aux_igual.next is not None:
        partionada.head = aux_igual.next
    else:
        partionada.head = aux_maior.next

    return partionada

p = LinkedList()
p.head = Node(9)
p.head.next = Node(2)
p.head.next.next = Node(5)
p.head.next.next.next = Node(6)
p.head.next.next.next.next = Node(1)

print("p: ")
LinkedList.imprimirLista(p)
print("Lista particionada com k = 5")
lp = LinkedList()
lp = particao(p, 5)
LinkedList.imprimirLista(lp)

# Tempo de execução = O(n)