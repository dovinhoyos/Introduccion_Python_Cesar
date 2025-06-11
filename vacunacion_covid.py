def determinar_fase(edad):
    """
    Determina la fase de vacunación contra el COVID-19 según la edad.

    Args:
        edad (int): La edad de la persona.

    Returns:
        str: La fase asignada según la edad.
    """
    if edad >= 80:
        return "Fase 1"
    elif 70 <= edad < 80:
        return "Fase 2"
    elif 60 <= edad < 70:
        return "Fase 3"
    elif 30 <= edad < 60:
        return "Fase 4"
    elif 18 <= edad < 30:
        return "Fase 5"
    else:
        return "En espera de Autorización"


def main():
    """
    Función principal que maneja el flujo del sistema de vacunación contra el COVID-19.

    Solicita la edad de 5 personas, determina su fase de vacunación y muestra el resultado.

    Returns:
        None
    """
    print("Bienvenido al sistema de vacunación contra el COVID-19 💉")

    for i in range(1, 6):
        while True:
            try:
                edad = int(input(f"\nIngresá la edad de la persona {i}: "))
                if edad < 0:
                    print("La edad no puede ser negativa. Intentá de nuevo.")
                    continue
                break
            except ValueError:
                print("Por favor, ingresá un número válido.")

        fase = determinar_fase(edad)
        print(f"La persona {i} está asignada a: {fase}")


if __name__ == "__main__":
    main()

