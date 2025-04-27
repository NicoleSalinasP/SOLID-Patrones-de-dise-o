from factory_method.tareas import Tarea

class DecoratorTarea(Tarea):
    def __init__(self,tarea : Tarea):
        self._tarea = tarea
        super().__init__(tarea.nombre, tarea.fecha, tarea.prioridad, tarea.estado)


    def descripcion(self):
            return self._tarea.descripcion()
    
class ArchivoAdjunto(DecoratorTarea):
    def descripcion(self):
        return  self._tarea.descripcion() + "\nTiene un archivo adjunto  "
    
class Marcador(DecoratorTarea):
    def descripcion(self):
        return  self._tarea.descripcion() + " \nMarcada como importante "
    
class TareaProtegida(DecoratorTarea):
    def descripcion(self):
        return self._tarea.descripcion() + "\nEsta Tarea requiere un permiso asignado" 