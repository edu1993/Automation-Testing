# Ejercicios de Repaso

---

## Pregunta 1
**¿Qué decorador en Pytest se utiliza para probar múltiples combinaciones de datos?**

**Respuesta:**
- a. @pytest.mark.exception  
- b. @pytest.mark.fixture  
- c. @pytest.skip  
- d. ✅ @pytest.mark.parametrize  

**Retroalimentación:**  
`@pytest.mark.parametrize` permite ejecutar un mismo test con distintos conjuntos de datos.  

---

## Pregunta 2
**¿Cuál es la principal ventaja de usar funciones en lugar de un flujo lineal?**

**Respuesta:**
- a. Evita tener que usar estructuras de control.  
- b. Permite escribir todo el código en una sola línea.  
- c. ✅ Mejora la claridad, reutilización y mantenimiento del código.  
- d. Hace que el código sea más lento, pero más compacto.  

**Retroalimentación:**  
Las funciones permiten modularizar el código, haciéndolo más claro, reutilizable y fácil de mantener.  

---

## Pregunta 3
**¿Qué comando se usa para enviar commits al repositorio remoto?**

**Respuesta:**
- a. ✅ git push  
- b. git fetch  
- c. git commit  
- d. git pull  

**Retroalimentación:**  
`git push` se usa para subir los commits al repositorio remoto, como GitHub.  

---

## Pregunta 4
**¿Para qué sirve la sentencia `raise ValueError` en Python?**

**Respuesta:**
- a. ✅ Para lanzar una excepción cuando ocurre un error esperado.  
- b. Para definir una nueva función.  
- c. Para evitar la ejecución de un bloque if.  
- d. Para terminar un programa abruptamente.  

**Retroalimentación:**  
`raise ValueError` permite lanzar una excepción personalizada cuando se detecta un error lógico o de entrada.  

---

## Pregunta 5
**¿Qué comando de Git se usa para crear un nuevo repositorio local?**

**Respuesta:**
- a. ✅ git init  
- b. git commit  
- c. git clone  
- d. git push  

**Retroalimentación:**  
El comando `git init` se usa para inicializar un nuevo repositorio Git en la carpeta actual.  

---

## Pregunta 6
**¿Qué comando de Pytest se usa para generar un reporte HTML de pruebas?**

**Respuesta:**
- a. pytest --generate-report  
- b. pytest --to-html  
- c. ✅ pytest --html=report.html  
- d. pytest-html  

**Retroalimentación:**  
`pytest --html=report.html --self-contained-html` genera un reporte visual autosuficiente en HTML.  

---

## Pregunta 7
**¿Cuál de las siguientes estructuras de datos en Python permite pares clave-valor?**

**Respuesta:**
- a. Set  
- b. Tupla  
- c. Lista  
- d. ✅ Diccionario  

**Retroalimentación:**  
Los diccionarios permiten almacenar datos en pares clave-valor, útiles para organizar información.  

---

## Pregunta 8
**¿Cuál de estas opciones describe correctamente un marker en Pytest?**

**Respuesta:**
- a. Una función decoradora que transforma números.  
- b. Un test que se ejecuta en segundo plano.  
- c. ✅ Una etiqueta que permite agrupar o filtrar tests.  
- d. Un nombre de archivo que debe tener cada test.  

**Retroalimentación:**  
Los markers etiquetan tests (como *smoke* o *exception*), permitiendo filtrarlos al ejecutar.  

---

## Pregunta 9
**¿Qué instrucción en Python se utiliza para manejar excepciones?**

**Respuesta:**
- a. ✅ try/except/finally  
- b. begin/rescue  
- c. catch/throw  
- d. error handling  

**Retroalimentación:**  
La estructura `try/except/finally` permite manejar errores de forma controlada en Python.  

---

## Pregunta 10
**¿Cuál es la función de un fixture en Pytest?**

**Respuesta:**
- a. Validar excepciones automáticamente.  
- b. Generar automáticamente reportes HTML.  
- c. ✅ Preparar datos o configuraciones reutilizables antes del test.  
- d. Ejecutar el test más de una vez.  

**Retroalimentación:**  
Un fixture prepara datos o configuraciones reutilizables antes de ejecutar un test.  

---
