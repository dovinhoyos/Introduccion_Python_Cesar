import random


def main():
    # Inicializar lista con 10 números aleatorios entre 1 y 100
    lista_numeros = [random.randint(1, 100) for _ in range(10)]
    print("Lista generada:")
    print(lista_numeros)

    # Ordenar la lista de menor a mayor
    lista_numeros.sort()
    print("\nLista ordenada de menor a mayor:")
    print(lista_numeros)


if __name__ == "__main__":
    main()
