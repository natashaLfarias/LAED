class Node:
    def __init__(self, data, index):
        self.data = data
        self.index = index
        self.next = None
        self.prev = None

def imprmirLista(p):
    q = p
    while q is not None:
        print(q.data, q.index, end="")
        if q.next is not None:
            print(" <-> ", end="")
        q = q.next
    print()

def criar_vetorEsperso(v):
    head = None
    ultimo = None

    for i in range(len(v)):
        if v[i] != 0:
            novoNo = Node(v[i], i)
            novoNo.next = None
            novoNo.prev = None

            if head is None:
                head = novoNo
                ultimo = novoNo
            else:
                ultimo.next = novoNo
                novoNo.prev = ultimo
                ultimo = novoNo

    return head

v = [0, 3, 0, 0, 0, 5, 0, 2, 0, 0, 8, 0, 0, 7, 0]

pTeste = criar_vetorEsperso(v)

imprmirLista(pTeste)

# tempo = O(n), sendo n o tamanho do vetor dessa vez
