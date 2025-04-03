"""
Dados dos conjuntos, A y B, 
    a- escribe un programa en Python que imprima los elementos que se encuentran en A o en B, o en ambos.

    b- escribe un programa en Python que imprima los elementos que se encuentran en A y en B

    c- Escribe un programa en Python que imprima el
    conjunto de los elementos que se encuentran en A o en B, pero no en ambos.

    d- Escribe un programa en Python que imprima si un conjunto es un subconjunto de otro conjunto.

    e- escribe un programa en Python que imprima el número de
    elementos del conjunto.

"""

conjunto = {1,2,4,6}
conjunto2 = {1,2,3,4,6,7}

def mostrarLista(Lista):
    print(Lista)

def main():
    # a
    mostrarLista(conjunto)
    mostrarLista(conjunto2)    
    mostrarLista(conjunto | conjunto2)
    # b
    mostrarLista(conjunto & conjunto2)
    # c
    mostrarLista(conjunto.symmetric_difference(conjunto2))
    # d
    mostrarLista(conjunto.issubset(conjunto2))
    # e
    mostrarLista(len(conjunto|conjunto2))
main()