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

Para su instalación lo primero que debemos de hacer es clonar este repositorio usando la orden: ` git clone https://github.com/jomaenfe/Planificador_diario-IV1819.git `. Cuando tengamos el repositorio clonado, tan solo tendremos que instalar "pytest" con la orden  `pip install pytest`. 

Para comprobar si todo está bien, sólo tenemos que irnos a la raíz del directorio y ejecutar `pytest` desde la terminal. Esta orden nos proporcionará una salida y ahí se verá el resultado del test.

*INTEGRACIÓN CONTINUA MEDIANTE TRAVIS*

Lo primero que tenemos que hacer es darnos de alta en [travis](https://travis-ci.org/) con nuestras credenciales de [github](https://github.com/), habilitamos el repositorio para que travis pueda hacer test y obtenemos un log de los mismos donde podremos ver si lo has pasado o no.

*DESPLIEGUE EN HEROKU*

- Despliegue en [heroku](https://planificadordiario.herokuapp.com/)
- Json [adicional](https://planificadordiario.herokuapp.com/status) en el despligue
- [Documentación](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/despliegue.md) del despliegue en heroku

*CONTENEDORES DOCKER*

Contenedor: [https://planificadordiariodocker.herokuapp.com/](https://planificadordiariodocker.herokuapp.com/)

Contenedor desplegado en docker-hub: [https://hub.docker.com/r/jomaenfe/planificador_diario-iv1819/](https://hub.docker.com/r/jomaenfe/planificador_diario-iv1819/)

Documentación sobre el despliegue de docker y demás información: en la carpeta [/docs](https://github.com/jomaenfe/Planificador_diario-IV1819/tree/master/docs)