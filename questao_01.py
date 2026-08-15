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

def tamanho(p):
    tam = 0
    while p is not None:
        tam+=1
        p = p.next
    return tam

def elemCentral(p):
    q = p
    tam = 5
    tam = tamanho(p)
    if tam % 2 == 0:
        posEC = tam / 2
    else:
        posEC = tam // 2 + 1
    pos_atual = 0
    while q is not None:
        pos_atual+=1
        if pos_atual == posEC:
            print("Elemento Central: ", q.data)
            return
        q = q.next

p = Node(3)

p.next = Node(9)
p.next.prev = p

p.next.next = Node(5)
p.next.next.prev = p.next

p.next.next.next = Node(2)
p.next.next.next.prev = p.next.next

p.next.next.next.next = Node(8)
p.next.next.next.next.prev = p.next.next.next



imprimirLista(p)
elemCentral(p)

# Tempo de execução = O(n)








    

