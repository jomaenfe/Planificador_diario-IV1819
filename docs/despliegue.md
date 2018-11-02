## DESPLIEGUE EN HEROKU

Yo he desplegado la aplicación web en heroku, me he decidido por este PaaS ya que proporciona mucha documentación y turoriales a seguir para su uso. En mi opinión está bastante completo y este ha sido el principal incentivo para decidirme por él. Para mi despliegue he seguido el [tutorial](https://devcenter.heroku.com/articles/getting-started-with-python) que nos proporciona heroku. Donde usamos uno de sus repositorios para probar un despliegue rápido y comprender sus principales funcionalidades. 

Voy a explicar un poco los pasos que he seguido para desplegar la aplicación con heroku:

### PROCEDIMIENTO

1. **Registro en Heroku** 
    
    En primer lugar tenemos que entrar en la página y registrarnos. 
    [Heroku login](https://signup.heroku.com/login?redirect-url=https%3A%2F%2Fid.heroku.com%2Foauth%2Fauthorize%3Fclient_id%3D1e7d4c52-6008-4a73-b132-09abb5d04859%26response_type%3Dcode%26scope%3Dglobal%252Cplatform%26state%3DSFMyNTY.g3QAAAACZAAEZGF0YW0AAAAxaHR0cHM6Ly9kYXNoYm9hcmQuaGVyb2t1LmNvbS9hdXRoL2hlcm9rdS9jYWxsYmFja2QABnNpZ25lZG4GAHcarsRmAQ.0XivXF_mTSVVsQSU5WwWutefChzM46-0W5qoZ7agEhw) 

2. **Creación de la aplicación**
    
    Una vez nos hemos registrado, tendremos que crear la aplicación. En el tutorial nos dice que debemos instalar heroku en nuestra máquina para poder usarlo por línea de comandos. Para instalarlo solo debemos teclear en la terminal `sudo snap install heroku --classic`. Una vez este instalado nos logueamos con `heroku login`, escribimos nuestros credenciales y ya estaríamos dentro de nuestra cuenta. Para crear la aplicacion yo he seguido el tutorial anteriormente expuesto y en la terminal he escrito `heroku create planificadordiario` y esto nos retornará un enlace. En mi caso este es el [`https://planificadordiario.herokuapp.com/`](https://planificadordiario.herokuapp.com/)


3. **Configuración con github**

    En este punto, se supone que ya deberíamos haber creado la aplicación. Cuando accedemos a nuestra cuenta de heroku desde el navegador web debería aparecernos nuestra aplicación. 

    ![paginaprincipal](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/principalheroku.png?raw=true)

    Dentro de nuestra aplicación debemos hacer click en **deploy** y en esa misma ventana, más abajo veremos **deployment method**. Aqui marcamos github y entramos con nuestras credenciales de github. Buscamos nuestro repositorio y lo conectamos también. Una vez está conectado deberíamos ver algo tal como se ve en la siguiente imagen.

    ![deplymethod](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/deployment.png?raw=true)

    Cuando ya esté conectado con nuestro repositorio debemos activar los "despliegues automáticos", en la imagen anterior están justo debajo de nuestro repositorio. Esto lo hacemos para que cuando se haga un push en nuestro repositorio también se despliegue de forma automática. Por último, también activamos **Wait for CI to pass before deploy** para que sólo lo suba a heroku si ha pasado los test que tenemos programados. 


4. **Crear archivo Procfile**

    En este archivo le indicamos que app debe ejecutar el servidor. Esto sirve para probar la aplicación de forma local (antes de subirla a heroku) y para que se ejecute en heroku de forma correcta también. El contenido de este archivo es:

    `web: gunicorn app:__hug_wsgi__ --log-file -`

5. **Actualizar las dependencias**

    Antes de probar la aplicación debemos comprobar que las depencias están todas en el archivo `requirements.txt` para que las descargue y el proyecto funcione de forma correcta. En mi caso, el contenido de este archivo es:

    ```
    atomicwrites==1.2.1
    attrs==18.2.0
    DateTime==4.3
    more-itertools==4.3.0
    pluggy==0.7.1
    py==1.6.0
    pytest==3.8.2
    pytz==2018.5
    six==1.11.0
    zope.interface==4.5.0
    hug
    gunicorn
    ```


6. **Comprobar que la aplicación esta desplegada**

    Una vez tenemos la aplicación implementada y hemos probado que funciona correctamente en local, tan solo nos quedaría hacer un push a github y automáticamente se nos desplegará en heroku. En mi caso, mi aplicación está en este [enlace](https://planificadordiario.herokuapp.com/)