# entorno virtual
python -m venv venv

# activa el entorno virtual (windows)
.\venv\Scripts\activate

# instalar requerimientos en python 
python -m pip install -r .\requirements.txt

## Django

# Crear un proyecto
django-admin startproject webserver

     manage.py
     webserver/
         asgi.py
         settings.py
         urls.py
         wsgy.py
# Ejecutar el servidor
dentro de la carpeta webserver
    cd webserver
python manage.py runserver

# Crear app con nombre api
django-admin startapp api 
