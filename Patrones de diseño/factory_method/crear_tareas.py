
from abc import ABC, abstractmethod
from factory_method.tareas import TareaNormal , TareaUrgente , TareaProgramada

class CrearTarea(ABC): #  Aplicando el factory method    con creador de tareas
    def crear_tarea(self, nombre, fecha, prioridad, estado):
     pass

    def IndicarPrioridad(self):
        tarea = self.crear_tarea()
        result = f"{tarea.prioridad()}"
        return result 
    
class  CrearTareaNormal(CrearTarea):
    def crear_tarea(self, nombre, fecha, prioridad, estado):
        return TareaNormal(nombre, fecha, prioridad, estado)   


class  CrearTareaUrgente(CrearTarea):
    def crear_tarea(self, nombre, fecha, prioridad, estado):
        return TareaUrgente( nombre, fecha, prioridad, estado)   

class  CrearTareaProgramada(CrearTarea):
    def crear_tarea(self, nombre, fecha, prioridad, estado):
        return TareaProgramada(nombre, fecha, prioridad, estado)   