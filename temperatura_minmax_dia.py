def registrar_temperaturas(dias):
    """
    Registra las temperaturas mínimas y máximas para cada día de la semana.

    Args:
        dias (list): Lista de días de la semana.

    Returns:
        dict: Un diccionario con las temperaturas mínimas y máximas por día.
    """
    temperaturas = {}
    for dia in dias:
        print(f"Ingrese las temperaturas para {dia}:")
        temp_min = float(input("Temperatura mínima: "))
        temp_max = float(input("Temperatura máxima: "))
        temperaturas[dia] = {"min": temp_min, "max": temp_max}
    return temperaturas


def mostrar_temperatura_media(temperaturas, dias):
    """
    Calcula y muestra la temperatura media de cada día.

    Args:
        temperaturas (dict): Diccionario con las temperaturas mínimas y máximas por día.
        dias (list): Lista de días de la semana.

    Returns:
        None
    """
    print("\nTemperatura media de cada día:")
    for dia in dias:
        temp_media = (temperaturas[dia]["min"] + temperaturas[dia]["max"]) / 2
        print(f"  {dia}: {temp_media:.2f}°C")


def mostrar_dias_temp_minima(temperaturas, dias):
    """
    Encuentra y muestra los días con la temperatura mínima más baja.

    Args:
        temperaturas (dict): Diccionario con las temperaturas mínimas y máximas por día.
        dias (list): Lista de días de la semana.

    Returns:
        None
    """
    temp_min_global = min(temperaturas[dia]["min"] for dia in dias)
    dias_temp_min = [dia for dia in dias if temperaturas[dia]["min"] == temp_min_global]

    print(
        f"\nEl/los día(s) con la temperatura mínima más baja ({temp_min_global}°C) son:"
    )
    for dia in dias_temp_min:
        print(f"  {dia}")


def buscar_dias_por_temp_maxima(temperaturas, dias):
    """
    Solicita una temperatura máxima y muestra los días que coinciden con esa temperatura.

    Args:
        temperaturas (dict): Diccionario con las temperaturas mínimas y máximas por día.
        dias (list): Lista de días de la semana.

    Returns:
        None
    """
    temp_max_input = float(
        input("\nIngrese una temperatura máxima para buscar días con esa temperatura: ")
    )
    dias_temp_max = [dia for dia in dias if temperaturas[dia]["max"] == temp_max_input]

    if dias_temp_max:
        print(f"\nDía(s) cuya temperatura máxima coincide con {temp_max_input}°C:")
        for dia in dias_temp_max:
            print(f"  {dia}")
    else:
        print(
            f"\nNo existe ningún día con una temperatura máxima de {temp_max_input}°C."
        )


def main():
    """
    Programa principal para gestionar temperaturas mínimas, máximas y medias de la semana.

    Returns:
        None
    """
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = registrar_temperaturas(dias)
    mostrar_temperatura_media(temperaturas, dias)
    mostrar_dias_temp_minima(temperaturas, dias)
    buscar_dias_por_temp_maxima(temperaturas, dias)


if __name__ == "__main__":
    main()

