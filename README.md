# API Vehículos 🚗

**Versión:** 1.0.0  
**Descripción:** API para gestión de vehículos, usuarios y autenticación utilizando FastAPI y PostgreSQL.  
**Autor:** Diego Del Castillo  
**Tecnologías:** Python 3.13, FastAPI, SQLAlchemy, PostgreSQL, JWT

## Requisitos / Pre-requisitos

- Python >= 3.10
- PostgreSQL >= 13
- Dependencias: las del archivo `requirements.txt`:

- fastapi
- uvicorn
- sqlalchemy
- psycopg2-binary
- passlib
- python-jose
- python-multipart

  ## Instalación y ejecución
  - Clonar el repositorio:
  git clone https://github.com/usuario/repo.git
  cd repo
-  python -m venv venv
- source venv/bin/activate  # Linux / Mac
- venv\Scripts\activate     # Windows
  
## Instalar dependencias:
pip install -r requirements.txt

## Ejecutar la aplicación:
uvicorn main:app --host 0.0.0.0 --port 8000

## Abrir Swagger UI para probar endpoints:
http://localhost:8000/docs

## Endpoints de la API
Autenticación
### POST /signup

Descripción: Crea un nuevo usuario JWT.

Request Body:

~~~
{
  "username": "string",
  "password": "string"
}
~~~

Response 201:
~~~
{
  "msg": "Usuario creado correctamente",
  "user": {
    "id": 1,
    "username": "juan123"
  }
}
~~~

Response 422:
~~~
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
~~~

### POST /login

Descripción: Genera un token JWT para autenticación.

Request Body:
~~~
{
  "username": "string",
  "password": "string"
}
~~~

Response 200:
~~~
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
~~~

Response 401:
~~~
{
  "detail": "Usuario o contraseña incorrectos"
}
~~~


### GET /vehicles

Descripción: Obtiene lista de vehículos.

Response 200:
~~~
[
  {
    "marca": "string",
    "sucursal": "string",
    "nombre_persona": "string",
    "id": 0
  }
]
~~~

### POST /vehicles

Descripción: Crea un nuevo vehículo.

Request Body:

~~~
{
  "marca": "string",
  "sucursal": "string",
  "nombre_persona": "string"
}
~~~

### GET /vehicles/{id}

Descripción: Obtiene un vehículo por id.

Response 200:
~~~
  {
    "marca": "string",
    "sucursal": "string",
    "nombre_persona": "string",
    "id": 0
  }
~~~

### PUT /vehicles/{id}

Descripción: Actualiza un vehículo de acuerdo al id ingresado.

Request Body:

~~~
{
  "marca": "string",
  "sucursal": "string",
  "nombre_persona": "string"
}
~~~

Response 200:
{
  "marca": "string",
  "sucursal": "string",
  "nombre_persona": "string",
  "id": 0
}

### DELETE /vehicles/{id}

Descripción: Elimina un vehículo de acuerdo al id ingresado.


Response 204:
NO CONTENT






