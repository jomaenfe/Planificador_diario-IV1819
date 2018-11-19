## Documentación para desplegar un contenedor Docker en Heroku.

Para realizar el despliegue de un contenedor de Docker en heroku he utilizado la documentación [oficial de heroku](https://devcenter.heroku.com/articles/container-registry-and-runtime). 

En primer lugar, lo que tenemos que hacer es bajarnos el CLI de heroku, pero como ya tengo un despliegue hecho en su web ya lo tengo instalado por lo que obvio este paso.

En segundo lugar debemos iniciar sesión en heroku, en el registro de contenedores. Para ello tecleamos el comando `heroku container:login`. Esto nos debería dar una salida como la que se ve en la siguiente imagen.

![Log_HerokuDocker](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/logueo_heroku_container.png?raw=true)

Una vez nos hemos logueado en el registro nos aseguramos de tener la versión de *Dockerfile* adecuada para que funcione en heroku. En mi caso, es la siguiente: 

```
# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD gunicorn app:__hug_wsgi__ --log-file -

```

Cuando nos hayamos asegurado de que es la correcta procedemos a hacer el **build** del contenedor, para lo que en heroku se utiliza `heroku container:push web --app <nombre de la app>`. Este comando nos dará una salida igual que la que nos da el comando `docker build -t <nombre del contenedor .`. En la siguiente imagen podemos ver la salida.

![Build_heroku](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/heroku_container_push.png?raw=true)

Cuando termine de hacer el build ya solo nos quedará lanzar nuestro contenedor en los registros de heroku para que empiece a funcionar y que podamos ver los resultados. Para ello utilizamos el comando `heroku container:release web --app <nombre de la app` y a continuación ya solo nos quedará ejecutar la aplicación desde la web o terminal para ver que funciona correctamente. En las siguientes imágenes se puede ver que en mi caso está todo correcto.

![Lanzando_contenedor](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/heroku_container_release.png?raw=true)

![Probando:_contenedor](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/probando_heroku_docker.png?raw=true)