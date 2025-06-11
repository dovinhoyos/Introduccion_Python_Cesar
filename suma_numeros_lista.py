def sumar_numeros_lista(lista):
    """
    Suma todos los números en una lista de enteros.

    Args:
        lista (list): Una lista de números enteros.

    Returns:
        int: La suma de los números en la lista.
    """
    return sum(lista)


if __name__ == "__main__":
    """
    Programa principal para demostrar el uso de la función `sumar_numeros_lista`.
    Utiliza una lista de ejemplo y muestra la suma total.
    """
    # Lista de numeros enteros
    numeros_enteros = [1, 2, 3, 4, 5]

    # Calcular la suma utilizando la función
    resultado = sumar_numeros_lista(numeros_enteros)

    # Mostrar el resultado
    print(f"La lista de ejemplo es: {numeros_enteros}")
    print(f"La suma de los números en la lista es: {resultado}")

