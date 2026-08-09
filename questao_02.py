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

def par_e_impar(p):
    if p == None:
        return(p)
    
    q = p.head
    par = LinkedList()
    impar = LinkedList()
    ult_par = None; ult_impar = None

    while q is not None:
        if q.data % 2 == 0:
            novoNo_par = Node(q.data)
            if par.head is None:
                par.head = novoNo_par
                ult_par = novoNo_par
            else:
                ult_par.next = novoNo_par
                ult_par = novoNo_par
        else:
            novoNo_impar = Node(q.data)
            if impar.head is None:
                impar.head = novoNo_impar
                ult_impar = novoNo_impar
            else:
                ult_impar.next = novoNo_impar
                ult_impar = novoNo_impar

        q = q.next

    return(par, impar)

p = LinkedList()
p.head = Node(2)
p.head.next = Node(8)
p.head.next.next = Node(5)
p.head.next.next.next = Node(10)
p.head.next.next.next.next = Node(7)

LinkedList.imprimirLista(p)
par, impar = par_e_impar(p)
print("Lista par: ")
LinkedList.imprimirLista(par)
print("Lista impar: ")
LinkedList.imprimirLista(impar)

# Tempo de execução = O(n)