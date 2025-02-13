class Tree: 
    def __init__(self, value):
        self.raiz = Node(value)
    
    def __addNode(self, node, newn):
        if newn < node.value:
            if node._left is None:
                node._left = Node(newn)
            else:
                self.__addNode(node._left, newn)
        else:
            if node._right is None:
                node._right = Node(newn)
            else:
                self.__addNode(node._right, newn)

    def addNode(self, newn):
        self.__addNode(self.raiz, newn)

    def postOrden(self, node):
        if node is not None:
            self.postOrden(node._left)
            self.postOrden(node._right)
            print(node.value, end=",")

    def preOrden(self, node):
        if node is not None:
            print(node.value, end=",")
            self.preOrden(node._left)
            self.preOrden(node._right)

    def inOrden(self, node):
        if node is not None:
            self.inOrden(node._left)
            print(node.value, end=",")
            self.inOrden(node._right)
    
    def searchNode(self, node, srN):
        if node is None:
            return None
        if node.value == srN:
            return node
        if node.value > srN:
            self.searchNode(node._left, srN)
        else:
            self.searchNode(node._right, srN)
            

class Node:
    def __init__(self, value):
        self.value = value
        self._left = None
        self._right = None


tree = Tree(10)

while(True):
    print("\n[1]Buscar\n" +"[2]Agregar\n" +"[3]Imprimir\n" +"[4]Borrar arbol\n" +"[5]Terminar\n")
    x = input()
    x= int(x)
    if(x==1):
        print("Ingrese el nodo que quiera agregar")
        srN1 = input()
        srN = int (srN1)
        if tree.searchNode(tree.raiz,srN):
            print("El nodo " + srN1 + " no se encuentra en el arbol")
        if not tree.searchNode(tree.raiz,srN):
            print("El nodo " + srN1 + " si se encuentra en el arbol")
        continue
    elif(x==2):
        print("Ingrese el nodo que quiera agregar")        
        newn = input()
        newn = int (newn)
        tree.addNode(newn)

    elif(x==3):
        print("Arbol impreso POSTORDEN")
        tree.postOrden(tree.raiz)
        print("\nArbol impreso PREORDEN")
        tree.preOrden(tree.raiz)
        print("\nArbol impreso PREORDEN")
        tree.inOrden(tree.raiz)
        continue
    elif(x==4):
        print("Borrar arbol")
        continue
    elif(x==5):
        print("Terminar")
        break

