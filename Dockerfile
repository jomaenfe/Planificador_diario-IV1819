# Usamos la imagen de python slim para que ocupe menos espacio
FROM python:3.6-slim

# Establecemos la carpeta /app para que docker trabaje en ella
WORKDIR /app

# Copiamos los archivos necesarios de nuestro proyecto a la carpeta /app
COPY ./src/ /app/src
COPY ./requirements.txt /app
COPY ./planEjemplo.json /app
COPY ./app.py /app


# Instalamos las dependencias necesarias para el funcionamiento de nuestro proyecto
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Hacemos que el puerto 80 sea accesible
EXPOSE 80

# Comando que se va a ejecutar en el contenedor
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:__hug_wsgi__"]

