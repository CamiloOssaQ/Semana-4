# Inicialización de la estructura de datos para almacenar tareas
tareas = {}

# Función para agregar nuevas tareas
def agregar_tarea():
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_limite = input("Ingrese la fecha límite (formato dd/mm/aaaa): ")
    estado = "pendiente"
    tarea_id = len(tareas) + 1
    tareas[tarea_id] = {"descripcion": descripcion, "fecha_limite": fecha_limite, "estado": estado}
    print(f"Tarea {tarea_id} agregada con éxito.")

# Función para mostrar todas las tareas almacenadas
def listar_tareas():
    if not tareas:
        print("No hay tareas almacenadas.")
    else:
        for tarea_id, tarea in tareas.items():
            print(f"ID: {tarea_id}, Descripción: {tarea['descripcion']}, Fecha límite: {tarea['fecha_limite']}, Estado: {tarea['estado']}")

# Función para marcar una tarea como completada
def completar_tarea():
    tarea_id = int(input("Ingrese el ID de la tarea a completar: "))
    if tarea_id in tareas:
        tareas[tarea_id]["estado"] = "completada"
        print(f"Tarea {tarea_id} marcada como completada.")
    else:
        print("ID de tarea no válido.")

# Función para eliminar una tarea de la lista
def eliminar_tarea():
    tarea_id = int(input("Ingrese el ID de la tarea a eliminar: "))
    if tarea_id in tareas:
        del tareas[tarea_id]
        print(f"Tarea {tarea_id} eliminada con éxito.")
    else:
        print("ID de tarea no válido.")

# Menú principal
while True:
    print("\n----- Administrador de Tareas -----")
    print("1. Agregar Tarea")
    print("2. Listar Tareas")
    print("3. Completar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
