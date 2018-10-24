import datetime
from pytest import fixture

@fixture
def op():
    from planificador.planificador_diario import Planificador_diario
    return Planificador_diario("Irme al bar", datetime.date.today(), datetime.time(19,00), datetime.time(22,00))

def test_modificarPlan(op):
    assert op.modificarPlan("hola") == "hola"

def test_modificarFecha(op):
    #Comprobamos que es un dato del tipo fecha
    assert isinstance(op.modificarFecha(datetime.date.today()),datetime.date)

def test_modificarHoraInicio(op):
    #Comprobamos que el dato es de tipo hora
    assert isinstance(op.modificarHora_inicio(datetime.time(20,00)), datetime.time)

def test_modficarHoraFin(op):
    #Comprobamos que el dato es de tipo hora
    assert isinstance(op.modificarHora_fin(datetime.time(20,00)), datetime.time)



