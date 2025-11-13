import math  # Importamos la librería matemática para raíz y factorial

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

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo.")
    return math.factorial(n)


def raiz_cuadrada(n: float) -> float:
    if n < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(n)


def mostrar_menu():
    print("\n" + "=" * 35)
    print("    🧮 CALCULADORA BÁSICA")
    print("=" * 35)
    print("1️⃣  Sumar")
    print("2️⃣  Restar")
    print("3️⃣  Multiplicar")
    print("4️⃣  Dividir")
    print("5️⃣  Factorial")
    print("6️⃣  Raíz cuadrada")
    print("7️⃣  Salir")
    print("=" * 35)


def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("👉 Elige una opción (1-7): ")

        if opcion == "7":
            print("👋 ¡Gracias por usar la calculadora! Hasta pronto.")
            break

        
        if opcion not in {"1", "2", "3", "4", "5", "6"}:
            print("⚠️  Opción no válida. Intenta de nuevo.")
            continue

        try:
            if opcion in {"1", "2", "3", "4"}:
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

            elif opcion == "5":
                n = int(input("Ingrese un número entero: "))
                resultado = factorial(n)
                print(f"✅ El factorial de {n} es: {resultado}\n")

            elif opcion == "6":
                n = float(input("Ingrese un número: "))
                resultado = raiz_cuadrada(n)
                print(f"✅ La raíz cuadrada de {n} es: {resultado}\n")

            else:
                print("⚠️  Opción no válida. Intenta de nuevo.\n")
    

        except ValueError as e:
            print(f"❌ Error: {e}\n")


if __name__ == "__main__":
    ejecutar_calculadora()
