# grillo_tech_ch2grillo_tech_ch1
=======

# Python Challenge 1

## Alternativas para ejecutar el proyecto

### 1. Ejecutar la aplicación con Docker

Si tienes Docker instalado, puedes seguir los siguientes pasos para construir y ejecutar la aplicación en un contenedor Docker.

#### Pasos:

1. **Construir la imagen de Docker**:  
   Desde el directorio raíz del proyecto, ejecuta el siguiente comando para construir la imagen:
   ```bash
   docker build -t python-challenge .
   ```

2. **Ejecutar la imagen de Docker**:  
   Después de construir la imagen, puedes correr el contenedor con el siguiente comando:
   ```bash
   docker run -it python-challenge
   ```

---

### 2. Ejecutar la aplicación directamente en la terminal

Si prefieres no utilizar Docker, puedes ejecutar la aplicación directamente en tu máquina. Asegúrate de tener Python instalado y seguir los pasos a continuación.

#### Pasos:

1. **Instalar las dependencias**:  
   Ejecuta el siguiente comando en el directorio del proyecto para instalar las dependencias necesarias desde `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar la aplicación**:  
   Después de instalar las dependencias, ejecuta la aplicación con:
   ```bash
   python main.py
   ```

---

### 3. Ejecutar la aplicación utilizando un ambiente virtual

Es recomendable utilizar un ambiente virtual para evitar conflictos con otras dependencias en tu sistema. Aquí se detallan los pasos para crear y activar un entorno virtual.

#### Pasos:

1. **Crear un ambiente virtual**:  
   Para Linux o macOS:
   ```bash
   python3 -m venv env
   ```
   Para Windows:
   ```bash
   python -m venv env
   ```

2. **Activar el ambiente virtual**:  
   En Linux o macOS:
   ```bash
   source env/bin/activate
   ```
   En Windows:
   ```bash
   .\env\Scripts\activate
   ```

3. **Instalar las dependencias**:  
   Con el ambiente virtual activado, instala las dependencias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:  
   Finalmente, ejecuta la aplicación con:
   ```bash
   python main.py
   ```

---

## Método de Validación (Testing)

Independientemente de cuál de los tres métodos de ejecución elijas, el método de testing consiste en verificar que al ejecutar el programa, se impriman tres tests con el resultado **"válido"**. Estos tests validan la funcionalidad correcta del código y sirven como confirmación de que la solución es correcta.

Por lo tanto, para validar que la aplicación funciona correctamente, asegúrate de que, al final de la ejecución, se muestren los tres tests con la salida "válido" en la terminal o consola.
