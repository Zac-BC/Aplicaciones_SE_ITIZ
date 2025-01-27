# entorno virtual
python -m venv "nombre_del_entorno"
python -m venv venv

# activar entorno virtual (windows)
.\"nombre_del_entorno"\Scripts\activate
.\venv\Scripts\activate

# Instalar requerimientos
python -m pip install -r .\"Nombre_del_archivo_de_requerimientos".txt
python -m pip install -r .\requirements.txt

## DJANGO

# Iniciar proyecto Django
django-admin startproject "nombre_del_proyecto"
django-admin startproject webserver

# Buscar Version de python
python --version