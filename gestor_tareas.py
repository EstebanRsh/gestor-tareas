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

def completar_tarea(indice):
    tareas = cargar_tareas()
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        guardar_tareas(tareas)

def eliminar_tarea(indice):
    tareas = cargar_tareas()
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        guardar_tareas(tareas)
def buscar_tareas(palabra):
    tareas = cargar_tareas()
    for i, tarea in enumerate(tareas):
        if palabra.lower() in tarea["nombre"].lower():
            estado = "✅" if tarea["completada"] else "❌"
            print(f"{i + 1}. {tarea['nombre']} - {estado}")
def mostrar_filtradas(completadas=True):
    tareas = cargar_tareas()
    for i, tarea in enumerate(tareas):
        if tarea["completada"] == completadas:
            estado = "✅" if tarea["completada"] else "❌"
            print(f"{i + 1}. {tarea['nombre']} - {estado}")


if __name__ == "__main__":
    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Buscar tarea")
        print("6. Mostrar solo completadas")
        print("7. Mostrar solo pendientes")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Escribe la tarea: ")
            agregar_tarea(nombre)
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            mostrar_tareas()
            indice = int(input("Número de tarea a completar: ")) - 1
            completar_tarea(indice)
        elif opcion == "4":
            mostrar_tareas()
            indice = int(input("Número de tarea a eliminar: ")) - 1
            eliminar_tarea(indice)
        elif opcion == "5":
            palabra = input("Ingresa palabra clave: ")
            buscar_tareas(palabra)
        elif opcion == "6":
            mostrar_filtradas(completadas=True)
        elif opcion == "7":
            mostrar_filtradas(completadas=False)
        elif opcion == "0":
            print("Guardando tareas...")
            break
        else:
            print("Opción inválida.")
