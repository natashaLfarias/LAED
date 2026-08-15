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

v = [1, 3, 7, 10, 13, 18, 21, 27]
p = criar_vetorEsperso(v)
imprimirLista(p)

k = 4
listaDeLista = lista_de_lista(p, k)
for i in range(k):
    print(f"lista[{i}] -> ", end="")
    imprimirLista(listaDeLista[i])




