# Prueba Técnica

## **Arquitectura de la Aplicación**

- **Descripción General**:
    - Utilizare la arquitectura MVC
- Consideraciones:
    - Utilizare PEP8: Que es PEP8?
        - Es una guía de estilo para escribir código Python que sigue las mejores prácticas y convenciones de la comunidad.

## Módulos:

1. **Módulo de Listar Noticias**
    - **Descripción**: Este módulo va a listar todas las noticias que el Frontend obtiene del Backend
2. **Módulo de Ver Detalle**
    - **Descripción**: Este módulo permite ver los detalles de una noticia específica.
3. **Módulo de Crear Noticia**
    - **Descripción**: Este módulo permite crear nuevas noticias en la base de datos.
4. **Módulo de Actualizar Noticia**
    - **Descripción**: Este módulo permite actualizar una noticia ya existente.
5. **Módulo de Eliminar Noticia**
    - **Descripción**: Este módulo maneja la eliminación de noticias, tanto lógica como física en el back.

### Documentación:

- Utilizare Swagger para documentar todos los endpoints del backend.

### Seguridad

- **JWT Tokens**:
    - **Propósito**: Implementar autenticación basada en tokens JWT para asegurar que solo los usuarios autenticados puedan realizar acciones específicas como crear, actualizar o eliminar noticias. para simular un CRM.
    - **Implementación**:
        - **Backend**: Utilizar `djangorestframework-simplejwt` para gestionar la autenticación y la emisión de tokens.
        - **Frontend**: Almacenar y enviar el token JWT en los encabezados de las solicitudes API.
- **Django CORS Headers**:
    - **Propósito**: Permitir que mi api solo sea accesible por dominios en especifico

## Base de datos:

- Utilizaría PostgreSQL pero como no podre mostrarlo en vivo , lo realizare con SQLITE3 para que puedan verlo.

### Rendimiento (Frontend):

- Utilizare React, Tailwind, Typescript y React Query. Este ultimo para manejar peticiones asíncronas para actualizar datos en tiempo real.
