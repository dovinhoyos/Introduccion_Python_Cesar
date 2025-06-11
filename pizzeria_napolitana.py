# Pizzería Napolitana


def mostrar_menu():
    """
    Muestra las opciones principales del menú de la pizzería.

    Esta función imprime las opciones disponibles para que el usuario elija
    entre una pizza vegetariana o no vegetariana.
    """
    print("Bienvenido a la pizzería Napolitana de Neiva 🍕")
    print("¿Deseás una pizza vegetariana o no vegetariana?")
    print("1. Vegetariana")
    print("2. No vegetariana")


def obtener_opcion_usuario():
    """
    Solicita al usuario que elija entre las opciones principales.

    Returns:
        int: Retorna 1 si el usuario elige vegetariana, 2 si elige no vegetariana.
        None: Retorna None si la entrada no es válida.
    """
    opcion = input("Elegí 1 o 2: ").strip()
    if opcion not in ["1", "2"]:
        print("Opción no válida. Salimos.")
        return None
    return int(opcion)


def obtener_ingrediente(ingredientes_disponibles):
    """
    Muestra al usuario los ingredientes disponibles y solicita seleccionar uno.

    Args:
        ingredientes_disponibles (list): Una lista de ingredientes adicionales disponibles.

    Returns:
        str: El ingrediente seleccionado por el usuario.
        None: Retorna None si la entrada no es válida.
    """
    print("Estos son los ingredientes disponibles:")
    for i, ingrediente in enumerate(ingredientes_disponibles, start=1):
        print(f"{i}. {ingrediente}")

    seleccion = input("Elegí el número de ingrediente que querés agregar: ").strip()
    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(ingredientes_disponibles):
            return ingredientes_disponibles[seleccion - 1]
        else:
            print("Opción no válida. Salimos.")
            return None
    except ValueError:
        print("Entrada inválida. Salimos.")
        return None


def preparar_pizza(tipo_pizza, ingredientes_base, ingrediente_adicional):
    """
    Muestra el resumen final de la pizza preparada.

    Args:
        tipo_pizza (str): Tipo de pizza seleccionada (vegetariana o no vegetariana).
        ingredientes_base (list): Ingredientes base comunes para todas las pizzas.
        ingrediente_adicional (str): Ingrediente adicional elegido.

    Returns:
        None
    """
    ingredientes_finales = ingredientes_base + [ingrediente_adicional]
    print("\n¡Tu pizza está lista!")
    print(f"Tipo de pizza: {tipo_pizza}")
    print("Ingredientes:", ", ".join(ingredientes_finales))


def main():
    """
    Función principal que maneja el flujo del programa de la pizzería.

    Controla el menú inicial, la selección de tipo de pizza, los ingredientes,
    y finalmente muestra el resumen de la pizza preparada.

    Returns:
        None
    """
    mostrar_menu()
    opcion = obtener_opcion_usuario()
    if opcion is None:
        return

    # Ingredientes base comunes
    ingredientes_base = ["mozzarella", "tomate"]

    # Definición de ingredientes adicionales por tipo
    ingredientes = {
        "vegetariana": ["pimiento", "tofu"],
        "no vegetariana": ["peperoni", "jamón", "salmón"],
    }

    # Determinar tipo de pizza e ingredientes disponibles
    tipo_pizza = "vegetariana" if opcion == 1 else "no vegetariana"
    ingredientes_disponibles = ingredientes[tipo_pizza]

    print(f"\nHas elegido una pizza {tipo_pizza}.")
    ingrediente_adicional = obtener_ingrediente(ingredientes_disponibles)

    if ingrediente_adicional is None:
        return

    preparar_pizza(tipo_pizza, ingredientes_base, ingrediente_adicional)


if __name__ == "__main__":
    main()

