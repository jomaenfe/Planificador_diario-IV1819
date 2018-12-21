# Fabfile to:
#    - Actualizar
#    - Iniciar

# Este import puede dar problemas si estamos usando python 3.x, para que no los de
# debemos instalar pip3 y como módulo instalar fabric3
from fabric.api import *

# En el caso de tener que actualizar el código, el primer paso sería borrar lo que tenemos, en segundo paso volver a clonar la app
# y como tercer paso instalar los requerimientos por si han cambiado.
def Actualizar():

    run('sudo rm -rf planificador-diario')

    run('git clone https://github.com/jomaenfe/Planificador_diario-IV1819.git')  

    run('pip3 install -r Planificador_diario-IV1819/requirements.txt')

# Para iniciar el servicio web usamos esta función.
def Iniciar():

    
     run('cd Planificador_diario-IV1819/ && sudo gunicorn app:__hug_wsgi__ -b 0.0.0.0:80')

# Para detener el servicio web usamos esta función.
def Detener():
    run('cd Planificador_diario-IV1819/ && sudo sh parar.sh')