def separar_y_ordenar_numeros(numeros):
    """
    Divide una lista de enteros en dos listas: números pares e impares, y las ordena.

    Args:
        numeros (list): Una lista de números enteros.

    Returns:
        tuple: Una tupla que contiene dos listas, la primera con números pares y la segunda con números impares, ambas ordenadas.
    """
    pares = sorted([num for num in numeros if num % 2 == 0])
    impares = sorted([num for num in numeros if num % 2 != 0])
    return pares, impares


if __name__ == "__main__":
    """
    Programa principal para demostrar el uso de la función `separar_y_ordenar_numeros`.
    Solicita al usuario ingresar una lista de enteros y muestra las listas ordenadas de pares e impares.
    """
    # Solicitar al usuario ingresar una lista de números
    entrada_usuario = input(
        "Ingrese una lista de números enteros separados por comas: "
    )

    # Convertir la entrada en una lista de números enteros
    numeros = [int(num.strip()) for num in entrada_usuario.split(",")]

    # Separar y ordenar los números en listas de pares e impares
    pares, impares = separar_y_ordenar_numeros(numeros)

    # Mostrar los resultados
    print(f"Números pares ordenados: {pares}")
    print(f"Números impares ordenados: {impares}")

