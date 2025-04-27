
from factory_method.crear_tareas import CrearTareaNormal, CrearTareaUrgente, CrearTareaProgramada
from Decorator.agregar_funciones_tarea import ArchivoAdjunto, Marcador, TareaProtegida
from Strategy.ordenamiento import OrdenPorFecha, OrdenPorPrioridad, OrdenPorEstado
from Contexto.contexto_tareas import contextoTarea

if __name__ == "__main__":
    # Crear tareas usando Factory
    tareas = [
        CrearTareaNormal().crear_tarea("Pagar immpuesto a la renta ", "2025-01-04", 2, "pendiente"),
        CrearTareaUrgente().crear_tarea("Enviar trabajo Taller de ingeniería de software", "2025-04-026", 1, "completada"),
        CrearTareaProgramada().crear_tarea("Programar por meet reunion para propuesta de trabajo", "2025-05-16", 3, "en progreso")
    ]

    # Aplicar Decorators
    tareas[0] = ArchivoAdjunto(tareas[0])
    tareas[1] = Marcador(tareas[1])
    tareas[2] = TareaProtegida(tareas[2])

    # Contexto que usa estrategias
    gestor = contextoTarea(OrdenPorFecha())

    print(" Tareas ordenadas por Fecha:")
    gestor.lista_tareas(tareas)

    print(" Tareas ordenadas por Prioridad:")
    gestor.ordenar_tarea_ejecucion(OrdenPorPrioridad())
    gestor.lista_tareas(tareas)

    print(" Tareas ordenadas por Estado:")
    gestor.ordenar_tarea_ejecucion (OrdenPorEstado())
    gestor.lista_tareas(tareas)
