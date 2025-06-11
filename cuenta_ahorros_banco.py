import datetime


def crear_cuenta(cuentas, consecutivo):
    """
    Crea una nueva cuenta bancaria y la agrega a la lista de cuentas.

    Args:
        cuentas (list): Lista actual de cuentas.
        consecutivo (int): Número único consecutivo para generar el código de la cuenta.

    Returns:
        int: El nuevo valor del consecutivo para la siguiente cuenta.
    """
    año = datetime.date.today().year
    codigo_cuenta = f"{año}-{consecutivo}"
    consecutivo += 1

    identificacion = input("👤 Identificación del cliente: ")
    nombre = input("📝 Nombre completo: ")
    correo = input("📧 Correo electrónico: ")

    cuenta = {
        "codigo": codigo_cuenta,
        "fecha_creacion": datetime.date.today(),
        "saldo": 0.0,
        "cliente": {
            "identificacion": identificacion,
            "nombre": nombre,
            "correo": correo,
        },
    }
    cuentas.append(cuenta)
    print(f"✅ Cuenta creada con éxito. Código de cuenta: {codigo_cuenta}")

    return consecutivo


def realizar_consignacion(cuentas):
    """
    Permite realizar una consignación en una cuenta bancaria existente.

    Args:
        cuentas (list): Lista actual de cuentas.

    Returns:
        None
    """
    codigo = input("🔍 Ingrese el código de la cuenta a consignar: ")
    cuenta = next((c for c in cuentas if c["codigo"] == codigo), None)
    if cuenta:
        monto = float(input("💵 Ingrese el monto a consignar: "))
        cuenta["saldo"] += monto
        print(f"✅ Consignación exitosa. Saldo actual: {cuenta['saldo']:.2f}")
    else:
        print("❌ Cuenta no encontrada.")


def realizar_retiro(cuentas):
    """
    Permite realizar un retiro de una cuenta bancaria existente.

    Args:
        cuentas (list): Lista actual de cuentas.

    Returns:
        None
    """
    codigo = input("🔍 Ingrese el código de la cuenta a retirar: ")
    cuenta = next((c for c in cuentas if c["codigo"] == codigo), None)
    if cuenta:
        monto = float(input("💸 Ingrese el monto a retirar: "))
        if monto <= cuenta["saldo"]:
            cuenta["saldo"] -= monto
            print(f"✅ Retiro exitoso. Saldo actual: {cuenta['saldo']:.2f}")
        else:
            print("⚠️ Saldo insuficiente.")
    else:
        print("❌ Cuenta no encontrada.")


def consultar_cuenta_por_codigo(cuentas):
    """
    Consulta los detalles de una cuenta bancaria específica por su código.

    Args:
        cuentas (list): Lista actual de cuentas.

    Returns:
        None
    """
    codigo = input("🔍 Ingrese el código de la cuenta a consultar: ")
    cuenta = next((c for c in cuentas if c["codigo"] == codigo), None)
    if cuenta:
        print(f"📄 Código: {cuenta['codigo']}")
        print(f"📅 Fecha de creación: {cuenta['fecha_creacion']}")
        print(f"💰 Saldo: {cuenta['saldo']:.2f}")
        print(
            f"👤 Cliente: {cuenta['cliente']['nombre']} ({cuenta['cliente']['identificacion']})"
        )
    else:
        print("❌ Cuenta no encontrada.")


def consultar_cuentas_por_cliente(cuentas):
    """
    Consulta todas las cuentas asociadas a una identificación de cliente especificada.

    Args:
        cuentas (list): Lista actual de cuentas.

    Returns:
        None
    """
    identificacion = input("👤 Ingrese la identificación del cliente: ")
    cuentas_cliente = [
        c for c in cuentas if c["cliente"]["identificacion"] == identificacion
    ]
    if cuentas_cliente:
        for cuenta in cuentas_cliente:
            print(f"📄 Código: {cuenta['codigo']}, 💰 Saldo: {cuenta['saldo']:.2f}")
    else:
        print("❌ No se encontraron cuentas para el cliente.")


def listar_cuentas(cuentas):
    """
    Muestra un listado de todas las cuentas registradas.

    Args:
        cuentas (list): Lista actual de cuentas.

    Returns:
        None
    """
    if cuentas:
        for cuenta in cuentas:
            print(
                f"📄 Código: {cuenta['codigo']}, 👤 Cliente: {cuenta['cliente']['nombre']}, 💰 Saldo: {cuenta['saldo']:.2f}"
            )
    else:
        print("❌ No hay cuentas registradas.")


def main():
    """
    Menú principal del sistema de gestión de cuentas bancarias.

    Returns:
        None
    """
    cuentas = []
    consecutivo = 1

    while True:
        print("\n🏦 MENÚ BANCO ADSO 2923603 🏦")
        print("1️⃣ Crear Cuenta")
        print("2️⃣ Consignar Cuenta")
        print("3️⃣ Retirar Cuenta")
        print("4️⃣ Consultar Cuenta Por Código")
        print("5️⃣ Consultar Cuenta por Identificación Cliente")
        print("6️⃣ Listar Cuentas")
        print("7️⃣ Salir")

        opcion = input("👉 Ingrese Opción (1-7): ")

        if opcion == "1":
            consecutivo = crear_cuenta(cuentas, consecutivo)
        elif opcion == "2":
            realizar_consignacion(cuentas)
        elif opcion == "3":
            realizar_retiro(cuentas)
        elif opcion == "4":
            consultar_cuenta_por_codigo(cuentas)
        elif opcion == "5":
            consultar_cuentas_por_cliente(cuentas)
        elif opcion == "6":
            listar_cuentas(cuentas)
        elif opcion == "7":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Por favor, ingrese un número entre 1 y 7.")


if __name__ == "__main__":
    main()

