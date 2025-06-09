import json

TAREAS_FILE = "tareas.json"

def cargar_tareas():
    try:
        with open(TAREAS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open(TAREAS_FILE, "w") as f:
        json.dump(tareas, f, indent=4)

def agregar_tarea(nombre):
    tareas = cargar_tareas()
    tareas.append({"nombre": nombre, "completada": False})
    guardar_tareas(tareas)

def mostrar_tareas():
    tareas = cargar_tareas()
    for i, tarea in enumerate(tareas):
        estado = "✅" if tarea["completada"] else "❌"
        print(f"{i + 1}. {tarea['nombre']} - {estado}")

if __name__ == "__main__":
    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Escribe la tarea: ")
            agregar_tarea(nombre)
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
