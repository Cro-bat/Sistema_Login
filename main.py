continuar = True
while continuar:
    # Preguntar login/register
    entrada = input("Bievenido, ¿Qué acción desea efectuar? Login/Register/Eliminar Registros\n").lower()
    entradas_posibles = ["login", "register", "eliminar registros", "eliminar"]

    while entrada not in entradas_posibles:
        entrada = input("Entrada inválida. ¿Qué acción desea efectuar? Login/Register/Eliminar Registros\n").lower()

        # Si register
    if entrada == "register":
        usuarios = open("Usuarios.txt", "a")
        nuevo_usuario = input("Introduzca nuevo usuario: ")
        # revisar usuario
        with open("usuarios.txt") as revisando:
            if nuevo_usuario in revisando.read():
                nuevo_usuario = input("Usuario ya existente. Introduzca nuevo usuario: ")
        usuarios.write(nuevo_usuario + ",")
        usuarios.close()
        # revisar contraseña
        with open("Usuarios.txt", "a") as usuarios:
            nueva_contra = ""
            while len(nueva_contra) <= 6:
                nueva_contra = input("Introduzca contraseña (más de 6 caracteres):\n")
            usuarios.write(nueva_contra + "\n")
        # aceptar/negar registro
        print(f"\nFelicidades su usuario ha quedado registrado como:\n"
              f"Usuario: {nuevo_usuario}\n"
              f"Contraseña: {nueva_contra}")

        # Si login
    elif entrada == "login":
        # preguntar usuario
        with open("Usuarios.txt", "r") as usuarios:
            usuario_actual = input("Introduzca su nombre de usuario: ")
            # while usuario_actual not in usuarios:
            #     usuario_actual = input("Usuario no encontrado, introduzca un usuario existente: ")
            # preguntar contraseña
            contra_actual = input("Introduzca contraseña: ")
            # revisar usuario
            if f"{usuario_actual},{contra_actual}\n" in usuarios:
                # aceptar ingreso
                print(f"Acceso concedido, bienvenido {usuario_actual}.")
                # denegar ingreso
            else:
                print("Acceso denegado, intentelo de nuevo.")

    else:
        confirmar_eliminar = False
        pregunta_eliminar = input("¿Está seguro de que desea eliminar los registros existentes?\n").lower()
        if pregunta_eliminar in ["yes", "si", "y", "s"]:
            usuarios = open("Usuarios.txt", "w")
            usuarios.write("")
            print("Registros eliminados con éxito.")

    # Preguntar repetir
    pregunta_continuar = input("¿Desea continuar?\n").lower()
    if pregunta_continuar not in ["yes", "si", "y", "s"]:
        continuar = False
