from Strategy.ordenamiento import OrdenamientoStrategy

class contextoTarea():
 def __init__(self, ordenar_tarea: OrdenamientoStrategy):
     self._ordenar_tarea = ordenar_tarea
     
 def ordenar_tarea_ejecucion (self, ordenar_tarea :OrdenamientoStrategy):
     self._ordenar_tarea = ordenar_tarea       

 def lista_tareas(self, tareas : list):
     tareas_por_orden = self._ordenar_tarea.ordenar(tareas)
     for tarea in tareas_por_orden:
        print (f"{tarea.descripcion()}\nFecha: {tarea.fecha} - Prioridad: {tarea.prioridad} - Estado : {tarea.estado}\n")
     