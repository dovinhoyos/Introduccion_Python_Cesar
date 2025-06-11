def solicitar_salario():
    """
    Solicita al usuario el salario mensual en millones de pesos colombianos.
    Valida que la entrada sea un número positivo.
    :return: salario mensual como float
    """
    while True:
        try:
            salario = float(
                input(
                    "💰 Ingrese su salario mensual en millones de pesos colombianos: "
                )
            )
            if salario < 0:
                print("⚠️ El salario no puede ser negativo. Intente de nuevo.")
            else:
                return salario
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingrese un número para el salario.")


def calcular_impuesto(salario):
    """
    Calcula el impuesto a pagar según el salario mensual.
    :param salario: salario mensual en millones de pesos colombianos
    :return: impuesto a pagar como float
    """
    if salario > 30:
        return salario * 0.10  # 10% para salarios de más de 30 millones
    elif salario > 20:
        return salario * 0.08  # 8% para salarios entre 20 y 30 millones
    elif salario > 15:
        return salario * 0.05  # 5% para salarios entre 15 y 20 millones
    elif salario >= 12:
        return salario * 0.03  # 3% para salarios entre 12 y 15 millones
    else:
        return 0  # No hay impuesto para salarios menores a 12 millones


def mostrar_resultado(salario, impuesto):
    """
    Muestra el resultado del cálculo del impuesto al usuario con iconos.
    :param salario: salario mensual en millones de pesos colombianos
    :param impuesto: impuesto calculado
    """
    print(f"📝 Su salario mensual es de {salario:,.2f} millones de pesos.")
    if impuesto > 0:
        print(f"💸 El impuesto a pagar es de {impuesto:,.2f} millones de pesos.")
    else:
        print("🎉 Según la tabla, no tiene que pagar impuesto.")


def main():
    """
    Función principal que coordina la solicitud de salario, cálculo y presentación del impuesto.
    """
    salario = solicitar_salario()
    impuesto = calcular_impuesto(salario)
    mostrar_resultado(salario, impuesto)


if __name__ == "__main__":
    main()
