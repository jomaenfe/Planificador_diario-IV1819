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
def Actualizar():

    sudo('rm -rf Planificador_diario-IV1819') # Ejecutamos el comando con sudo.

    resultado_orden = run('git clone https://github.com/jomaenfe/Planificador_diario-IV1819.git') # Almacenamos el resultado de la operación en una variable.
     
    if not resultado_orden.failed:
     # Elimino información innecesaria para el funcionamiento de la aplicación.
     with cd('Planificador_diario-IV1819/'): # Si se ha clonado el repositorio correctamente hacemos lo siguiente.
          sudo('rm -rf docs')
          run('rm .gitignore .travis.yml Dockerfile Procfile README.md Vagrantfile heroku.yml LICENSE')
     run('pip3 install -r Planificador_diario-IV1819/requirements.txt') # Comprobamos si la ejecución anterior ha sido correcta y en ese caso, instalamos los requerimientos.

# Para iniciar el servicio web usamos esta función.
def Iniciar():

    with cd('Planificador_diario-IV1819/'): # Con witd cd, lo que estmamos haciendo es mantener la sesión en esa carpeta para ejecutar después gunicorn.
     run('sudo sh iniciar_gunicorn.sh')

# Para detener el servicio web usamos esta función.
def Detener():
    
    with cd('Planificador_diario-IV1819/scripts/'): # Exactamente igual que antes, solo que para detener gunicorn.
     run('sudo sh script_detener.sh')
