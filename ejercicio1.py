#Enunciado parcial 4 forma C
#Definiendo funciones
#Funciones de validacion
def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_copias(copias):
    try:
        cantidad = int(copias)
        return cantidad >= 0
    except ValueError:
        return False

def validar_prestamo(prestamos):
    try:
        cantidad = int(prestamos)
        return cantidad > 0
    except ValueError:
        return False

#Funciones del menu
def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opción inválida. Ingrese un número entre 1 y 6.")
        except ValueError:
            print("Debe ingresar un número entero.")
 
 #Funciones de las opciones del menu
def agregar_libro(libros):
    titulo = input("Ingrese el nombre del libro: ")
    copias = input("Ingrese la cantidad de copias: ")
    prestamo = input ("Ingrese el periodo de prestamo del libro: ")
    if not validar_titulo(titulo):
        print("Error: El nombre no puede estar vacío ni ser solo espacios en blanco.")
        return
    if not validar_copias(copias):
        print("Error: Las copias deben ser un número entero mayor o igual a cero.")
        return
    if not validar_prestamo(prestamo):
        print("Error: El período de préstamo debe ser un número entero mayor que cero.")
        return
    
    libro = {
        "titulo": titulo.strip(),
        "copias": int(copias),
        "prestamo": int(prestamo),
        "disponible": False
    }
    libros.append(libro)
    print(f"¡Libro {titulo.strip()} agregado exitosamente!")

def buscar_libro(libros, titulo):
    for i in range(len(libros)):
        if libros [i]["titulo"].lower() == titulo.lower():
            return i
    return -1

def eliminar_libro(libros):
    titulo = input("Ingrese el nombre del libro a eliminar: ")
    posicion = buscar_libro(libros, titulo)
    if posicion != -1:
        libros.pop(posicion)
        print(f"¡Libro {titulo} eliminado correctamente!")
    else:
        print(f"¡El libro {titulo} no se encuentra registrado!")

def actualizar_disponibilidad(libros):
    for libro in libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False

def mostrar_libros(libros):
    actualizar_disponibilidad(libros)
    if len(libros) == 0:
        print("No hay libros registrados.")
        return
    print("\n=== LISTA DE LIBROS ===")
    for libro in libros:
        print(f"Titulo: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Prestamo: {libro['prestamo']}")
        if libro["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: SIN COPIAS")
        print("=====================================")
        
#Programa principal/main
libros = []
menu = True
while menu:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_libro(libros)

    elif opcion == 2:
        titulo = input("Ingrese el nombre del libro a buscar: ")
        posicion = buscar_libro(libros, titulo)
        if posicion != -1:
            print(f"¡Libro encontrado en la posición {posicion}!")
            print(f"Título: {libros[posicion]['titulo']}")
            print(f"Copias: {libros[posicion]['copias']}")
            print(f"Préstamo: {libros[posicion]['prestamo']}")
            if libros[posicion]["disponible"]:
                print("Estado: DISPONIBLE")
            else:
                print("Estado: SIN COPIAS")

        else:
            print(f"El libro '{titulo}' no se encuentra registrada.")

    elif opcion == 3:
        eliminar_libro(libros)

    elif opcion == 4:
        actualizar_disponibilidad(libros)
        print("Disponibilidad actualizada correctamente.")

    elif opcion == 5:
        mostrar_libros(libros)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        menu = False