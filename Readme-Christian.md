# Instrucciones para Levantar CIPE

## Requisitos Previos

- Tener MySQL instalado en tu sistema.
- PostgreSQL instalado en tu sistema para la rama `develop`.

## Pasos para Levantar el Proyecto

1. **Clonar el Repositorio:**

    Clonar el repositorio de CIPE desde GitHub:
    
    ```bash
    git clone https://github.com/MathiMartinez00/cipe-captura.git
    ```

2. **Acceder al Directorio:**

    Ingresar al directorio del proyecto CIPE:
    
    ```bash
    cd cipe
    ```

3. **Cambiar a la Branch `develop` si lo desea:**

    Cambiar a la branch `develop` si es necesario:
    
    ```bash
    git checkout develop
    ```

    **Actualizar la Branch `develop`:**

   Obtener los últimos cambios en la branch `develop`:

   ```bash
   git pull origin develop
   ```

5. **Renombrar Archivos de Configuración:**

    Renombrar el archivo `cipe/settings.py.sample` a `cipe/settings.py`:
    
    ```bash
    mv cipe/settings.py.sample cipe/settings.py
    ```

    Renombrar el archivo `.env.dev.sample` a `.env.dev`:
    
    ```bash
    mv .env.dev.sample .env.dev
    ```

6. **Crear Base de Datos y Configurar Permisos para MySQL:**

    Acceder a MySQL como el usuario `root`:
    
    ```bash
    mysql -u root -p
    ```

    Dentro del cliente de MySQL, ejecutar los siguientes comandos SQL para crear la base de datos `cipe` y el usuario `cipe_user` con contraseña `cipe`, y otorgar todos los privilegios sobre la base de datos `cipe` al usuario `cipe_user`:

    ```sql
    CREATE DATABASE cipe;
    CREATE USER 'cipe_user'@'localhost' IDENTIFIED BY 'cipe';
    GRANT ALL PRIVILEGES ON cipe.* TO 'cipe_user'@'localhost';
    FLUSH PRIVILEGES;
    ```

    Una vez ejecutados los comandos SQL, puedes salir del cliente de MySQL con el comando `exit`.

7. **Crear Base de Datos y Configurar Permisos para PostgreSQL:**

    Acceder a PostgreSQL como el usuario `postgres`:
    
    ```bash
    sudo -u postgres psql
    ```

    Dentro del cliente de PostgreSQL, ejecutar los siguientes comandos SQL para crear la base de datos `cipe`, el usuario `cipe_user` con contraseña `cipe`, y otorgar todos los privilegios sobre la base de datos `cipe` al usuario `cipe_user`:

    ```sql
    CREATE DATABASE cipe;
    CREATE USER cipe_user WITH PASSWORD 'cipe';
    GRANT ALL PRIVILEGES ON DATABASE cipe TO cipe_user;
    ```

    Una vez ejecutados los comandos SQL, puedes salir del cliente de PostgreSQL con el comando `\q`.

8. **Generar Clave Secreta y API Key de Google:**

    Generar una clave secreta aleatoria para utilizar en la configuración del proyecto y una API Key de Google: https://developers.google.com/maps/documentation/embed/get-api-key?hl=es-419 
   
    Clave Secreta:
    ```bash
    python3 -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))'
    ```

9. **Configurar Variables de Entorno para MySQL:**

    Configurar las variables de entorno y parámetros de configuración de la base de datos en el archivo `.env.dev` para MySQL:
    
    ```
    DEBUG=0
    SECRET_KEY=$SECRET_KEY
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    SQL_ENGINE=django.db.backends.mysql
    SQL_DATABASE=cipe
    SQL_USER=cipe_user
    SQL_PASSWORD=cipe
    SQL_HOST=db
    SQL_PORT=3306
    GOOGLE_MAPS_API_KEY=$GOOGLE_MAPS_API_KEY
    DATABASE=mysql
    ```

10. **Configurar Variables de Entorno para PostgreSQL:**

    Configurar las variables de entorno y parámetros de configuración de la base de datos en el archivo `.env.dev` para PostgreSQL:
    
    ```
    DEBUG=0
    SECRET_KEY=$SECRET_KEY
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=cipe
    SQL_USER=cipe_user
    SQL_PASSWORD=cipe
    SQL_HOST=db
    SQL_PORT=5432
    GOOGLE_MAPS_API_KEY=$GOOGLE_MAPS_API_KEY
    DATABASE=postgres
    ```

11. **Construir el Contenedor Docker para Develop:**

    Construir el contenedor Docker utilizando el archivo de composición `docker-compose.yml`:
    
    ```bash
    docker-compose up --build -d
    ```

12. **Acceder a la Aplicación en Develop:**

    Ir a http://localhost:8000 para acceder a la herramienta CIPE en desarrollo.

13. **Construir el Contenedor Docker en Producción:**

    Construir el contenedor Docker para producción utilizando el archivo de composición `docker-compose.prod.yml`:
    
    ```bash
    docker-compose -f docker-compose.prod.yml up --build -d
    ```

14. **Cargar Datos Iniciales en Producción:**

    Cargar datos iniciales en la base de datos de producción utilizando el siguiente comando:
    
    ```bash
    docker-compose -f docker-compose.prod.yml exec app python manage.py loaddata data/initial_data.json
    ```

15. **Acceder a la Aplicación en Producción:**

    Para acceder a la herramienta CIPE en producción, ve a http://localhost:1550 en tu navegador web.
