# Mi primera calculadora con funciones en Python :D

# Funciones para cada operación
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("⚠️ Error: no se puede dividir por cero")
        return None

print("=== Calculadora en Python ===")

while True:
    # Menú
    print("\nOpciones:")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "5":
        print("Adiós! 👋")
        break

    # Pedimos los números
    try:
        num1 = float(input("Escribe el primer número: "))
        num2 = float(input("Escribe el segundo número: "))
    except ValueError:
        print("⚠️ Eso no es un número válido")
        continue

    # Usamos las funciones según la opción
    if opcion == "1":
        print("Resultado:", sumar(num1, num2))
    elif opcion == "2":
        print("Resultado:", restar(num1, num2))
    elif opcion == "3":
        print("Resultado:", multiplicar(num1, num2))
    elif opcion == "4":
        resultado = dividir(num1, num2)
        if resultado is not None:
            print("Resultado:", resultado)
    else:
        print("⚠️ Opción incorrecta, prueba otra vez")
