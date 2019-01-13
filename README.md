# PLANIFICADOR DIARIO

## Repositorio para el proyecto de infraestructura virtual

### Nombre del proyecto: Planificador diario

[![Build Status](https://travis-ci.org/jomaenfe/Planificador_diario-IV1819.svg?branch=master)](https://travis-ci.org/jomaenfe/Planificador_diario-IV1819)

### Autor: Jose Manuel Enríquez Fernández

#### Descripción:

EL proyecto trata sobre un servicio web, que voy a desarrollar en Python y que su principal utilidad será recordarnos que debemos hacer cada día para cumplir nuestros objetivos.

#### Desarrollo del proyecto:

 *DESCRIPCIÓN DE LA CLASE*

Se ha creado una clase planificador_diario, la cual se encuentra alojada en `/src/planificador_diario.py`. Esta clase se encarga de crear una tarea en un día, y con un rango horario en concreto. Se trabaja con los atributos "tarea","fecha", "hora_inicio", "hora_fin".

Para testear las funciones de la clase, he creado el archivo test_planificador.py que se encuentra en la ruta `/test/test_planificador.py`.

 *INSTALACIÓN Y TESTEO*

Antes de nada, tenemos que tener cubierta una dependencia básica para el proyecto. Este proyecto utiliza python3 para ejecutarse y Ubuntu como sistema operativo. Por lo que debemos tener Ubuntu instalado e instalar [python3](https://docs.python-guide.org/starting/install3/linux/) en nuestro sistema. También es recomendable instalar [git](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-18-04-quickstart).

Una vez hemos cumplido los *prerequisitos* clonamos el repositorio en nuestra máquina usando la siguiente orden: ` git clone https://github.com/jomaenfe/Planificador_diario-IV1819.git `. 

Cuando tengamos el repositorio en nuestra máquina, tan solo debemos ejecutar `pip3 install -r requirements.txt ` desde la carpeta raiz del proyecto para que se instalen las dependencias.

Después de instalar las dependencias ya estará todo listo para ejecutarlo, por lo que ejecutamos `sudo sh iniciar_gunicorn.sh` para que se inicie el servidor y ya estaría funcionando la aplicación en local. 

Para ejecutar los test, sólo tenemos que irnos a la raíz del directorio y ejecutar `pytest` desde la terminal. Esta orden nos proporcionará una salida y ahí se verá el resultado del test sobre la clase de la app.

*INTEGRACIÓN CONTINUA MEDIANTE TRAVIS*

Lo primero que tenemos que hacer es darnos de alta en [travis](https://travis-ci.org/) con nuestras credenciales de [github](https://github.com/), habilitamos el repositorio para que travis pueda hacer test y obtenemos un log de los mismos donde podremos ver si lo has pasado o no.

*DESPLIEGUE EN HEROKU*

- Despliegue en [heroku](https://planificadordiario.herokuapp.com/)
- Json [adicional](https://planificadordiario.herokuapp.com/status) en el despligue
- [Documentación](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/despliegue.md) del despliegue en heroku

*CONTENEDORES DOCKER*

Contenedor: [https://planificadordiariodocker.herokuapp.com/](https://planificadordiariodocker.herokuapp.com/status)

Contenedor desplegado en docker-hub: [Planificador Docker-hub](https://hub.docker.com/r/jomaenfe/planificador_diario-iv1819/)

Documentación sobre la creación de nuestro contenedor [aqui](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/documentacion_docker.md)

Documentación sobre el despliegue en docker-hub [aqui](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/documentacion_dockerhub.md)

Documentación sobre el despliegue en heroku [aqui](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/despliegue_docker_heroku.md)

*DESPLIEGUE EN AZURE*

Despliegue final: planificador-diario-1819.westeurope.cloudapp.azure.com

Documentación sobre el despligue final en la que incluyo, fabric, ansible y vagrant: [documentación](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/despliegue-azure.md)