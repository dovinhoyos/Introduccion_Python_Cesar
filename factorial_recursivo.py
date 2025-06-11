def factorial_recursivo(n):
    """
    Calcula el factorial de un número de forma recursiva.

    Args:
        n (int): El número entero del cual se desea calcular el factorial (n >= 0).

    Returns:
        int: El factorial del número dado.

    Raises:
        ValueError: Si el número proporcionado es negativo.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)


if __name__ == "__main__":
    """
    Programa principal para calcular el factorial de un número usando una función recursiva.
    Solicita al usuario un número entero no negativo y muestra el resultado.
    """
    try:
        # Solicitar al usuario un número entero.
        numero = int(
            input("Ingrese un número entero no negativo para calcular su factorial: ")
        )

        # Calcular el factorial utilizando la función recursiva.
        resultado = factorial_recursivo(numero)

        # Mostrar el resultado en pantalla.
        print(f"El factorial de {numero} es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")

