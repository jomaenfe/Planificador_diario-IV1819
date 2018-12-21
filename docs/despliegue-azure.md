## Documentación para desplegar una aplicación en IaaS:

Para desplegar una aplicación en un IaaS, lo que hacemos nosotros es desplegar una máquina virtual, y dentro de esta máquina virtual desplegamos nuestra aplicación. Para ello, tenemos que crear la máquina virtual, aprovisionarla con lo que necesitemos para la aplicación web y por último, poder desplegar la aplicación web.

### Aprovisionamiento de la máquina virtual. Ansible.

Para este apartado, he usado [ansible](https://www.ansible.com/). Para poder crear el archivo `playbook.yml` de ansible, he seguido la [este](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html) apartado de la documentación oficial. El archivo ha quedado tal que así:

```

- hosts: all
  sudo: yes
  remote_user: jomaenfe

  tasks:
  - name: Añadir repo de python
    apt_repository: repo=ppa:deadsnakes/ppa state=present

  - name: Actualizar sistema
    command: sudo apt-get update

  - name: Instalar Git
    command: sudo apt-get install -y git
  
  - name: Instalar python version 3.6
    apt: pkg=python3.6 state=present
  
  - name: Cambiando la versión de python
    command: sudo ln -sfn /usr/bin/python3.6 /usr/bin/python

  - name: Instalar pip3
    command: sudo apt-get -y install python3-pip

  - name: Clonar GitHub
    git: repo=https://github.com/jomaenfe/Planificador_diario-IV1819.git  dest=planificador-diario/ force=yes

  - name: Instalar requirements
    command: pip3 install -r planificador-diario/requirements.txt

```

Lo que hace principalmente es preparar la máquina para que pueda ejecutar nuestra aplicación sin problemas. Es por esto que en el archivo se instalan ciertas aplicaciones y dependencias que se necesitan en el sistema para el funcionamiento de la aplicación. Entre ellas, se instala python 3.6, pip3 (para instalar módulos de python), git para clonar el repositorio y también se cambia la versión de python en la estructura del sistema para que todo funcione correctamente.

Al principio del archivo, podemos ver `host: all`. Esto se refiere a que para todos los host, en nuestro caso sólo tendremos el de nuestra máquina virtual, podrán ejecutar este archivo de aprovisionamiento. El archivo host se encuentra en la dirección `/etc/ansible/hosts` y para añadir un nuevo host debemos hacerlo como se muestra:

```
[planificador]
planificador-diario-iv1819.westeurope.cloudapp.azure.com
```

El nombre que identifica al host va entre corchetes y el host justo debajo, puede ser tanto la ip como la dirección. En mi caso, he usado la dirección.

### Despliegue de la máquina virtual y aprovisionamiento. Vagrant.

Como yo he usado azure para desplegar la máquina virtual, tengo que poder enlazar vagrant con azure. Para ello voy a usar el plugin de [vagrant-azure](https://github.com/Azure/vagrant-azure). En esta guía viene bien documentado todo lo que tenemos que hacer para poder configurar este plugin y conseguir desplegar nuestra máquina virtual en azure de forma automática.

En primer lugar, tenemos que instalar el CLI de azure, en esta [web](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) viene explicado como instalarlo y también el plugin de vagrant azure, ejecutando `vagrant install plugin vagrant-azure`.

Cuando lo tengamos instalado, el siguiente paso será loguearnos, para ello ejecutamos `az login`, tras esto, se nos abrirá una ventana en el navegador donde nos podremos autenticar. Después de autenticarnos, en la terminal saldrán las subscripciones que tenemos. En mi caso, como se puede ver en la **imagen 1**, salen las dos que nos ha proporcionado JJ.

Para poder ver, las subscripciones que tenemos y copiar la `id` de las mismas, ejecutamos `az account list`, y nos dará una salida como la que se puede ver en la imagen 1.

![Imagen_1](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/azaccount.png?raw=true)

Imagen 1.

Después de loguearnos procedemos a crear un directorio activo de azure (AAD). Este directorio, nos dará claves para que nosotros podamos dárselas a vagrant. Con estas claves, vagrant se conectará con nuestra cuenta de azure y hará el despliegue y aprovisionamiento de la máquina. En primer lugar, debemos obtener la `id` de la subscripción donde queremos que se cree la máquina virtual. Para ello ejecutamos `az account list --query "[?isDefault].id" -o tsv` y nos dará una salida como la que se puede ver en la **imagen 2**.

![Imagen 2](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/azaccountid.png?raw=true)

Imagen 2.

Debemos guardar la salida del comando anterior para poder continuar. Ahora ejecutamos el comando `az ad sp create-for-rbac --name planificador-diario-iv1819` que creará el directorio AAD del que hemos hablado anteriormente. La salida de este comando debería ser como la de la imagen 3.

![Imagen 3](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/appsid.png?raw=true)

Imagen 3.

Una vez tenemos todos estos parámetros a mano, creamos el vagrantfile. Es muy parecido al que tenemos en el tutorial que he citado anteriormente. Quedaría tal que así:

```
Vagrant.configure('2') do |config|
  config.vm.box = 'azure'

  # Claves ssh para conectarse a la máquina.
  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.vm.provider :azure do |azure, override|

    # Estas varibles tenemos que exportarlas, son las variables que se encargan de identificar la cuenta de azure
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    #Variables para modificar la información de la máquina virtual.
    azure.vm_name = "planificador-diario-iv1819"
    azure.vm_size = "Basic_A2"
    azure.tcp_endpoints = "80"
    azure.location = "westeurope"
    azure.admin_username = "jomaenfe"

  end

  # Aquí es donde aprovisionamos la máquina cuando la creamos
  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provision/playbook.yml"
  end

end
```

Las variables que van predecidas de `ENV` son variables que debemos exportar. Ahora, para relacionar las variables que hemos sacado y las que debemos darle a cada cosa, sería tal que así:
- AZURE_TENANT_ID = tenant
- AZURE_CLIENT_ID = appId
- AZURE_CLIENT_SECRET = password
- AZURE_SUBSCRIPTION_ID = al valor que hemos obtenido ejecutando `az account list --query "[?isDefault].id" -o tsv`.

Yo he incluido más variables que sirven para darle información adicional a la máqina virtual. Como por ejemplo el nombre y el nombre del DNS, las caracterísitcas de la máquina, el puerto que debemos abrir , la localización y el nombre de usuario del administrador.

Una vez hemos exportado las variables, tan solo nos quedaría ejecutar `vagrant up --provider=azure` y se encargará de crear la máquina automátiamente. En la **imagen 4** podemos ver cómo se crea la máquina y se aprovisiona.

![Imagen_4](https://github.com/jomaenfe/Planificador_diario-IV1819/blob/master/docs/img/aprovisionamientovagrant.png?raw=true)


### Desplegar la aplicación. Fabfile.

Para desplegar la aplicación desde dentro de la máquina web, hemos usado [Fabric](http://docs.fabfile.org/en/1.14/index.html), y he seguido la [documentación](http://docs.fabfile.org/en/1.14/tutorial.html) para usarla. Como lo voy a usar para lanzar la aplicación desde dentro de la máquina virtual, el archivo que he tenido que hacer es bastante simple.

```

# Fabfile to:
#    - Actualizar
#    - Iniciar
#    - Detener

# Este import puede dar problemas si estamos usando python 3.x, para que no los de
# debemos instalar pip3 y como módulo instalar fabric3
from fabric.api import *

# En el caso de tener que actualizar el código, el primer paso sería borrar lo que tenemos, en segundo paso volver a clonar la app
# y como tercer paso instalar los requerimientos por si han cambiado.
def Actualizar():

    run('sudo rm -rf Planificador_diario-IV1819')

    run('git clone https://github.com/jomaenfe/Planificador_diario-IV1819.git')  

    run('pip3 install -r Planificador_diario-IV1819/requirements.txt')

# Para iniciar el servicio web usamos esta función.
def Iniciar():

    
     run('cd Planificador_diario-IV1819/ && sudo gunicorn app:__hug_wsgi__ -b 0.0.0.0:80')

# Para detener el servicio web usamos esta función.
def Detener():
    run('cd Planificador_diario-IV1819/despliegue/ && sudo sh script_detener.sh')

```

Este archivo tan solo sirve, para actualizar la aplicación en caso de que se cambie el código. Donde lo que hace es borrar lo que tiene, volver a descargarse el repositorio e instalar las dependencias. Iniciar el servicio, arrancar el servidor gunicorn y, para el servidor gunicorn. Para para el servidor gunicorn, he tenido que buscar un script que lo que hace es matar el servicio que tienen un id asociado a gunicorn. Este script lo he cogido de [aqui](http://cheng.logdown.com/posts/2015/04/17/better-way-to-run).

Para acceder y modificar el estado de la aplicación ejecutamos `ab -f despliegue/fabfile.py -H vagrant@planificador-diario-iv1819.westeurope.cloudapp.azure.com [orden]`, donde en orden debemos poner "Actualizar", "Iniciar" o "Detener" según se necesite. Y con esto podremos manejar la máquina a distancia y sin tener que acceder manualmente a ella.

