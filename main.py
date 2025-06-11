from car import Carro
from book import Libro

if __name__ == "__main__":
    my_carro = Carro("ABC-123", "Toyota", 2020, "Rojo")
    my_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 471)
    print(
        f"Carro: Placa={my_carro.get_placa()}, Marca={my_carro.get_marca()}, Modelo={my_carro.get_modelo()}, Color={my_carro.get_color()}"
    )
    print(
        f"Libro: Título={my_libro.get_titulo()}, Autor={my_libro.get_autor()}, Páginas={my_libro.get_numeroPaginas()}"
    )

