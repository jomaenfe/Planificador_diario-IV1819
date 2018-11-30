## Documentación para la creación de un contenedor Docker con la aplicación.

### **Creación de mi contenedor**:

Para la creación de mi contenedor he utilizado la [documentación oficial de docker](https://docs.docker.com/get-started/part2/), donde está explicado de forma muy clara y es facil de seguir. 

En primer lugar lo que tenemos que hacer es definir nuestro archivo [*Dockerfile*](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/Dockerfile). En mi caso he definido el siguiente archivo: 

```
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

```

Donde podemos ver que le indicamos la versión que queremos que utilice de Python, los directorios donde se encuentra la aplicación y los que debe incluir en el contenedor, las dependencias que debe instalar y por último el puerto que debe exponer y los archivos que debe ejecutar para nuestra aplicación. 

Una vez hemos definido nuestro archivo *Dockerfile* tendremos que construir el contenedor en sí con nuestra aplicación. Para ello ejecutamos la siguiente orden:

` docker build -t planificadordiariodocker . `

Esta orden se encargará de descargar todas las dependecias de nuestra aplicación y de "empaquetar" todo el contenido en un contenedor. Cuando haya finalizado de construir podremos probar nuestro nuevo contenedor en local para ver si funciona o no. Para ejecutarlo debemos teclear la siguiente orden:

`docker run -p 5000:80 planificadordiariodocker`

En este momento, como le hemos especificado en el *Dockerfile* que necesita gunicorn para funcionar lo que va a hacer es usarlo, utilizamos el "-p" para decirle a docker en que puerto debe escuchar. La salida de la orden debería ser como la que se puede ver en la siguiente imagen.

![Ejecutando_Docker](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/ejecutandoDocker.png?raw=true)

Para comprobar que nuestra aplicación funciona podemos entrar en nuestro navegador web y teclear la siguiente dirección `localhost:5000`. Tas entrar deberíamos ver un JSON como el que se muestra en la siguiente imagen.

![localhost_docker](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/localhost_docker.png?raw=true)

Con esto ya tendríamos nuestro contenedor Docker creado de forma local.



