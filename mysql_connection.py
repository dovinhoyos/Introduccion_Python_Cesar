# Importar librería para conectarnos a bases de datos MySQL
import pymysql as mysql
from typing import Optional

# Credenciales para la conexión
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "mymacosroot",
    "database": "productospy",
}


def crear_conexion() -> Optional[mysql.connections.Connection]:
    """
    Crear la conexión a la base de datos.

    Retorna una conexión abierta o None si ocurre un error.
    """
    try:
        conexion = mysql.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"],
        )
        return conexion
    except mysql.MySQLError as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None


def agregar_producto(producto: tuple[int, str, int, str]) -> None:
    """
    Agregar un producto a la base de datos.

    :param producto: Una tupla que contiene los datos del producto (proCodigo, proNombre, proPrecio, ProCategoria).
    """
    conexion = crear_conexion()
    if not conexion:
        return

    cursor = None
    try:
        # Crear objeto cursor
        cursor = conexion.cursor()

        # Consulta de inserción actualizada
        consulta = (
            "INSERT INTO productos (proCodigo, proNombre, proPrecio, ProCategoria) "
            "VALUES (%s, %s, %s, %s)"
        )
        cursor.execute(consulta, producto)
        conexion.commit()

        if cursor.rowcount == 1:
            print("Producto agregado correctamente")

    except mysql.MySQLError as e:
        conexion.rollback()
        print(f"Error al intentar agregar el producto: {e}")

    finally:
        # Cerrando cursor y conexión
        if cursor:
            cursor.close()
        conexion.close()


# Ejecución de prueba
if __name__ == "__main__":
    producto = (17, "Refrigerador", 4500000, "Electrodomestico")
    agregar_producto(producto)
