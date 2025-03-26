# ClassConnect

## Tabla de Contenidos

- [Introducción](#introducción)
- [Desafíos del Proyecto](#desafíos-del-proyecto)
- [Pre-requisitos](#pre-requisitos)
- [Guía de Usuario para Testing](#guía-de-usuario-para-testing)
- [Comandos Docker](#comandos-docker)
- [Variables de entorno](#variables-de-entorno)

## Introducción

Este proyecto es una solución para la gestión de cursos utilizando FastAPI y PostgreSQL. La aplicación permite crear, listar, eliminar y obtener detalles de cursos a través de una API RESTful-like. Además, se han implementado pruebas end-to-end para asegurar el correcto funcionamiento de la aplicación.

## Desafíos del Proyecto

Lo más desafiante del proyecto fue configurar correctamente el entorno de Docker para que todos los servicios (API, base de datos y pruebas) se comunicaran entre sí sin problemas. Además, asegurar que las pruebas end-to-end se ejecutaran correctamente en el entorno de Docker fue un reto significativo. 
En el entorno de testing (docker-compose.test.yml), tuve que implementar un metodo de health-check tanto para la BDD como para mi servicio web, a la hora de levantar mi container de testing (test_runner). Es por eso que en mi API se incluye un endpoint mas al sistema, "/health" , el cual me indica si el sistema esta activo, en caso de obtener una respuesta satisfactoria tanto de la BDD como de mi servicio web, el contenedor de testing se levanta y procede a realizar las pruebas automatizadas.
Por otro lado, simplemente como aclaracion, se podra observar en el archivo "docker-compose.test.yml" que existen ciertos valores hardcodeados, como el {PORT} y demas, esto quise hacerlo parametrizable, por eso cree el "common-services.yml", pero hasta el momento estaba fallando, por algun motivo no toma las variables de entorno del ".env.test", si no que toma las variables de entorno del ".env" lo cual es incorrecto y se producen inconsistencias si uno quiere tener levantado los 2 ambientes (produccion y testing) al mismo tiempo, ya que se intenta tomar un puerto que ya esta en uso, debido a que estan queriendo usar la misma variable de entorno {PORT}.

## Pre-requisitos

Para levantar el entorno de desarrollo, se necesitan los siguientes paquetes:

- Docker
- Docker Compose

## Guía de Usuario para Testing

Para las pruebas, se utilizó la librería `pytest` junto con `TestClient` de FastAPI.

- **pytest**: Es una herramienta de testing en Python que permite escribir pruebas simples y escalables. Con `pytest`, puedes realizar pruebas unitarias, pruebas de integración y pruebas end-to-end. Además, `pytest` proporciona una buena funcionalidad para la ejecución de pruebas, incluyendo la capacidad de ejecutar pruebas en paralelo, generar informes detallados y manejar fixtures para la configuración y limpieza del entorno de pruebas. Más información en la [documentación oficial de pytest](https://docs.pytest.org/en/7.1.x/).

- **TestClient**: Es una herramienta proporcionada por FastAPI para realizar pruebas de integración y end-to-end. `TestClient` permite simular peticiones HTTP a la aplicación FastAPI y verificar las respuestas. Esto es útil para asegurarse de que los endpoints de la API funcionan correctamente y devuelven los resultados esperados. Más información en la [documentación de FastAPI sobre TestClient](https://fastapi.tiangolo.com/reference/testclient/?h=test).

## Variables de entorno

### Archivo .env

```sh
ENVIRONMENT=development
HOST=0.0.0.0
PORT=8000
EXTERNAL_DATABASE_PORT=5434
INTERNAL_DATABASE_PORT=5432
DATABASE_HOST=db
DATABASE_NAME=mydatabase
DATABASE_USER=myuser
DATABASE_PASSWORD=mypassword
DATABASE_URL=postgresql://${DATABASE_USER}:${DATABASE_PASSWORD}@${DATABASE_HOST}:${INTERNAL_DATABASE_PORT}/${DATABASE_NAME}
```

### Archivo .env.test

```sh
ENVIRONMENT=test
HOST=0.0.0.0
PORT=8001
EXTERNAL_DATABASE_PORT=5435
INTERNAL_DATABASE_PORT=5432
DATABASE_HOST=db_test
DATABASE_NAME=test_database
DATABASE_USER=test_user
DATABASE_PASSWORD=test_password
DATABASE_URL=postgresql://${DATABASE_USER}:${DATABASE_PASSWORD}@${DATABASE_HOST}:${INTERNAL_DATABASE_PORT}/${DATABASE_NAME}
```

## Comandos Docker

Desde la raiz del proyecto:
 
### Construir el ambiente de produccion

```sh
sudo docker-compose up --build
```

### Construir el ambiente de testing

```sh
sudo docker-compose --env-file .env.test -f docker-compose.test.yml up --build
```


