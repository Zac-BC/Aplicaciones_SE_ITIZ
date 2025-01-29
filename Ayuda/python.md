# entorno virtual
python -m venv "nombre_del_entorno"
python -m venv venv

# activar entorno virtual (windows)
.\"nombre_del_entorno"\Scripts\activate
.\venv\Scripts\activate

# Instalar requerimientos
python -m pip install -r .\"Nombre_del_archivo_de_requerimientos".txt
python -m pip install -r .\requirements.txt

# Buscar Version de python
python --version

## DJANGO

# Iniciar proyecto Django
django-admin startproject "nombre_del_proyecto"
django-admin startproject webserver

# Ejecutar el servidor
dentro de la carpeta webserver
python manage.py runserver

# Creando app de nombre
django-admin startapp "Nombre_de_la_app"
django-admin startapp api

# Denttro del archivo settings en webserver en "INSTALLED_APPS ="
INSTALLED_APPS = [
    "XXXXX",
    "xxxxxx",

    "api",
]