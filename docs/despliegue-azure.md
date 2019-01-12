## Documentación para desplegar una aplicación en IaaS:

Para desplegar una aplicación en un IaaS, lo que hacemos nosotros es desplegar una máquina virtual, y dentro de esta máquina virtual desplegamos nuestra aplicación. Para ello, tenemos que crear la máquina virtual, aprovisionarla con lo que necesitemos para la aplicación web y por último, poder desplegar la aplicación web.

### Aprovisionamiento de la máquina virtual. Ansible.

Para este apartado, he usado [ansible](https://www.ansible.com/). Para poder crear el archivo `playbook.yml` de ansible, he seguido varios apartados de la documentación oficial. En el mismo archivo está explicado que hace cada paso que doy. Los apartados de la guía que he seguido son los siguientes: [apt_repository](https://docs.ansible.com/ansible/latest/modules/apt_repository_module.html), [apt](https://docs.ansible.com/ansible/latest/modules/apt_module.html), [git](https://docs.ansible.com/ansible/latest/modules/git_module.html) y [command](https://docs.ansible.com/ansible/latest/modules/command_module.html).

En cada uno de ellos, viene una tabla en la que especifica para que sirve cada parámetro de cada apartado. Y, también, varios ejemplos de como usar cada uno de ellos. Mi archivo fabfile se ha basado en los ejemplos que hay en cada uno de los anteriores enlaces, para poder instalar todo lo necesario y que mi aplicación funcione en la máquina virtual.

```

- hosts: all       # Especifico que este archivo es valido para todos los hosts.
  become: true     # Permito entrar en modo superusuario para las siguientes tareas.
  
  # Tareas que voy a ejecutar para provisionar la máquina.
  tasks:

  - name: Añadir repo de python
    apt_repository: # Añado un repositorio con la versión 3.6 de python.
        repo: ppa:jonathonf/python-3.6 #Donde se encuentra el repositorio.
        state: present  # Verifica si está o no presente en el sistema, si no lo está lo añade y si lo está no hace nada.

  - name: Actualizar sistema
    apt: # Para trabajar con paquetes, como en Ubuntu.
        update_cache: yes # Esto ejecuta "apt-get update".

    # Comprueba si está instalado git, si no lo está lo instala y si lo está lo ignora.
  - name: Instalar Git
    apt: 
        name: git 
        state: present
        
    # Comprueba si está instalado python3.6, si no lo está lo instala y si lo está lo ignora.
  - name: Instalar python version 3.6
    apt: 
        name: python3.6 
        state: present
  
    # Cambio el path de la versión de python porque yo uso python3.
  - name: Cambiar version
    command: ln -sfn /usr/bin/python3.6 /usr/bin/python    

    #Instala pip3.
  - name: Instalar pip3
    become: true
    apt: 
      pkg: python3-pip 
      state: latest # Instala o comprueba que el paquete está instalado en su última versión.

    # Clono mi repositorio de github en la máquina.
  - name: Clonar GitHub
    git: 
        repo: https://github.com/jomaenfe/Planificador_diario-IV1819.git  
        dest: planificador-diario/ # Path de destino donde se clonará el repositorio.

    # Instalo dependencias para mi proyecto.
  - name: Instalar requirements
    command: pip3 install -r planificador-diario/requirements.txt 

```

Lo que este archivo hace principalmente es preparar la máquina para que pueda ejecutar nuestra aplicación sin problemas. Es por esto que en el archivo se instalan ciertas aplicaciones y dependencias que se necesitan en el sistema para el funcionamiento de la aplicación. Entre ellas, se instala python 3.6, pip3 (para instalar módulos de python), git para clonar el repositorio y también se cambia la versión de python en la estructura del sistema para que todo se ejecute con python3 directamente.

Al principio del archivo, podemos ver `host: all`. Esto se refiere a que para todos los host, en nuestro caso sólo tendremos el de nuestra máquina virtual, podrán ejecutar este archivo de aprovisionamiento. El archivo host se encuentra en la dirección `/etc/ansible/hosts`, y para añadir un nuevo host debemos hacerlo como se muestra:

```
[planificador]
planificador-diario-1819.westeurope.cloudapp.azure.com
```

El nombre que identifica al host va entre corchetes y el host va justo debajo; puede ser tanto la ip como la dirección. En mi caso, he usado la dirección.

### Despliegue de la máquina virtual y aprovisionamiento. Vagrant.

Como yo he usado azure para desplegar la máquina virtual, tengo que poder enlazar vagrant con azure. Para ello voy a usar el plugin de [vagrant-azure](https://github.com/Azure/vagrant-azure). En esta documentación viene bien explicado todo lo que tenemos que hacer para poder configurar este plugin y conseguir desplegar nuestra máquina virtual en azure de forma automática.

En primer lugar, tenemos que instalar el CLI de azure, en esta [web](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) viene explicado como instalarlo.


Una vez tengamos instalado el CLI de azure, el siguiente paso será loguearnos, para ello ejecutamos `az login`, tras esto, se nos abrirá una ventana en el navegador donde nos podremos autenticar. Después de autenticarnos, en la terminal saldrán las subscripciones que tenemos. En mi caso, como se puede ver en la **imagen 1**, salen las que nos ha proporcionado JJ.

Para poder ver las subscripciones que tenemos y copiar la `id` de las mismas, ejecutamos `az account list`, y nos dará una salida como la que se puede ver en la imagen 1.

![Imagen_1](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/azaccount.png?raw=true)

Imagen 1.

Después de loguearnos procedemos a crear un directorio activo de azure (AAD). Este directorio, nos dará claves para que nosotros podamos dárselas a vagrant. Con estas claves, vagrant se conectará con nuestra cuenta de azure y hará el despliegue y aprovisionamiento de la máquina. En primer lugar, debemos obtener la `id` de la subscripción donde queremos que se cree la máquina virtual. Para ello ejecutamos `az account list --query "[?isDefault].id" -o tsv` y nos dará una salida como la que se puede ver en la **imagen 2**.

![Imagen 2](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/azaccountlist.png?raw=true)

Imagen 2.

Debemos guardar la salida del comando anterior para poder continuar. Ahora ejecutamos el comando `az ad sp create-for-rbac --name planificador-diario-iv1819` que creará el directorio AAD del que hemos hablado anteriormente. La salida de este comando debería ser como la de la imagen 3.

![Imagen 3](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/appsid.png?raw=true)

Imagen 3.

Una vez tenemos todos estos parámetros a mano procedemos con la instalación del plugin de vagrant. En primer lugar ejecutamos el siguiente comando `vagrant box add azure-vagrant-box https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure`. La utilidad de este comando reside en descargar el repositorio al que está enlazado para que vagrant lo use como base a la hora de ejecutar el vagrantfile más adelante. Las [boxes](https://www.vagrantup.com/docs/boxes.html) de vagrant son paquetes de formato para diferentes entornos, en nuestro caso azure. Cuando se añade, debemos ver una salida en pantalla como la siguiente:

![Add_box](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/descargo-box.png?raw=true)

Después de añadir esta información, procedemos a instalar el plugin ejecutando `vagrant install plugin vagrant-azure`.

Ahora creamos el vagrantfile. Tomando como modelo el vagrantfile que hay en la [documentación](https://github.com/Azure/vagrant-azure), y adaptándolo a nuestro proyecto; quedaría tal que así:

```
# Usamos la versión 2 del plugin azure-vagrant.
Vagrant.configure('2') do |configuracion| # Variable de configuración para modificar la configuración de la "box" y claves que vamos a usar.
  configuracion.vm.box = 'azure-vagrant-box' # Usamos como base para el funcionamiento de vagrant la "box" que hemos añadido a la configuración anteriormente.

  # Claves ssh para conectarse a la máquina.
  configuracion.ssh.private_key_path = '~/.ssh/id_rsa' # Cogemos la clave ssh almacenada en esta ruta de nuestro sistema para conectarnos a la máquina
                                                       # sin necesidad de contraseña.
  
  
  configuracion.vm.provider :azure do |planificador_diario, override| # Creo la variable planificador_diario a partir del topicalizador de azure para 
                                                                      # poder darle información al proveedor tanto de variables para la conexión a 
                                                                      # nuestra cuenta como de parámetros para la creación de nuestra máquina virtual. 

    # Estas varibles tenemos que exportarlas, son las variables que se encargan de identificar la cuenta de azure
    planificador_diario.tenant_id = ENV['id_tenant']
    planificador_diario.client_id = ENV['id_cliente']
    planificador_diario.client_secret = ENV['passw_cliente']
    planificador_diario.subscription_id = ENV['id_subscripcion']

    #Variables para modificar la información de la máquina virtual.
    planificador_diario.vm_name = "planificador-diario-iv1819" # Con esto modifico el nombre de nuestra máquina virtual.
    planificador_diario.vm_size = "Basic_A2" # Este es el identificador del hardware que va a usar la máquina. 
    planificador_diario.tcp_endpoints = "80" # Abro el puerto 80 en la máquina.
    planificador_diario.location = "westeurope" # Defino el lugar donde estará ubicada la máquina.
    planificador_diario.admin_username = "jomaenfe" # Defino el nombre de usuario del adminsitrador de la máquina virtual.

  end

  # Aquí es donde aprovisionamos la máquina cuando la creamos
  configuracion.vm.provision :ansible do |provisionamiento| # Creo la variable "provisionamiento" a partir del topicalizador de ansible, con la que 
                                                            # haremos la provisión de nuestra máquina una vez creada y funcionando.
  
     provisionamiento.playbook = "provision/playbook.yml" # Provisiono la máquina virtual.
  end

end
```

Cada línea del vagrantfile tiene una explicación comentada de lo que hace. Mucha información la he sacado de la [documentación](https://github.com/Azure/vagrant-azure) que he ido siguiendo, el resto de la información la saqué de una tutoría con JJ, y de algunos enlaces que se han pasado por el grupo de la asignatura: [topicalizadores](https://stackoverflow.com/questions/7065421/could-implicit-topics-be-implemented-cleanly-in-a-language/7066007#7066007).

Las variables que van precedidas por `ENV` son variables que debemos exportar en el entorno de nuestra terminal. Ahora, para relacionar las variables que hemos sacado y las que debemos darle a cada cosa, sería tal que así:
- id_tenant = tenant
- id_cliente = appId
- passw_cliente = password
- id_subscripcion = el valor que hemos obtenido ejecutando `az account list --query "[?isDefault].id" -o tsv`.

Yo he incluido más variables que sirven para darle información adicional a la máqina virtual. Como por ejemplo el nombre y el nombre del DNS, las caracterísitcas de la máquina, el puerto que debemos abrir , la localización y el nombre de usuario del administrador.

Una vez hemos exportado las variables, tan solo nos quedaría ejecutar `vagrant up --provider=azure` y se encargará de crear la máquina automátiamente. En la **imagen 4** podemos ver cómo se crea la máquina y se aprovisiona.

![Imagen_4](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/aprovisionamientoycreacion.png?raw=true)

Imagen 4.


### Desplegar la aplicación. Fabfile.

Para desplegar la aplicación desde dentro de la máquina virtual, hemos usado [Fabric](http://docs.fabfile.org/en/1.14/index.html), y he seguido la siguiente documentación de [digital ocean](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments) para crear mi archivo. Dentro de esta documentación vienen varios apartados donde se explican distintas ordenes y formas para crear el fabfile, con sus respectivos ejemplos. En mi caso, he seguido las siguientes: sudo,run y cd; que se encuentran dentro de este [apartado](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments#fabric's-features-and-integration-with-ssh).

```

# Fabfile que sirve para:
#    - Actualizar la aplicación
#    - Iniciar la aplicación
#    - Detener la aplicación

# Para crear este archivo, he seguido el modelo de la siguiente documentación 
# https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments#example-fabfile-for-automating-management-tasks


# Este módulo puede dar problemas si estamos usando python 3.x, para que no los de
# debemos instalar pip3 y como módulo instalar fabric3
from fabric.api import *

# Aqui van los host a los que se va a conectar para desplegar, o hacer cambios.
env.hosts = [
     'planificador-diario-1819.westeurope.cloudapp.azure.com',
]

# Defino el nombre de usuario para que se conecte a la máquina virtual.
env.user = 'vagrant'


# En el caso de tener que actualizar el código, el primer paso sería borrar lo que tenemos, en segundo paso volver a clonar la app
# y como tercer paso instalar los requerimientos por si han cambiado.
# En el caso de tener que actualizar el código, el primer paso sería borrar lo que tenemos, en segundo paso volver a clonar la app
# y como tercer paso instalar los requerimientos por si han cambiado.
def Actualizar():

    sudo('rm -rf Planificador_diario-IV1819') # Ejecutamos el comando con sudo.

    resultado_orden = run('git clone https://github.com/jomaenfe/Planificador_diario-IV1819.git') # Almacenamos el resultado de la operación en una variable.
     
    if not resultado_orden.failed:
     # Elimino información innecesaria para el funcionamiento de la aplicación.
     with cd('Planificador_diario-IV1819/'): # Si se ha clonado el repositorio correctamente hacemos lo siguiente.
          sudo('rm -rf docs')
          run('rm .gitignore .travis.yml Dockerfile Procfile README.md Vagrantfile heroku.yml')
     run('pip3 install -r Planificador_diario-IV1819/requirements.txt') # Comprobamos si la ejecución anterior ha sido correcta y en ese caso, instalamos los requerimientos.

# Para iniciar el servicio web usamos esta función.
def Iniciar():

    with cd('Planificador_diario-IV1819/'): # Con witd cd, lo que estmamos haciendo es mantener la sesión en esa carpeta para ejecutar después gunicorn.
     run('sudo sh iniciar_gunicorn.sh')

# Para detener el servicio web usamos esta función.
def Detener():
    
    with cd('Planificador_diario-IV1819/scripts/'): # Exactamente igual que antes, solo que para detener gunicorn.
     run('sudo sh script_detener.sh')

```

Este archivo tan solo sirve; para actualizar la aplicación en caso de que se cambie el código. Donde lo que hace es borrar lo que tiene, volver a descargarse el repositorio, borrar lo que no sirve para la ejecución de la aplicación en sí, e instalar las dependencias. Iniciar el servicio, arrancar el servidor gunicorn y, parar el servidor gunicorn. Para poder detener el servidor de gunicorn he usado el flag `-p archivo.pid`. Este flag lo que hace es almacenar en el archivo que se le pasa el pid de ejecución de gunicorn,el pid lo uso después para poder matar sólo ese proceso cuando queramos terminar la ejecución. Para terminar la ejecución uso un script simple que hay almacenado en la carpeta `scripts`:

```

#!/bin/bash

kill -9 $(cat appid.pid) # Leemos el archivo appid.pi donde tenemos almacenado el pid con el que se ha iniciado gunicorn
                         # y matamos el proceso para parar su ejecución.

```

También, como es referenciado en la sección de [preguntas frecuentes](http://www.fabfile.org/faq.html) de fabfile, en la parte en la que explica porque no puedes ejecutar un programa en segundo plano. He tenido que crear un [script](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/iniciar_gunicorn.sh) en la raiz de mi proyecto que se encarga de arrancar el servidor para que funcione en segundo plano.

```
exec gunicorn -p scripts/appid.pid app:__hug_wsgi__ -b 0.0.0.0:80 --daemon
```

Para acceder y modificar el estado de la aplicación ejecutamos `fab <orden>`, donde en orden debemos poner "Actualizar", "Iniciar" o "Detener" según se necesite. Y con esto podremos manejar la máquina a distancia y sin tener que acceder manualmente a ella. Como ejemplo, en las siguientes capturas voy a iniciar y a detener el servicio con fab.

![Iniciar_Servicio](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/Iniciofabfile.png?raw=true)

![Detener_Servicio](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/detenerfab.png?raw=true)

