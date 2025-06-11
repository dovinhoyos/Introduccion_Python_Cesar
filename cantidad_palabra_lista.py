def contar_palabra_en_lista(lista, palabra):
    """Cuenta cuántas veces aparece una palabra en una lista."""
    return lista.count(palabra)


# Lista de palabras
lista_palabras = ["manzana", "pera", "manzana", "durazno", "uva", "manzana", "pera"]

# Mostrar la lista al usuario
print("Lista de palabras:", lista_palabras)

# Pedir una palabra para buscar en la lista
dato_ingresado = input("Ingrese la palabra que desea buscar en la lista: ")

# Convertir la palabra ingresada a minúscula
palabra_a_buscar = dato_ingresado.lower()

# Contar cuántas veces aparece la palabra en la lista
cantidad_apariciones = contar_palabra_en_lista(lista_palabras, palabra_a_buscar)

print(
    f"La palabra '{palabra_a_buscar}' aparece {cantidad_apariciones} veces en la lista."
)

