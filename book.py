# book.py
class Libro:
    """
    Representa un objeto Libro con atributos como titulo, autor y numeroPaginas.
    """

    def __init__(self, titulo: str, autor: str, numeroPaginas: int):
        """
        Constructor de la clase Libro.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            numeroPaginas (int): El número de páginas del libro.
        """
        self.__titulo = titulo  # Atributo privado
        self.__autor = autor  # Atributo privado
        self.__numeroPaginas = numeroPaginas  # Atributo privado

    # Métodos getter
    def get_titulo(self) -> str:
        return self.__titulo

    def get_autor(self) -> str:
        return self.__autor

    def get_numeroPaginas(self) -> int:
        return self.__numeroPaginas

    # Métodos setter
    def set_titulo(self, titulo: str) -> None:
        self.__titulo = titulo

    def set_autor(self, autor: str) -> None:
        self.__autor = autor

    def set_numeroPaginas(self, numeroPaginas: int) -> None:
        self.__numeroPaginas = numeroPaginas
