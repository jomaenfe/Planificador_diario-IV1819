## Documentación para publicar nuetro contenedor en Docker-hub.

### **Creación de la cuenta**:

En primer lugar debemos crearnos una cuenta en [docker-hub](https://hub.docker.com/). Una vez hemos creado una cuenta, en mi caso mi usuario es [jomaenfe](https://hub.docker.com/u/jomaenfe/). Cuando tengamos nuestra nueva cuenta vamos a "settings" y a "Linked Accounts & Services" para conectar nuestro perfil de Github. En la siguiente imagen se puede ver como quedaría el perfil después de vincular nuestras cuentas. A continuación, vamos a configurarlo para que se despliegue de forma automática cuando hagamos cambios en github.

![cuentas_sincronizadas](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/sincronizacion_cuentas.png?raw=true)

### **Configuración para despliegues automáticos**:

En primer lugar debemos hacer click en "create" y, en el menú que se despliega, damos click en "Create Automated Build" (Imagen 1). En la siguiente pantalla haremos click en github para sincronizarlo con nuestros repositorios (Imagen 2), en la lista que aparece con nuestros repositorios seleccionamos el respositorio en el que tenemos el proyecto (Imagen 3) y ya en la última pantalla ponemos la información de nuestro nuevo repositorio en docker-hub (Imagen 4). La información que ponemos en este último paso no es demasiado importante porque se puede modificar una vez ya está creado el repositorio, el cual se debería ver en vuestros repositorios de docker-hub (Imagen 5). 

![Imagen 1](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/autodespliegue_1.png?raw=true)

Imagen 1.

![Imagen 2](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/autodespliegue_2.png?raw=true)

Imagen 2.

![Imagen 3](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/autodespliegue_3.png?raw=true)

Imagen 3.

![Imagen 4](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/autodespliegue_4.png?raw=true)

Imagen 4.

![Imagen 5](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/autodespliegue_5.png?raw=true)

Imagen 5.

Una vez terminado esto, nos vamos a Github para comprobar que efectivamente en nuestro repositorio se ha creado un "webhook" de docker con el evento "push" activo. Para ello lo primero que tenemos que hacer es irnos a nuestro repositorio y hacer click en "Settings", una vez en ahí hacemos click en "Webhooks", como en la siguiente imagen deberíamos ver uno de docker con el evento "push" entre parentesis. Esto significa que ya tendríamos el despliegue automático configurado.

![Webhooks_github](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/webhooks_github.png?raw=true)

### **Desplegando nuestro contenedor**:

Para desplegar nuestro contenedor tan solo debemos subir el archivo *Dockerfile* a nuestro repositorio y automáticamente docker-hub hará el build de nuestro contenedor (obviamente si pasa los test de Travis-CI). 

