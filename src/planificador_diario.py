import datetime

class Planificador_diario:

    @classmethod
    def inicializarClaseArgs(self, plan, fecha, hora_inicio, hora_fin):
        self.plan = plan
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    @classmethod
    def inicializarClase(self):
        self.plan = None
        self.fecha = None
        self.hora_inicio = None
        self.hora_fin = None

    def status(self):
        """ Funcion que se encarga de evaluar el estado de la clase """
        return True

    def modificarPlan(self,plan):
        self.plan = plan
        return self.plan
    
    def modificarFecha(self, fecha):
        self.fecha = fecha
        return self.fecha

    def modificarHorario(self, hora_inicio, hora_fin):
        self.modificarHora_inicio(hora_inicio)
        self.modificarHora_fin(hora_fin)

    def modificarHora_inicio(self, hora_inicio):
        self.hora_inicio = hora_inicio
        return self.hora_inicio

    def modificarHora_fin(self, hora_fin):
        self.hora_fin = hora_fin
        return self.hora_fin

    def mostrarPlan(self):
        print(self.plan)
        print("En el dia",self.fecha)
        print(self.hora_inicio)
        print(self.hora_fin)









