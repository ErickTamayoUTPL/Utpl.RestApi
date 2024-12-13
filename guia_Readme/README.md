# Utpl.RestApi
Proyecto para trabajar con Api en REST utilizando FastAPI


## Descripción del Proyecto

**Este proyecto es una aplicación web construida utilizando FastAPI.** FastAPI es un framework de Python moderno, rápido y fácil de usar para crear APIs. Es ideal para construir aplicaciones web backend que necesitan ser eficientes y escalables.

## Requisitos

* **Python:** Asegúrate de tener Python 3.6 o superior instalado.
* **FastAPI:** Instala FastAPI usando pip:
  ```bash
  pip install fastapi uvicorn

## Documentación 


API de Registro centralizado de proyectos 
Este proyecto busca implentar el desarrollo de un sistema centralizado para gestionar proyectos, permitiendo a los usuarios registrar, consultar, actualizar y eliminar información de manera segura y accesible. El sistema utiliza una arquitectura basada en C4 con usuarios finales y administradores como actores principales. Los componentes incluyen una aplicación web de gestión construida con Angular 16, una API RESTful desarrollada con Python y FastAPI, y una base de datos PostgreSQL para almacenar los datos de proyectos. Pulumi se utiliza para aprovisionar los recursos en la nube, garantizando flexibilidad y escalabilidad. El flujo del sistema comienza con solicitudes del usuario final que son procesadas por la API y almacenadas en la base de datos. Los administradores supervisan y gestionan permisos desde la aplicación web.

## C4 Model
En el archivo c4model.txt encontrarán el código correspondiente al diseño de la Arquitectura C4 Model propuesta, el cual está desarrollado de manera parcial.

Este diseño puede ser ejecutado en la plataforma https://structurizr.com/dsl  
Y se podra ejecutar haciendo un copiando la carpeta C4model.txt

## Ejecución de código 

Desde la carpeta app y el códig python de "main.py"







  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
