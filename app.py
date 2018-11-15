import hug
import json
from src.planificador_diario import Planificador_diario

estadoSimple = {
    "status": "OK",
    "ejemplo": {
            "ruta":"/status",
            "valor":"{ 'dia': '09', 'mes':'11', 'anio':'2018', 'plan': 'celebrar cumpleanios', 'hora_inicio': '21', 'minuto_inicio':'00', 'hora_fin':'23', 'minuto_fin':'30' }"
    } 

}

@hug.get('/')
def comprobarEstado():
        return estadoSimple
        

@hug.get('/status')
def status():
    instancia = Planificador_diario()
    value = instancia.status()

    if value==True:
        with open('planEjemplo.json') as j:
            respuesta = json.load(j)


    return respuesta



