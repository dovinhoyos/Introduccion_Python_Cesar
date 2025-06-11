def calcular_precio_entrada(edad):
    """
    Calcula el precio de entrada según la edad del cliente.

    Parámetros:
        edad (int): La edad del cliente.

    Retorna:
        str: Mensaje con el precio de la entrada.
    """
    if edad < 5:
        return "🎉 La entrada es gratuita. ¡Disfruta! 🎈"
    elif 5 <= edad <= 18:
        return "💵 El precio de la entrada es 5,000 pesos. 🎮"
    else:
        return "💰 El precio de la entrada es 10,000 pesos. 🕹️"


def main():
    """
    Función principal que solicita la edad del cliente y muestra el precio de la entrada.
    """
    try:
        edad = int(input("🔢 Por favor, ingrese la edad del cliente: "))
        mensaje = calcular_precio_entrada(edad)
        print(mensaje)
    except ValueError:
        print("⚠️ Error: Por favor, ingrese un número válido para la edad.")


if __name__ == "__main__":
    main()
