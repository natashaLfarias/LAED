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

v = [0, 0, 0, 4, 0, 0, 0, 5, 0, 10, 0, 0, 1, 0, 0, 0, 0, 9, 0]
p = criar_vetorEsperso(v)
imprmirLista(p)

def busca_por_indice(p, k):
    if p is None or k < 0:
        return None
    
    q = p
    while q is not None:
        if q.index == k:
            print(f"Valor do ídice {k} = {q.data}")
            return q.data
        if q.next is None:
            print(f"Índice {k} com 0 ou maior que o tamanho do vetor!")
            return
        q = q.next

busca_por_indice(p, 9)

def busca_por_valor(p, x):
    if p is None:
        return None
    
    q = p
    while q is not None:
        if q.data == x:
            print(f"{x} está no índice {q.index}")
            return q.index
        if q.next is None:
            print("Valor não está na lista!")
            return -1
        q = q.next

busca_por_valor(p, 1)

def atualizacao(p, x, k):
    if p is None or k < 0:
        return None
    q = p
    while q is not None:
        if q.index == k:
            q.data = x
            return
        q = q.next

atualizacao(p, 12, 17)
imprmirLista(p)

'''
busca por índice = O(n), n é o tamanho da lista espersa
busca por valor = O(n)
atualização = O(n)
'''