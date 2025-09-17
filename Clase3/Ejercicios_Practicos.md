# ⚙️ Ejercicios Prácticos – Clase 3 – Automatización

---

## Contexto
El objetivo es afianzar el uso de **estructuras de control** y la **entrada/salida de datos** en Python.  
Se comenzará con una **calculadora básica** que luego se modularizará con funciones, condicionales y bucles.  

---

## Ejercicio Práctico (Obligatorio)

### Actividad 1: Mejorando la calculadora
1. Refactorizar el script de la calculadora lineal en al menos **4 funciones separadas**:
   - `Sumar()`
   - `Restar()`
   - `Multiplicar()`
   - `Dividir()`

2. Añadir **manejo de excepciones** para:
   - Entradas inválidas.
   - División por cero.

---

### Actividad 2: Git y GitHub

#### Git local
1. Crear una carpeta nueva para el proyecto de calculadora.  
2. Inicializar un repositorio con `git init`.  
3. Agregar y confirmar cambios con:
   ```bash
   git add .
   git commit -m "Primera versión de la calculadora"
  ```

### GitHub

1. Crear una cuenta en [GitHub](https://github.com).  
2. Crear un nuevo repositorio desde tu perfil (usá el mismo nombre del proyecto).  
3. Copiar la URL del repositorio (HTTPS).  
4. Enlazar el repositorio local con GitHub:  
   - - -
   git remote add origin <URL_DEL_REPO>
   - - -
5. Subir los archivos con:  
   - - -
   git push -u origin main
   - - -
