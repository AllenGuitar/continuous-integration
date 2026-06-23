# Continuous Integration

Repositorio correspondiente al proyecto práctico de Integración Continua para la materia **Énfasis Profesional II**.

El objetivo del proyecto es implementar un flujo básico de integración continua utilizando GitHub Actions, pruebas automatizadas y contenedores Docker.

## Descripción del proyecto

La aplicación está compuesta por tres partes principales:

- Un backend desarrollado en Node.js que expone una API REST.
- Un quiz de curiosidades sobre gatitos implementado en Python para las pruebas con GitHub Actions.
- Un frontend web que permite interactuar con la aplicación.

Además, se implementó un pipeline de integración continua encargado de ejecutar pruebas automáticas cada vez que se realizan cambios en el repositorio.

## Integrantes

Subgrupo 5 – Integración Continua

- Bryant David Bohorquez Caro
- Juan Sebastián Bustos Marroquin
- Luis Campos Rojas
- Juan Jaramillo Jiménez
- Sara Sotaquira Pineda


## Integración continua

El proyecto utiliza GitHub Actions para automatizar la ejecución de pruebas.

Ante cada `push` o `pull request`, se ejecuta el workflow definido en:

```text
.github/workflows/ci.yml
```

Si alguna prueba falla, la ejecución del pipeline se marca como fallida.

## Pruebas

Las pruebas automatizadas se encuentran en:

```text
backend/test_quiz_gatitos.py
```

Los casos de prueba verifican:

- Respuestas correctas e incorrectas.
- Manejo de mayúsculas y minúsculas.
- Cálculo del puntaje total.
- Asignación del nivel obtenido según el puntaje.


## Tecnologías utilizadas

- Node.js
- Express
- Python
- GitHub Actions
- Docker
- Docker Compose

  ## Estructura del proyecto

```text
continuous-integration/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── backend/
│   ├── src/
│   │   └── index.js
│   ├── quiz_gatitos.py
│   ├── test_quiz_gatitos.py
│   ├── Dockerfile
│   └── package.json
│
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── shausuke2.jpg
│   ├── Dockerfile
│   └── nginx.conf
│
├── docker-compose.yml
└── README.md
```


