from abc import ABC, abstractmethod

class OrdenamientoStrategy(ABC):
    @abstractmethod
    def ordenar(self, tareas: list):
        pass

class OrdenPorFecha(OrdenamientoStrategy):
    def ordenar(self, tareas: list):
        return sorted(tareas, key=lambda tarea: tarea.fecha)
    
class OrdenPorPrioridad(OrdenamientoStrategy):
    def ordenar(self, tareas: list):
        return sorted(tareas, key=lambda tarea: tarea.prioridad)
    
class OrdenPorEstado(OrdenamientoStrategy):
    def ordenar(self, tareas: list):
        return sorted(tareas, key=lambda tarea: tarea.estado)
    
   