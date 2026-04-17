# ******************************************************************************************
# Clasificación de Estudiantes en Python
# Programa interactivo para registrar y clasificar calificaciones de estudiantes
# ******************************************************************************************


# Función para solicitar la cantidad de estudiantes
def solicitar_cantidad():
    while True:
        entrada = input("Ingrese la cantidad de estudiantes: ")

        if entrada.lower() == "salir":
            return None

        try:
            cantidad = int(entrada)
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser mayor que 0.")
        except ValueError:
            print("Debe ingresar un número entero válido o escribir 'salir'.")


# Función para solicitar el nombre del estudiante
def solicitar_nombre():
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()

        if nombre.lower() == "salir":
            return None

        if nombre != "":
            return nombre
        else:
            print("El nombre no puede estar vacío.")


# Función para solicitar la calificación
def solicitar_calificacion():
    while True:
        entrada = input("Ingrese la calificación (0 a 10): ")

        if entrada.lower() == "salir":
            return None

        try:
            calificacion = float(entrada)
            if 0 <= calificacion <= 10:
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 10.")
        except ValueError:
            print("Debe ingresar un número válido o escribir 'salir'.")


# Inicio del programa
print("Escriba 'salir' en cualquier momento para cerrar el programa.\n")

estudiantes = []

# Solicitar número de estudiantes a registrar
cantidad = solicitar_cantidad()

if cantidad is None:
    print("\nPrograma finalizado.")
else:
    # Bucle for usando el método range()
    for i in range(cantidad):
        print(f"\nEstudiante {i + 1}")

        # Solicitar nombre
        nombre = solicitar_nombre()
        if nombre is None:
            print("\nPrograma finalizado.")
            break

        # Solicitar calificación
        calificacion = solicitar_calificacion()
        if calificacion is None:
            print("\nPrograma finalizado.")
            break

        # Clasificación según la calificación
        if calificacion >= 9:
            clasificacion = "Excelente"
        elif calificacion >= 7:
            clasificacion = "Muy bien"
        elif calificacion >= 5:
            clasificacion = "Bien"
        else:
            clasificacion = "Insuficiente"

        # Guardar datos en el array local
        estudiantes.append((nombre, calificacion, clasificacion))


# Mostrar resultados unicamente si hay datos registrados
if len(estudiantes) > 0:
    print("\n--- LISTADO DE ESTUDIANTES ---")

    encabezados = ["Nombre", "Calificación", "Clasificación"]

    # Calcular el ancho de cada columna automáticamente
    ancho_nombre = max(len(encabezados[0]), max(len(nombre) for nombre, _, _ in estudiantes))
    ancho_calificacion = max(len(encabezados[1]), max(len(f"{calificacion:.1f}") for _, calificacion, _ in estudiantes))
    ancho_clasificacion = max(len(encabezados[2]), max(len(clasificacion) for _, _, clasificacion in estudiantes))

    # Crear separador entre filas y columnas
    separador = (
        f"+-{'-' * ancho_nombre}-+-{'-' * ancho_calificacion}-+-{'-' * ancho_clasificacion}-+"
    )

    # Imprimir encabezados de cada columna
    print(separador)
    print(
        f"| {'Nombre':<{ancho_nombre}} | "
        f"{'Calificación':<{ancho_calificacion}} | "
        f"{'Clasificación':<{ancho_clasificacion}} |"
    )
    print(separador)

    # Imprimir filas en conssola
    for nombre, calificacion, clasificacion in estudiantes:
        print(
            f"| {nombre:<{ancho_nombre}} | "
            f"{calificacion:>{ancho_calificacion}.1f} | "
            f"{clasificacion:<{ancho_clasificacion}} |"
        )

    print(separador)
