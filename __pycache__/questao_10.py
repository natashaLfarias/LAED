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

def criar_vetorEsperso(v):
    head = None
    ultimo = None

    for i in range(len(v)):
        if v[i] != 0:
            novoNo = Node(v[i])
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

def lista_de_lista(p, k):
    if p is None or k <= 0:
        return None

    q_aux = p
    tam_p = 0
    while q_aux is not None:
        tam_p+=1
        q_aux = q_aux.next

    tam_sub = tam_p // k
    mod = tam_p % k

    lista = [0] * k

    q = p
    for i in range(k):
        lista[i] = q

        if i < mod:
            tam_atual = tam_sub + 1
        else:
            tam_atual = tam_sub
        if tam_atual == 0 or q is None:
            continue

        for _ in range(tam_atual - 1):
            if q is not None:
                q = q.next

        if q is not None and q.next is not None:
            prox_sub = q.next
            q.next = None
            prox_sub.prev = None
            q = prox_sub
        else:
            q = None

    return lista

def imprimirLL(l, k):
    for i in range(k):
        print(f"lista[{i}] -> ", end="")
        imprimirLista(l[i])

def busca(l, x):
    if not l or l[0] is None:
        return -1

    k = len(l)
    index = 0

    while index < k-1 and l[index + 1] != None and l[index + 1].data <= x:
        index+=1

    q = l[index]
    while q is not None and q.data <= x:
        if q.data == x:
            print("achei!")
            return True
        q = q.next

    return -1

def insercao(l, x):
    if not l:
        return

    k = len(l)
    index = 0
    while index < k-1 and l[index + 1] != None and l[index + 1].data <= x:
        index+=1

    novoNo = Node(x)
    q = l[index]

    if q is None:
        l[index] = novoNo
        return

    if x < q.data:
        novoNo.next = q
        q.prev = novoNo
        l[index] = novoNo
        return

    while q.next is not None and q.next.data < x:
        q = q.next

    novoNo.next = q.next
    novoNo.prev = q

    if q.next is not None:
        q.next.prev = novoNo

    q.next = novoNo

def remocao(l, x):
    if not l or l[0] is None:
        return -1

    k = len(l)
    index = 0

    while index < k-1 and l[index+ 1] is not None and l[index+1].data <= x:
        index+=1

    q = l[index]
    while q is not None and q.data < x:
        q = q.next

    if q is None or q.data != x:
        return -1

    if q.prev is not None:
        q.prev.next = q.next
    else:
        l[index] = q.next 

    if q.next is not None:
        q.next.prev = q.prev

    return True

v = [2, 9, 15, 19, 31, 49]
p = criar_vetorEsperso(v)
imprimirLista(p)
lista = lista_de_lista(p, 3)
imprimirLL(lista, 3)

print(busca(lista, 9))
insercao(lista, 13)
print()
imprimirLL(lista, 3)
remocao(lista, 9)
print()
imprimirLL(lista, 3)
print(busca(lista, 9))

    

