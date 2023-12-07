#Programa que permite hacer lo siguiente: Agregar, editar, borrar y guardar datos

print("Bienvenido a la biblioteca Pandrex, por favor ingrese su nombre y una opción")
nombre = input("Por favor ingrese su nombre: ")
while True:
    print("\nopción 1: añadir un nuevo anime")
    print("\nopción 2: editar un anime")
    print("\nopción 3: eliminar un anime")
    print("\nopción 4: salir\n")

    menu = int(input("Por favor ingrese una opción: "))

    if menu == 1:
        anime = input("Por favor ingrese el nombre de su anime favorito: ")
        lista = [anime]
        print(f"Nombre: {nombre} \nNuevo anime añadido: {lista}")
        
    elif menu == 2:
        cancion = input("Por favor ingrese el nombre del anime que desea editar: ")
        print(f"Nombre: {nombre} \nHas elegido editar {anime}")
        
    elif menu == 3:
        artista = input("Por favor ingrese el nombre del anime que desea eliminar: ")
        print(f"Nombre: {nombre} \nHas elegido eliminar {anime}")
        
    elif menu == 4:
        print("Ha seleccionado salir")
        break

