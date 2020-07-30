prueba = "Tony,Mierda123"
with open("Usuarios.txt", "r") as usuarios:
    if prueba in usuarios:
        print("si")
    else:
        print("no")