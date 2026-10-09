def sumar(a, b):
    return a + b


def main():
    print("Calculadora simple")
    num1 = float(input("Escribe el primer número: "))
    num2 = float(input("Escribe el segundo número: "))

    resultado = sumar(num1, num2)
    print(f"La suma es: {resultado}")


if __name__ == "__main__":
    main()