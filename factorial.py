def factorial(n):
    """
    Calcula el factorial de un número de forma recursiva.

    Args:
        n (int): El número entero para el cual se calculará el factorial.

    Returns:
        int: El factorial del número dado.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    """
    Función principal que solicita al usuario un número entero y calcula su factorial.

    Solicita al usuario que ingrese un número entero no negativo, calcula su factorial
    utilizando la función `factorial`, y muestra el resultado.

    Returns:
        None
    """
    while True:
        try:
            numero = int(input("Ingresá un número entero para calcular su factorial: "))
            if numero < 0:
                print(
                    "El factorial no está definido para números negativos. Probá de nuevo."
                )
                continue
            resultado = factorial(numero)
            print(f"El factorial de {numero} es: {resultado}")
            break
        except ValueError:
            print("Por favor, ingresá un número entero válido.")


if __name__ == "__main__":
    main()

