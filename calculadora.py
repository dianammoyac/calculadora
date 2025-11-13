def sumar(a: float, b: float) -> float:
    return a + b

def restar(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b


def mostrar_menu():
    print("\n" + "=" * 30)
    print("    🧮 CALCULADORA BÁSICA")
    print("=" * 30)
    print("1️⃣  Sumar")
    print("2️⃣  Restar")
    print("3️⃣  Multiplicar")
    print("4️⃣  Dividir")
    print("5️⃣  Salir")
    print("=" * 30)


def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("👉 Elige una opción (1-5): ")

        if opcion == "5":
            print("👋 ¡Gracias por usar la calculadora! Hasta pronto.")
            break

        if opcion not in {"1", "2", "3", "4"}:
            print("⚠️  Opción no válida. Intenta de nuevo.")
            continue

        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))

            if opcion == "1":
                resultado = sumar(a, b)
                operacion = "suma"
            elif opcion == "2":
                resultado = restar(a, b)
                operacion = "resta"
            elif opcion == "3":
                resultado = multiplicar(a, b)
                operacion = "multiplicación"
            elif opcion == "4":
                resultado = dividir(a, b)
                operacion = "división"

            print(f"✅ El resultado de la {operacion} es: {resultado}\n")

        except ValueError as e:
            print(f"❌ Error: {e}\n")


if __name__ == "__main__":
    ejecutar_calculadora()
