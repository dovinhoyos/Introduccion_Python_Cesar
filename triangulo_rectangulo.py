def es_triangulo(a, b, c):
    """
    Verifica si tres lados pueden formar un triángulo.

    Args:
        a (float): Longitud del primer lado.
        b (float): Longitud del segundo lado.
        c (float): Longitud del tercer lado.

    Returns:
        bool: True si pueden formar un triángulo, False en caso contrario.
    """
    return (a + b > c) and (a + c > b) and (b + c > a)


def es_triangulo_rectangulo(a, b, c):
    """
    Verifica si un triángulo es rectángulo utilizando el teorema de Pitágoras.

    Args:
        a (float): Longitud del primer lado.
        b (float): Longitud del segundo lado.
        c (float): Longitud del tercer lado.

    Returns:
        bool: True si es un triángulo rectángulo, False en caso contrario.
    """
    # Ordenar los lados para garantizar que el mayor sea la hipotenusa
    lados = sorted([a, b, c])
    hipotenusa = lados[2]
    cateto1 = lados[0]
    cateto2 = lados[1]

    # Comprobación con tolerancia por redondeo
    return abs(hipotenusa**2 - (cateto1**2 + cateto2**2)) < 1e-6


def main():
    """
    Programa principal para verificar triángulos y determinar si son rectángulos.

    Solicita al usuario las longitudes de tres lados, valida si pueden formar un triángulo
    y verifica si el triángulo es rectángulo.

    Returns:
        None
    """
    print("Verificación de triángulos 🧐")

    try:
        # Solicitar al usuario las longitudes de los lados
        lado1 = float(input("Ingresá la longitud del lado 1: "))
        lado2 = float(input("Ingresá la longitud del lado 2: "))
        lado3 = float(input("Ingresá la longitud del lado 3: "))

        # Verificar si se puede formar un triángulo
        if es_triangulo(lado1, lado2, lado3):
            print("¡Se puede formar un triángulo con esos lados!")
            # Verificar si el triángulo es rectángulo
            if es_triangulo_rectangulo(lado1, lado2, lado3):
                print("Además, es un triángulo rectángulo. 🔺")
            else:
                print("Pero no es un triángulo rectángulo. 🔻")
        else:
            print("No se puede formar un triángulo con esos lados. ❌")
    except ValueError:
        print("Por favor, ingresá valores numéricos válidos.")


if __name__ == "__main__":
    main()

