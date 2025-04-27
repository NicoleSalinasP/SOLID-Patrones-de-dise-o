from abc import ABC, abstractmethod

class Tarea(ABC):
     def __init__(self, nombre, fecha, prioridad, estado):
        self.nombre = nombre
        self.fecha = fecha
        self.prioridad = prioridad
        self.estado = estado
         
        @abstractmethod
        def descripcion(self):
            pass

class TareaNormal(Tarea):
    def descripcion(self):
        return f"Tarea Normal: {self.nombre}."
    

class TareaUrgente(Tarea):
    def descripcion(self):
        return f"Tarea Normal: {self.nombre}."


class TareaProgramada(Tarea):
    def descripcion(self):
        return f"Tarea Normal: {self.nombre}."