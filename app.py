import hug
import json
from src.planificador_diario import Planificador_diario

estadoSimple = {
    "status": "OK"
}

@hug.get('/')
def comprobarEstado():
        return estadoSimple
        

@hug.get('/status')
def status():
    instancia = Planificador_diario()
    value = instancia.status()

    if value==True:
        with open('status.json') as j:
            respuesta = json.load(j)
            


    return respuesta



