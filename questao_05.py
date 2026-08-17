class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.topo = None

    def push(self, x):
        aux = Node(x)
        aux.next = self.topo
        self.topo = aux

    def pop(self):
        if self.topo is None:
            print("Pilha vazia!")
            return -1
        aux = self.topo
        self.topo = self.topo.next
        removido = aux.data

        return removido

def balanceamento_delimitadores(expressao):
    pilha = Stack()

    for i, c in enumerate(expressao, start=1):
        if c == '(' or c == "[" or c == "{":
            pilha.push(c)
        elif c == ')' or c == "]" or c == "}":
            if pilha.topo is None:
                print(f"Fechador extra na posição {i}!")
                return False
            topo = pilha.pop()

            if (c == ')' and topo != '(') or (c == ']' and topo != '[') or (c == '}' and topo != '{'):
                print(f"Fechador inválido na posição {i}!")
                return False

    if pilha.topo != None:
        print("Abertura sem fechamento")
        return False

    return True

cadeias = ["({[]})", "({[)}]", "({[]}[()]{})"]
print()
for cadeia in cadeias:
    resultado = balanceamento_delimitadores(cadeia)
    print(cadeia)
    print(resultado)
    print()

# Tempo: O(n), percorre o string inteiro somente uma vez.
# Espaço: O(n), porque pode ter apenas aberturas.