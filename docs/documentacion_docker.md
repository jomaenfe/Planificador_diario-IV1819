## Documentación para la creación de un contenedor Docker con la aplicación.

### **Instalación**:

Para la instalación de Docker he seguido este [tutorial](https://ubunlog.com/como-instalar-docker-en-ubuntu-18-04-y-derivados/).

Como siempre, antes de instalar algún paquete para desarrollo es bueno limpiar versiones anteriores en el sistema. En el caso de Docker, la ordena a usar sería esta `sudo apt-get remove docker docker-engine docker.io`. En mi caso, como es la primera vez que instalo Docker no es necesario ejecutarla. También se recomienda ejecutar un `sudo apt-get update` y después `sudo apt-get upgrade`. Con esto nos aseguraremos de que el sistema tiene la últimas versiones tanto de las aplicaciones que tiene instaladas como del mismo sistema. 

Para comenzar con la instalación de Docker en sí, lo que primeramente debemos hacer es instalar unas dependencias. Para ellos ejecutamos `sudo apt-get install apt-transport-https`, `sudo apt-get install ca-certificates`, `sudo apt-get install curl` y `sudo apt-get install software-properties-common`. 

Tras haber instalado las dependecias, procedemos a importar la clave GPG. Para ello, ejecutamos `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`. Para comprobar que las descargas se han hecho de forma correcta debemos comprobar la huella digital. Para ello nos bastará con buscar los últimos 8 caracteres de la misma, esta orden nos los mostraría ` sudo apt-key fingerprint 0EBFCD88 `. En la salida de este comando deberíamos ver una línea igual que la siguiente ` key fingerprint = 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88 `. Si la huella esta bien procedemos a añadir el repositorio ` sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
 ` y ejecutamos un update para que se actualice.
 
Una vez hemos hecho esto ya solo nos quedará ejecutar `  sudo apt-get install docker-ce ` y ya lo tendremos instalado. Por último, para añadir nuestro usuario al grupo de usuarios de Docker ejecutamos `sudo usermod -aG docker $USER` cambiando $user por el nombre de nuestro usuario y posteriormente reiniciando la máquina.

### **Probando la instalación**:

Para probar que la instalación se ha realizado de forma correcta podemos usar un contenedor que tiene Docker y probarlo. Este contenedor lo único que hace es descargarse en nuestro equipo y mostrar por pantalla un "Hola mundo". Para probarlo tan solo debemos teclear en nuestra terminal `docker run hello-world` y por pantalla deberíamos ver algo similar a la siguiente imagen. 

![Prueba de Docker](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/prueba_docker.png?raw=true)

En la misma pantalla nos dice que nuestra instalación está funcionando correctamente por lo que debería bastarnos para poder trabajar co Docker.

### **Creación de mi contenedor**:

Para la creación de mi contenedor he utilizado la [documentación oficial de docker](https://docs.docker.com/get-started/part2/), donde está explicado de forma muy clara y es facil de seguir. 

En primer lugar lo que tenemos que hacer es definir nuestro archivo *Dockerfile*. En mi caso he definido el siguiente archivo: 
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



