# Clase N° 2: Fundamentos de Python - Parte 1



## Objetivos de Aprendizaje

- **Repasar los conceptos fundamentales** 
Aprenderás sobre variables, tipos de datos y operadores que constituyen la base de cualquier programa en Python.

- **Dominar estructuras de control** 
Entenderás cómo controlar el flujo de ejecución mediante condicionales y bucles para crear programas dinámicos.

- **Crear programas básicos** 
Aplicarás estos conocimientos para desarrollar una calculadora simple y resolver ejercicios prácticos que reforzarán tu aprendizaje.

- **Prepararte para automatización** 
Establecerás las bases necesarias para, en futuras clases, aplicar estos conocimientos en contextos de automatización de pruebas.

---

## Fundamentos de Python

Python es uno de los lenguajes más populares para automatización y desarrollo debido a su simplicidad sintáctica y potentes capacidades.  
Durante esta clase, aprenderemos desde los conceptos más básicos como variables y tipos de datos, hasta estructuras de control más complejas que nos permitirán crear nuestros primeros programas funcionales.

Al finalizar esta sesión, tendrás los conocimientos necesarios para comprender cómo Python procesa datos y cómo puedes utilizarlo para resolver problemas computacionales simples.

---

## ¿Por qué Python?

### Ventajas clave
- Sintaxis clara y legible, similar al inglés cotidiano  
- Inmensa comunidad de desarrolladores  
- Amplia biblioteca estándar ("baterías incluidas")  
- Facilidad para instalar paquetes externos (pip)  
- Lenguaje común entre testers, desarrolladores y científicos de datos  

---

## Variables y tipos de datos

### Comentarios en el código
Son notas que el intérprete ignora.  

Tipos:  

```
# Comentario de una sola línea

'''
Comentario
de múltiples
líneas
'''

"""
También se pueden usar
comillas dobles
para comentarios multilínea
"""

x = 10  # Comentario al final de una línea
```

### Variables y Tipos de Datos
En Python no es necesario declarar el tipo.  

Tipos básicos: `int`, `float`, `str`, `bool`.

```
nombre = "Matías"
edad = 30
altura = 1.75
es_automation_tester = True
```

---

## Operadores

### Operador de asignación
```
# Asignación simple
x = 10
y = "Automation Tester"

# Asignación múltiple
a, b, c = 1, 2, 3

# Asignación con operación
contador = 0
contador = contador + 1  # O simplificado:
contador += 1
```

### Operadores aritméticos

| Operador | Descripción | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| + | Suma | 5 + 3 | 8 |
| - | Resta | 10 - 4 | 6 |
| * | Multiplicación | 2 * 6 | 12 |
| / | División | 8 / 2 | 4.0 |
| % | Módulo | 9 % 2 | 1 |
| ** | Potencia | 3 ** 2 | 9 |
| // | División entera | 7 // 2 | 3 |

---

## Entrada y Salida

Modelo **E/P/S**: Entrada → Procesamiento → Salida.  

```
# Ejemplo de entrada, procesamiento y salida
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))

# Procesamiento
años_para_jubilacion = 65 - edad

# Salida
print(f"Hola {nombre}, te faltan {años_para_jubilacion} años para jubilarte.")
```

---

## Conversión de tipos

Funciones: `int()`, `float()`, `str()`, `bool()`

```
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros: "))
es_numero = "123".isdigit()  # Devuelve True
```

---

## Condicionales

```
edad = int(input("¿Cuál es tu edad? "))

if edad >= 18:
    print("Eres mayor de edad. Puedes trabajar en TalentoLab.")
elif edad >= 16:
    print("Podrías realizar una pasantía en TalentoLab.")
else:
    print("Eres demasiado joven para trabajar aquí.")
```

---

## Bucles

### For
```
for i in range(5):
    print(i)

for letra in "Python":
    print(letra)
```

### While
```
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

---

## Contadores y Acumuladores

```
# Contar números pares del 1 al 10
contador = 0
for i in range(1, 11):
    if i % 2 == 0:
        contador += 1
print(f"Hay {contador} números pares")

# Suma y promedio
suma = 0
for i in range(1, 11):
    suma += i
print(f"La suma es: {suma}")
print(f"El promedio es: {suma / 10}")
```

---

## Break y Continue

```
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

# Encontrar el primer divisible por 7
for num in range(1, 101):
    if num % 7 == 0:
        print(f"El primer divisible por 7 es: {num}")
        break
```

---

## Calculadora Básica en Python

```
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Elige (+, -, *, /): ")

if operacion == "+":
    print(f"Resultado: {num1 + num2}")
elif operacion == "-":
    print(f"Resultado: {num1 - num2}")
elif operacion == "*":
    print(f"Resultado: {num1 * num2}")
elif operacion == "/":
    if num2 != 0:
        print(f"Resultado: {num1 / num2}")
    else:
        print("Error: división por cero")
else:
    print("Operación no válida")
```

---


