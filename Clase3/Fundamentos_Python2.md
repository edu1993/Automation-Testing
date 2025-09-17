# Clase N° 3 - Fundamentos de Python Parte 2 y Control de Versiones

## Índice

### Fundamentos de Python - Parte 1
- Variables y tipos de datos simples
- Operador de asignación
- Operadores aritméticos, relacionales y lógicos
- Entrada/Salida básica (**print()**, **input()**)
- Conversión entre tipos de datos simples
- Programas con entrada, procesamiento y salida de datos
- Comentarios en el código
- Estructuras de control
- Calculadora básica en Python (programación lineal)

### Fundamentos de Python Parte 2 - Control de Versiones
- Estructuras de datos
- Funciones
- Manejo de excepciones
- Introducción a Git y GitHub

### Introducción a Pytest y Automatización Básica
- Instalación de Pytest y preparación del proyecto
- Creación de casos de prueba
- Decoradores y aserciones
- Fixtures: qué son, para qué sirven y variantes
- Parametrización y markers personalizados
- Reporte HTML nativo

## Objetivos de la Clase

### Programación Modular
Comprender la diferencia entre programación lineal y modular mediante funciones.

### Refactorización
Refactorizar un script de calculadora en un diseño basado en funciones.

### Manejo de Errores
Implementar manejo de errores con excepciones controladas.

### Control de Versiones
Conocer y aplicar el flujo de trabajo básico de Git y las prácticas colaborativas en GitHub.

## Estructuras de datos en Python

Las estructuras de datos son fundamentales en cualquier lenguaje de programación, ya que permiten organizar y manipular información de manera eficiente. En Python, existen estructuras nativas muy versátiles que se adaptan a distintos tipos de problemas.

### Listas
Colecciones ordenadas y modificables. Permiten elementos duplicados y diferentes tipos de datos.
- Se definen con corchetes **[]**
- Acceso por índice (desde 0)
- Métodos: **append()**, **remove()**, **sort()**

### Tuplas
Colecciones ordenadas e inmutables. Útiles para datos que no deben cambiar.
- Se definen con paréntesis **()**
- No se pueden modificar después de creadas
- Más rápidas que las listas

### Diccionarios
Colecciones no ordenadas de pares clave-valor. Ideales para representar datos estructurados.
- Se definen con llaves **{}**
- Acceso por clave en lugar de índice
- Métodos: **keys()**, **values()**, **items()**

#### Ejemplo de diccionario
**persona = {"nombre": "Ana", "edad": 30, "país": "Argentina"}**  
**print(persona["nombre"])  # Ana**  
**persona["email"] = "ana@mail.com"  # Agrega clave nueva**

#### Métodos útiles
- **keys()** → Devuelve todas las claves
- **values()** → Devuelve todos los valores
- **items()** → Devuelve pares clave-valor
- **pop(clave)** → Elimina una clave específica

## Funciones

Son bloques de código reutilizables que se pueden llamar múltiples veces tras definirse una sola vez.

### Ventajas
- **Reutilización:** Permiten usar el mismo código múltiples veces sin repetirlo.
- **Modularidad:** Dividen problemas complejos en componentes más pequeños y manejables.
- **Encapsulamiento:** Ocultan la complejidad interna y exponen solo lo necesario.

### Sintaxis básica
**def saludar(nombre):**  
&nbsp;&nbsp;&nbsp;&nbsp;**print(f"Hola, {nombre}!")**

### Ejemplo de uso
**saludar("Ana")  # Imprime: Hola, Ana!**

Las funciones pueden tener parámetros opcionales con valores predeterminados, devolver múltiples valores, definirse dentro de otras funciones (anidadas) y también pueden ser funciones lambda para operaciones simples.

### Ejemplo con docstring y return
**def saludar(nombre):**  
&nbsp;&nbsp;&nbsp;&nbsp;**"""Imprime un saludo al usuario"""**  
&nbsp;&nbsp;&nbsp;&nbsp;**print(f"¡Hola, {nombre}!")**  

**saludar("Ana")**

## Manejo de Excepciones

### Concepto
Los errores son inevitables: desde una división por cero hasta ingresar un dato no válido. Python ofrece **try-except** para manejar errores de forma controlada.

### Estructura
- **try**: Bloque donde se intenta ejecutar código
- **except**: Bloque que maneja la excepción si ocurre un error
- **finally**: Bloque que se ejecuta siempre, haya o no error

### Ejemplo
**try:**  
&nbsp;&nbsp;&nbsp;&nbsp;**valor = int(input("Ingresa un número entero: "))**  
&nbsp;&nbsp;&nbsp;&nbsp;**resultado = 10 / valor**  
&nbsp;&nbsp;&nbsp;&nbsp;**print(f"10 / {valor} = {resultado}")**  
**except ZeroDivisionError:**  
&nbsp;&nbsp;&nbsp;&nbsp;**print("Error: División por cero.")**  
**except ValueError:**  
&nbsp;&nbsp;&nbsp;&nbsp;**print("Error: Entrada inválida, no es un número entero.")**  
**finally:**  
&nbsp;&nbsp;&nbsp;&nbsp;**print("Operación finalizada.")**

### Errores comunes
- **ZeroDivisionError**: División por cero
- **ValueError**: Entrada con formato incorrecto
- **KeyError**: Acceso a claves inexistentes en diccionarios

## Git

Git es una herramienta de control de versiones que permite registrar, rastrear y compartir cambios en proyectos de código.

### Instalación
- **Windows:** Descarga desde Git SCM
- **Mac:** **brew install git**
- **Linux (Debian/Ubuntu):** **sudo apt-get install git**

### Configuración inicial
**git config --global user.name "Tu Nombre"**  
**git config --global user.email "tuemail@ejemplo.com"**

### Flujo típico de trabajo
1. Editar archivos en el proyecto
2. **git init** (una sola vez por proyecto)
3. **git add .** para agregar cambios
4. **git commit -m "mensaje"** para guardar snapshot
5. **git push** para subir al repositorio remoto

## GitHub

Plataforma en la nube para alojar repositorios Git, facilitar la colaboración y revisión de código.

### Crear una cuenta
1. Ingresar a [GitHub](https://github.com)  
2. Clic en **Sign up**  
3. Completar nombre de usuario, correo y contraseña  
4. Confirmar correo electrónico  
5. Elegir plan gratuito

### Flujo de trabajo básico
- Crear un repositorio en GitHub  
- Vincular repositorio local: **git remote add origin https://github.com/tu-usuario/proyecto.git**  
- Subir cambios: **git push -u origin main**

### Comandos básicos de Git
| Comando | Descripción |
|---------|-------------|
| **git init** | Convierte la carpeta actual en un repositorio Git local |
| **git clone URL** | Descarga copia de repositorio remoto |
| **git status** | Muestra estado actual del repositorio |
| **git add archivo.txt** | Añade un archivo al área de preparación |
| **git commit -m "mensaje"** | Crea un commit con cambios preparados |
| **git push origin main** | Envía commits locales al repositorio remoto |
| **git pull origin main** | Obtiene y fusiona cambios del repositorio remoto |
| **git branch nueva-rama** | Crea nueva rama |
| **git checkout nueva-rama** | Cambia a la rama especificada |

