## Documentación para desplegar un contenedor Docker en Heroku.

Para realizar el despliegue de un contenedor de Docker en heroku he utilizado la documentación [oficial de heroku](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml). 

En primer lugar, lo que tenemos que hacer es bajarnos el CLI de heroku y tener creada la aplicación en la web. Como ya tengo un despliegue hecho obviamos los pasos para instalar el CLI y para crear una aplicación.

En segundo lugar, en mi caso, como tengo la aplicación desplegada de varias formas en heroku tengo que cambiar el repositorio a la aplicación con la que voy a trabajar por lo que ejecuto `heroku git:remote -a planificadordiariodocker` y lo cambio.

En tercer lugar, empezamos con la construcción del archivo [heroku.yml](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/heroku.yml).

```
build:
  docker:
    web: Dockerfile
run:
  web: gunicorn app:__hug_wsgi__ --log-file -
```

Este archivo contiene instrucciones para que cada vez que hagamos un push a nuestro repostorio y pase los test, heroku haga un build de nuestro contenedor en sus registros y lo ejecute. Para hacer el build se le indica nuestro archivo Dockerfile y para que lo ejecute sin problemas añadimos `run web: gunicorn app:__hug_wsgi__ --log-file -`. Esto último sustiye la última línea del Dokcerfile, "CMD", por la que le estamos dando aqui y que se ejecute este comando.

Una vez tenemos hecho esto, añadimos a nuestro repositorio el archivo. A continuación, tenemos que establecer la pila de nuestra aplicación para establecer que es un contenedor lo que vamos a subir. Para ello, ejecutamos `heroku stack:set container --app planificadordiariodocker`. 

Por último, tan solo nos queda subir al repositorio de heroku los cambios de nuestra aplicación y ya estará todo hecho. Para ello, debemos ejecutar `git push heroku master`. La salida por terminal debeŕia construir el contenedor y subir los archivos a los registros de forma automática. Cuando haya terminado, al entrar al [enlace](https://planificadordiariodocker.herokuapp.com/status) que nos proporciona heroku, nuestra aplicación deberá haberse actualizado. 