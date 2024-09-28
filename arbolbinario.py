class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def insertar_en_bst(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    if valor < raiz.valor:
        raiz.izquierdo = insertar_en_bst(raiz.izquierdo, valor)
    else:
        raiz.derecho = insertar_en_bst(raiz.derecho, valor)
    return raiz

def lista_a_bst(lista):
    raiz = None
    for valor in lista:
        raiz = insertar_en_bst(raiz, valor)
    return raiz

def imprimir_bst(raiz):
    if raiz is not None:
        imprimir_bst(raiz.izquierdo)
        print(raiz.valor, end=' ')
        imprimir_bst(raiz.derecho)

# Definición de la lista de elementos
lista = [55, 77, 33, 44, 11, 22, 1,6,7,85,64,13,123,67,99,0,1]

# Convertir la lista en un árbol binario de búsqueda
arbol = lista_a_bst(lista)

# Imprimir el árbol binario de búsqueda en orden
imprimir_bst(arbol)