def obtener_nombre():
    """
    Solicita al usuario su nombre y lo valida.
    Returns:
        str: Nombre del usuario con la primera letra en mayúscula.
    """
    while True:
        nombre = input("📝 Por favor, introduce tu nombre: ").strip().capitalize()
        if nombre:
            return nombre
        print("⚠️ El nombre no puede estar vacío. Inténtalo de nuevo.")


def obtener_sexo():
    """
    Solicita al usuario su sexo y lo valida.
    Returns:
        str: Sexo del usuario ('M' para hombre, 'F' para mujer).
    """
    while True:
        sexo = (
            input("⚧ Por favor, introduce tu sexo (M/F para Hombre/Mujer): ")
            .strip()
            .upper()
        )
        if sexo in ["M", "F"]:
            return sexo
        print(
            "❌ Entrada inválida. Por favor, introduce 'M' para hombre o 'F' para mujer."
        )


def determinar_grupo(nombre, sexo):
    """
    Determina el grupo del usuario basado en su nombre y sexo.
    Args:
        nombre (str): Nombre del usuario.
        sexo (str): Sexo del usuario ('M' o 'F').
    Returns:
        str: Grupo asignado ('A' o 'B').
    """
    primera_letra_nombre = nombre[0]
    if sexo == "F":  # Si es mujer
        return "A" if primera_letra_nombre < "M" else "B"
    elif sexo == "M":  # Si es hombre
        return "A" if primera_letra_nombre > "N" else "B"
    return "Indefinido"  # Caso por defecto (no debería ocurrir)


def main():
    """
    Función principal que ejecuta el programa.
    """
    print("👋 ¡Bienvenido al programa de asignación de grupos!")
    nombre = obtener_nombre()
    sexo = obtener_sexo()
    grupo = determinar_grupo(nombre, sexo)
    print(f"🎉 Hola {nombre}, eres del grupo: {grupo}")


# Ejecutar el programa
if __name__ == "__main__":
    main()
