# Proyecto de Lista de Empleados en Django

Este proyecto es una aplicación simple en Django que muestra una lista de nombres de empleados en una página web. Fue creado como parte de un desafío para demostrar la visualización de contenido dinámico en Django.

## Descripción del Proyecto

La aplicación muestra una lista de nombres de empleados almacenados en una lista de Python. El número de empleados no es fijo, lo que permite flexibilidad en los datos mostrados.

## Características

- Mostrar una lista de nombres de empleados
- Mostrar el conteo total de empleados
- Demostrar el uso de vistas, URLs y plantillas de Django

## Requisitos

- Python 3.x
- Django 5.1.2
- Otras dependencias listadas en `requirements.txt`

## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual:
   ```
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - En Windows:
     ```
     venv\Scripts\activate
     ```
   - En macOS y Linux:
     ```
     source venv/bin/activate
     ```
4. Instala los paquetes requeridos:
   ```
   pip install -r requirements.txt
   ```

## Ejecución de la Aplicación

1. Navega al directorio del proyecto que contiene `manage.py`.
2. Ejecuta el siguiente comando para iniciar el servidor de desarrollo:
   ```
   python manage.py runserver
   ```
3. Abre un navegador web y ve a `http://127.0.0.1:8000/` para ver la aplicación.

## Estructura del Proyecto

- `views.py`: Contiene la lógica para procesar los datos de los empleados.
- `urls.py`: Define los patrones de URL para la aplicación.
- `templates/index.html`: La plantilla HTML para mostrar la lista de empleados.

## Contribuciones

Este proyecto fue creado como parte de un ejercicio de aprendizaje. Sin embargo, las sugerencias y mejoras son bienvenidas. No dudes en hacer un fork del repositorio y enviar pull requests.

## Autor
Natalia Peña
