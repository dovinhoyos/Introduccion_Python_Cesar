def contar_palabra_en_texto(texto, palabra):
    """
    Cuenta cuántas veces aparece una palabra específica en un texto dado.

    Args:
        texto (str): El texto en el cual buscar.
        palabra (str): La palabra que se desea contar.

    Returns:
        int: El número de veces que la palabra aparece en el texto, ignorando signos de puntuación y mayúsculas/minúsculas.
    """
    # Dividir el texto en palabras usando espacios como delimitador
    palabras = texto.split()

    # Contar cuántas palabras coinciden después de limpiar signos de puntuación y normalizar a minúsculas
    contador = sum(
        1 for p in palabras if p.strip('.,;:!?"()[]{}').lower() == palabra.lower()
    )
    return contador


# Ejemplo de uso:
if __name__ == "__main__":
    """
    Ejemplo de uso interactivo del contador de palabras en un texto.
    Solicita al usuario el texto y la palabra a buscar, y muestra el resultado del conteo.
    """
    # Texto de ejemplo utilizado para la búsqueda
    texto_ejemplo = "Hola, ¿cómo estás? Espero que estés bien. Bienvenido a esta sesión y que la pases bien."

    # Palabra que se desea buscar en el texto anterior
    palabra_a_buscar = "bien"

    # Llamar a la función contar_palabra_en_texto para obtener el número de ocurrencias
    resultado = contar_palabra_en_texto(texto_ejemplo, palabra_a_buscar)

    # Mostrar el resultado al usuario
    print(f"La palabra '{palabra_a_buscar}' aparece {resultado} vez/veces en el texto.")

