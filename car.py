class Carro:
    """
    Representa un objeto Carro con atributos como placa, marca, modelo y color.
    """

    def __init__(self, placa: str, marca: str, modelo: int, color: str):
        """
        Constructor de la clase Carro.

        Args:
            placa (str): La placa del carro.
            marca (str): La marca del carro.
            modelo (int): El año del modelo del carro.
            color (str): El color del carro.
        """
        self.__placa = placa  # Atributo privado
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo  # Atributo privado
        self.__color = color  # Atributo privado

    # Métodos getter
    def get_placa(self) -> str:
        return self.__placa

    def get_marca(self) -> str:
        return self.__marca

    def get_modelo(self) -> int:
        return self.__modelo

    def get_color(self) -> str:
        return self.__color

    # Métodos setter
    def set_placa(self, placa: str) -> None:
        self.__placa = placa

    def set_marca(self, marca: str) -> None:
        self.__marca = marca

    def set_modelo(self, modelo: int) -> None:
        self.__modelo = modelo

    def set_color(self, color: str) -> None:
        self.__color = color
