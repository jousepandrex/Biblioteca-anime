#Programa que permite hacer lo siguiente: Agregar, editar, borrar y guardar datos

print("Bienvenido a la biblioteca Pandrex, por favor ingrese su nombre y una opción")
nombre = input("Por favor ingrese su nombre: ")
while True:
    print("opción 1: anime favorito")
    print("\nopción 2: canción favorita")
    print("\nopción 3: artista favorito")
    print("\nopción 4: videojuego favorito")
    print("\nopción 5: personaje favorito")
    print("\nopción 6: salir\n")

    menu = int(input("Por favor ingrese una opción: "))

    if menu == 1:
        anime = input("Por favor ingrese el nombre de su anime favorito: ")
        print(f"Nombre: {nombre} \nAnime favorito: {anime}")
        
    elif menu == 2:
        cancion = input("Por favor ingrese el nombre de su cancion favorita: ")
        print(f"Nombre: {nombre} \nCanción favorita: {cancion}")
        
    elif menu == 3:
        artista = input("Por favor ingrese el nombre de su artista favorito: ")
        print(f"Nombre: {nombre} \nArtista favorita: {artista}")
        
    elif menu == 4:
        videojuego = input("Por favor ingrese el nombre de su videojuego favorito: ")
        print(f"Nombre: {nombre} \nVideojuego favorito: {videojuego}")
        
    elif menu == 5:
        personaje = input("Por favor ingrese el nombre de su personaje favorito: ")
        print(f"Nombre: {nombre} \nPersonaje favorita: {personaje}")
        
    elif menu == 6:
        print("Ha seleccionado salir")
        break

