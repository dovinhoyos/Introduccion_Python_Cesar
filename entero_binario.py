def convertir_a_binario(numero):
    """Convierte un número entero a su representación binaria."""
    return bin(numero)[
        2:
    ]  # bin() genera una cadena con el prefijo '0b', se elimina con [2:]


# Solicitar al usuario un número entero
numero = int(input("Ingrese un número entero: "))

# Llamar a la función para obtener la representación binaria
binario = convertir_a_binario(numero)

print(f"La representación binaria de {numero} es: {binario}")

